#pragma once
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <iostream>
#include <cstdlib>

using namespace std;

string text;
string abc;
string encode;
string decode;

int *freq;

const int first_qtr = 65535 / 4 + 1;
const int half = 2 * first_qtr;
const int third_qtr = 3 * first_qtr;

class ArithmeticCoding
{
    public:
        void get_text()
        {
            string path = "input.txt";
            ifstream fin;
            fin.open(path);
            char symbol;
            while (fin.get(symbol))
            {
                text += symbol;
            }
            fin.close();
            text.push_back('\0');
        }

        void get_abc()
        {
            bool exit_flag = 0;
            abc.push_back('-');
            for (int i = 0; i < text.size(); i++)
            {
                exit_flag = 0;
                for (int g = 0; g < abc.size(); g++)
                {
                    if (abc[g] == text[i])
                    {
                        exit_flag = 1;
                        break;
                    }
                }
                if (exit_flag == 1)
                {
                    continue;
                }
                else
                {
                    abc.push_back(text[i]);
                    continue;
                }
            }
            sort(abc.begin() + 1, abc.end());
        }

        void get_frequency()
        {
            freq = new int[abc.size()];
            for (int i = 0; i < abc.size(); i++)
            {
                freq[i] = 0;
            }
            for (int i = 0; i < abc.size(); i++)
            {
                for (int g = 0; g < text.size(); g++)
                {
                    if (abc[i] == text[g])
                    {
                        freq[i] += 1;
                    }
                }
            }
        }

        void encode_text()
        {
            int mass_size = text.length();
            unsigned short int* _low = new unsigned short int[mass_size];
            unsigned short int* _high = new unsigned short int[mass_size];
            _low[0] = 0;
            _high[0] = 65535;
            int element = 1;
            int position = 0;
            unsigned int range = 0;
            int del = freq[abc.size() - 1];
            int bits_to_foll = 0;
            string code = "";

            while (position < text.length())
            {
                get_next_symbol(position, &element);
                position += 1;

                range = _high[position - 1] - _low[position - 1] + 1;
                _low[position] = _low[position - 1] + (range * freq[element - 1]) / del;
                _high[position] = _low[position - 1] + (range * freq[element]) / del - 1;

                for (;;)
                {
                    if (_high[position] < half)
                    {
                        code += write_bits(0, bits_to_foll);
                        bits_to_foll = 0;
                    }
                    else if (_low[position] >= half)
                    {
                        code += write_bits(1, bits_to_foll);
                        bits_to_foll = 0;
                        _low[position] -= half;
                        _high[position] -= half;
                    }
                    else if (_low[position] >= first_qtr && _high[position] < third_qtr)
                    {
                        bits_to_foll += 1;
                        _low[position] -= first_qtr;
                        _high[position] -= first_qtr;
                    }
                    else
                    {
                        break;
                    }
                    _low[position] = 2 * _low[position];
                    _high[position] = 2 * _high[position] + 1;
                }
            }
            encode = code;
        }

        void get_next_symbol(int position, int *element)
        {
            bool exit = false;
            for (position; position < text.size() && !exit; position++)
            {
                char temp_text = text[position];
                for (int i = 0; i < abc.size(); i++)
                {
                    char temp_abc = abc[i];
                    if (temp_text == temp_abc)
                    {
                        *element = i;
                        exit = true;
                        break;
                    }
                }
            }
        }

        string write_bits(bool bit, int bits_to_foll)
        {
            string temp;
            temp += to_string(bit);
            while (bits_to_foll > 0)
            {
                temp += to_string(!bit);
                bits_to_foll -= 1;
            }
            return temp;
        }
};


int main()
{
    ArithmeticCoding coding;
	coding.get_text();
    coding.get_abc();
    coding.get_frequency();
    
    cout << abc << "\n";
    for (int i = 0; i < abc.size(); i++)
    {
        if (abc[i] != '\n')
        {
            cout << abc[i]<< " ";
            cout << freq[i] << "\n";
        }
        
    }
    coding.encode_text();
    cout << encode << "\n";

    
}



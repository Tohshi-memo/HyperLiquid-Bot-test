# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T03:52:30.756835+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_4h` score `38.7438` n `90` status `ready` deltaP `-3.7442` edge `3.3075` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8804` n `62` status `ready` deltaP `38.3586` edge `0.6713` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.9914` n `62` status `ready` deltaP `22.5635` edge `0.5666` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.3662` n `62` status `ready` deltaP `16.0009` edge `0.4338` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.8785` n `62` status `ready` deltaP `35.4059` edge `0.1705` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.395` n `90` status `ready` deltaP `10.6563` edge `0.7898` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.0253` n `62` status `ready` deltaP `33.0019` edge `0.0583` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4671` n `62` status `ready` deltaP `10.1748` edge `0.1733` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3756` n `90` status `ready` deltaP `16.4231` edge `0.1849` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.2932` n `62` status `ready` deltaP `18.179` edge `0.1297` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.984` n `62` status `ready` deltaP `24.8745` edge `0.0145` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.8616` n `90` status `ready` deltaP `13.5636` edge `0.1076` maxDD `-1.0977`
- `news_risk_high->unknown_4h` score `1.5234` n `62` status `ready` deltaP `-6.7192` edge `0.2963` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4502` n `62` status `ready` deltaP `21.0144` edge `0.0874` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2393` n `90` status `ready` deltaP `21.5371` edge `0.1638` maxDD `-3.5466`
- `market_context_high->fx_4h` score `1.0926` n `90` status `ready` deltaP `22.0396` edge `0.0188` maxDD `-0.3077`
- `news_risk_high->crypto_alt_1h` score `1.0795` n `62` status `ready` deltaP `2.8588` edge `0.1228` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7118` n `90` status `ready` deltaP `11.9461` edge `0.0039` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1386` n `90` status `ready` deltaP `10.1031` edge `0.0393` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.1284` n `90` status `ready` deltaP `7.1964` edge `0.5623` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

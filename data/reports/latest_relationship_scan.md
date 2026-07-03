# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T16:37:25.848715+00:00`
- Price records: `672`
- Market context records: `5575`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11396`

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

- `market_context_high->equity_24h` score `4.3099` n `174` status `ready` deltaP `15.0084` edge `0.767` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2438` n `191` status `ready` deltaP `11.1903` edge `0.2583` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `0.878` n `174` status `ready` deltaP `13.7991` edge `0.4352` maxDD `-29.6555`
- `market_context_high->fx_24h` score `0.8185` n `174` status `ready` deltaP `17.0977` edge `0.0516` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.6516` n `191` status `ready` deltaP `5.815` edge `0.1794` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.6392` n `191` status `ready` deltaP `6.6371` edge `0.1731` maxDD `-9.46`
- `market_context_high->index_1h` score `-0.2213` n `203` status `ready` deltaP `3.4195` edge `0.0081` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-0.2771` n `191` status `ready` deltaP `6.1199` edge `0.0095` maxDD `-0.8712`
- `market_context_high->equity_1h` score `-0.2871` n `203` status `ready` deltaP `5.5448` edge `0.0398` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.4431` n `203` status `ready` deltaP `1.3185` edge `0.0011` maxDD `-0.4122`
- `market_context_high->metal_1h` score `-0.5347` n `203` status `ready` deltaP `-0.2898` edge `0.0009` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6668` n `203` status `ready` deltaP `0.3577` edge `0.0382` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7854` n `203` status `ready` deltaP `2.2794` edge `0.0439` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.2446` n `203` status `ready` deltaP `-2.8155` edge `-0.0084` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5247` n `191` status `ready` deltaP `2.5148` edge `0.0171` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.9956` n `174` status `ready` deltaP `13.386` edge `0.0536` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0783` n `191` status `ready` deltaP `-14.1593` edge `-0.0619` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.4596` n `191` status `ready` deltaP `-7.5118` edge `-0.054` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.8646` n `174` status `ready` deltaP `-7.6329` edge `-0.2213` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.1266` n `174` status `ready` deltaP `3.7596` edge `0.0841` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

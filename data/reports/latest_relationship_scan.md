# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T20:37:31.165697+00:00`
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

- `market_context_high->unknown_4h` score `38.1899` n `90` status `ready` deltaP `-5.4185` edge `3.2725` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8319` n `62` status `ready` deltaP `37.902` edge `0.6703` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0126` n `62` status `ready` deltaP `22.2591` edge `0.5704` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.6335` n `62` status `ready` deltaP `11.0224` edge `0.3226` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.2468` n `62` status `ready` deltaP `30.4498` edge `0.1509` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.259` n `90` status `ready` deltaP `8.835` edge `0.6563` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8424` n `62` status `ready` deltaP `31.4799` edge `0.0532` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.442` n `62` status `ready` deltaP `10.0251` edge `0.1722` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3271` n `90` status `ready` deltaP `15.9665` edge `0.1839` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0621` n `62` status `ready` deltaP `17.5701` edge `0.1145` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9636` n `62` status `ready` deltaP `24.7248` edge `0.0138` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4782` n `62` status `ready` deltaP `21.0144` edge `0.091` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.1274` n `62` status `ready` deltaP `3.1582` edge `0.1248` maxDD `-2.4854`
- `news_risk_high->unknown_4h` score `0.9695` n `62` status `ready` deltaP `-8.3935` edge `0.2613` maxDD `-5.6309`
- `market_context_high->metal_24h` score `0.9501` n `90` status `ready` deltaP `19.5617` edge `0.1399` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.9141` n `90` status `ready` deltaP `20.2131` edge `0.0161` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6663` n `90` status `ready` deltaP `11.497` edge `0.0031` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.129` n `90` status `ready` deltaP `8.5851` edge `-0.0036` maxDD `-1.0977`
- `news_risk_high->metal_1h` score `0.1257` n `62` status `ready` deltaP `6.6013` edge `0.0083` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.1222` n `90` status `ready` deltaP `9.9534` edge `0.0382` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

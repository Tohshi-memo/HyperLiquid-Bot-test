# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T09:37:29.998896+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8300`

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

- `market_context_high->unknown_1h` score `70.6614` n `124` status `ready` deltaP `-0.6422` edge `5.9342` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `53.2547` n `112` status `ready` deltaP `-1.372` edge `4.4966` maxDD `-1.9648`
- `market_context_high->crypto_major_24h` score `10.9496` n `81` status `ready` deltaP `29.8032` edge `0.7274` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3431` n `65` status `ready` deltaP `32.5516` edge `0.5819` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1094` n `81` status `ready` deltaP `25.3666` edge `0.4853` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8308` n `65` status `ready` deltaP `19.7866` edge `0.4884` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.5301` n `112` status `ready` deltaP `15.2439` edge `0.2723` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3596` n `65` status `ready` deltaP `23.7847` edge `0.1214` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1752` n `65` status `ready` deltaP `11.2073` edge `0.1999` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.929` n `65` status `ready` deltaP `32.2186` edge `0.0555` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5434` n `65` status `ready` deltaP `20.4245` edge `0.1368` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4053` n `65` status `ready` deltaP `9.567` edge `0.1722` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0471` n `65` status `ready` deltaP `25.3178` edge `0.0168` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.886` n `65` status `ready` deltaP `17.7064` edge `0.0807` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.43` n `112` status `ready` deltaP `25.3702` edge `0.0257` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.0474` n `65` status `ready` deltaP `3.0723` edge `0.1187` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9196` n `124` status `ready` deltaP `14.8831` edge `0.0058` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.828` n `124` status `ready` deltaP `10.3487` edge `0.0889` maxDD `-3.7778`
- `market_context_high->crypto_alt_4h` score `0.5992` n `112` status `ready` deltaP `2.2866` edge `0.2136` maxDD `-7.6465`
- `news_risk_high->commodity_24h` score `0.5433` n `65` status `ready` deltaP `24.9119` edge `0.1067` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

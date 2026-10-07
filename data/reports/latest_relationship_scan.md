# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T11:07:27.794166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_4h` score `36.5888` n `94` status `ready` deltaP `-4.8067` edge `3.135` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.3922` n `62` status `ready` deltaP `35.9904` edge `0.6464` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1128` n `62` status `ready` deltaP `23.3921` edge `0.5712` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.6212` n `62` status `ready` deltaP `26.2153` edge `0.127` maxDD `0.0`
- `news_risk_high->index_4h` score `2.9185` n `62` status `ready` deltaP `32.6121` edge `0.052` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.8321` n `62` status `ready` deltaP `7.0901` edge `0.1987` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.261` n `62` status `ready` deltaP `8.6778` edge `0.1661` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.0795` n `62` status `ready` deltaP `18.5386` edge `0.1095` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.0748` n `94` status `ready` deltaP `14.2677` edge `0.1742` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0079` n `62` status `ready` deltaP `25.3236` edge `0.0135` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4437` n `62` status `ready` deltaP `20.4858` edge `0.0901` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.1598` n `62` status `ready` deltaP `3.3079` edge `0.1265` maxDD `-2.4854`
- `market_context_high->crypto_major_24h` score `1.1427` n `94` status `ready` deltaP `5.1271` edge `0.4097` maxDD `-16.7906`
- `market_context_high->fx_1h` score `0.872` n `94` status `ready` deltaP `13.9476` edge `0.0039` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.6134` n `94` status `ready` deltaP `16.8883` edge `0.0142` maxDD `-0.3868`
- `market_context_high->metal_24h` score `0.3736` n `94` status `ready` deltaP `16.0202` edge `0.0896` maxDD `-3.5466`
- `news_risk_high->commodity_24h` score `0.3595` n `62` status `ready` deltaP `25.9801` edge `0.0295` maxDD `-8.196`
- `news_risk_high->metal_1h` score `0.188` n `62` status `ready` deltaP `7.3498` edge `0.0085` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.1464` n `94` status `ready` deltaP `10.1191` edge `0.0402` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `0.1074` n `94` status `ready` deltaP `5.7682` edge `0.0081` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

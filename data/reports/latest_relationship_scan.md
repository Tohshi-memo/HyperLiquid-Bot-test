# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T10:37:26.532691+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8312`

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

- `market_context_high->unknown_1h` score `75.9942` n `124` status `ready` deltaP `-0.6422` edge `6.3786` maxDD `-0.9839`
- `market_context_high->crypto_major_24h` score `10.7384` n `81` status `ready` deltaP `29.8032` edge `0.7098` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3947` n `65` status `ready` deltaP `32.5516` edge `0.5862` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.5718` n `81` status `ready` deltaP `25.3666` edge `0.4405` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.892` n `65` status `ready` deltaP `19.7866` edge `0.4935` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.3795` n `65` status `ready` deltaP `23.9583` edge `0.1219` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.2805` n `112` status `ready` deltaP `15.2439` edge `0.2515` maxDD `-4.047`
- `news_risk_high->equity_24h` score `3.1354` n `65` status `ready` deltaP `10.8601` edge `0.1989` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9704` n `65` status `ready` deltaP `32.6759` edge `0.0559` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.57` n `65` status `ready` deltaP `20.5769` edge `0.138` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4713` n `65` status `ready` deltaP `9.8664` edge `0.1757` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0734` n `65` status `ready` deltaP `25.6172` edge `0.017` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8532` n `65` status `ready` deltaP `17.4015` edge `0.08` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5665` n `112` status `ready` deltaP `26.851` edge `0.0272` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1277` n `65` status `ready` deltaP `3.5214` edge `0.1224` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.8647` n `124` status `ready` deltaP `14.2264` edge `0.0056` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.5429` n `124` status `ready` deltaP `9.0352` edge `0.0739` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.5144` n `65` status `ready` deltaP `24.9119` edge `0.103` maxDD `-10.9169`
- `market_context_high->equity_24h` score `0.4913` n `81` status `ready` deltaP `8.3719` edge `-0.001` maxDD `-0.4427`
- `market_context_high->commodity_4h` score `0.4786` n `112` status `ready` deltaP `10.7796` edge `0.0474` maxDD `-2.3507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

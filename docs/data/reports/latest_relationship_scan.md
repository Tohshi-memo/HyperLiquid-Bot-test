# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T03:22:29.977776+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `3735.4757` n `49` status `ready` deltaP `22.2186` edge `311.1836` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.9815` n `40` status `ready` deltaP `51.4583` edge `0.8618` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.1618` n `40` status `ready` deltaP `51.3194` edge `0.6008` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `3.1112` n `49` status `ready` deltaP `6.4398` edge `0.2927` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.297` n `49` status `ready` deltaP `12.5622` edge `0.0624` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.5142` n `45` status `ready` deltaP `7.2087` edge `0.1025` maxDD `-2.7703`
- `news_risk_high->metal_4h` score `0.4241` n `49` status `ready` deltaP `9.8525` edge `0.0238` maxDD `-0.8085`
- `market_context_high->fx_4h` score `0.3691` n `45` status `ready` deltaP `15.7452` edge `0.0054` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.3666` n `47` status `ready` deltaP `7.5646` edge `0.034` maxDD `-1.3282`
- `news_risk_high->equity_1h` score `0.1452` n `49` status `ready` deltaP `4.8424` edge `0.0621` maxDD `-2.916`
- `news_risk_high->metal_1h` score `0.1181` n `49` status `ready` deltaP `5.6459` edge `0.0095` maxDD `-0.5599`
- `market_context_high->crypto_alt_4h` score `0.0896` n `45` status `ready` deltaP `4.0718` edge `0.0749` maxDD `-4.9116`
- `news_risk_high->index_1h` score `0.0518` n `49` status `ready` deltaP `4.7477` edge `0.0073` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `0.0255` n `49` status `ready` deltaP `4.5582` edge `0.004` maxDD `-0.2475`
- `market_context_high->fx_1h` score `-0.0162` n `47` status `ready` deltaP `6.8161` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.2552` n `49` status `ready` deltaP `4.2588` edge `0.0071` maxDD `-3.1233`
- `news_risk_high->commodity_1h` score `-0.2704` n `49` status `ready` deltaP `5.3067` edge `-0.0185` maxDD `-1.7898`
- `news_risk_high->fx_4h` score `-0.2731` n `49` status `ready` deltaP `5.4504` edge `0.0244` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.3333` n `49` status `ready` deltaP `4.5582` edge `-0.0011` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.7055` n `40` status `ready` deltaP `0.6597` edge `0.0348` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

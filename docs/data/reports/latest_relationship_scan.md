# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T16:37:26.680144+00:00`
- Price records: `672`
- Market context records: `2883`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `8.7614` n `142` status `ready` deltaP `8.084` edge `1.0679` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `4.9661` n `142` status `ready` deltaP `10.067` edge `0.3932` maxDD `-1.7175`
- `market_context_high->equity_24h` score `4.8683` n `142` status `ready` deltaP `9.4288` edge `0.5432` maxDD `-12.6963`
- `market_context_high->index_24h` score `2.2772` n `142` status `ready` deltaP `11.1062` edge `0.2138` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7088` n `142` status `ready` deltaP `15.5516` edge `0.3481` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.7378` n `142` status `ready` deltaP `6.0331` edge `0.1266` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6959` n `142` status `ready` deltaP `15.1301` edge `0.0725` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0087` n `142` status `ready` deltaP `4.6471` edge `0.0173` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.041` n `142` status `ready` deltaP `4.3308` edge `0.0408` maxDD `-3.1801`
- `market_context_high->equity_4h` score `-0.1478` n `142` status `ready` deltaP `4.4014` edge `0.0963` maxDD `-5.7037`
- `market_context_high->commodity_1h` score `-0.6124` n `142` status `ready` deltaP `-0.7316` edge `0.0017` maxDD `-4.3601`
- `market_context_high->crypto_alt_4h` score `-0.6237` n `142` status `ready` deltaP `14.4903` edge `0.2855` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.6609` n `142` status `ready` deltaP `4.9465` edge `0.0583` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.6772` n `142` status `ready` deltaP `-2.1843` edge `0.0025` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6808` n `142` status `ready` deltaP `-0.466` edge `0.0004` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.736` n `142` status `ready` deltaP `-1.7015` edge `0.0333` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.7588` n `142` status `ready` deltaP `4.9739` edge `0.0565` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1237` n `142` status `ready` deltaP `3.6671` edge `0.0235` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2771` n `142` status `ready` deltaP `-4.9725` edge `0.0046` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3723` n `142` status `ready` deltaP `-1.8852` edge `-0.0146` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

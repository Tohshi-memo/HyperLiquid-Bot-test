# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T23:37:31.582593+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5918`

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

- `news_risk_high->unknown_24h` score `5116.8798` n `61` status `ready` deltaP `23.8245` edge `426.2899` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `15.3183` n `40` status `ready` deltaP `52.6736` edge `0.9651` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.1786` n `40` status `ready` deltaP `51.3194` edge `0.6022` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.3655` n `61` status `ready` deltaP `14.4692` edge `0.3437` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.4074` n `61` status `ready` deltaP `13.4021` edge `0.066` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0407` n `40` status `ready` deltaP `13.5976` edge `0.1274` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7679` n `40` status `ready` deltaP `8.5061` edge `0.1323` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6457` n `40` status `ready` deltaP `20.4573` edge `0.026` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5031` n `43` status `ready` deltaP `9.9359` edge `0.0357` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.3135` n `43` status `ready` deltaP `11.3633` edge `0.0022` maxDD `-0.6874`
- `news_risk_high->equity_1h` score `0.2749` n `61` status `ready` deltaP `6.4641` edge `0.0621` maxDD `-2.916`
- `news_risk_high->fx_1h` score `-0.0404` n `61` status `ready` deltaP `3.3572` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `-0.0416` n `61` status `ready` deltaP `10.4983` edge `0.0223` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.119` n `61` status `ready` deltaP `1.8529` edge `0.0047` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1864` n `61` status `ready` deltaP `4.5475` edge `0.014` maxDD `-3.1233`
- `news_risk_high->metal_4h` score `-0.1894` n `61` status `ready` deltaP `2.2691` edge `0.0082` maxDD `-0.8085`
- `news_risk_high->commodity_1h` score `-0.329` n `61` status `ready` deltaP `5.8948` edge `-0.0137` maxDD `-2.0891`
- `news_risk_high->metal_1h` score `-0.3405` n `61` status `ready` deltaP `-0.5276` edge `0.0002` maxDD `-0.5599`
- `market_context_high->crypto_alt_1h` score `-0.492` n `43` status `ready` deltaP `-0.7137` edge `0.0044` maxDD `-3.0178`
- `news_risk_high->crypto_major_1h` score `-0.5265` n `61` status `ready` deltaP `0.2282` edge `0.003` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

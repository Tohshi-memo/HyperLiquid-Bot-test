# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T22:37:28.714179+00:00`
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

- `news_risk_high->unknown_24h` score `5007.6906` n `61` status `ready` deltaP `23.8245` edge `417.1908` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `15.7351` n `40` status `ready` deltaP `53.3681` edge `0.9952` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.1366` n `40` status `ready` deltaP `51.3194` edge `0.5987` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.4455` n `61` status `ready` deltaP `15.079` edge `0.3463` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.467` n `61` status `ready` deltaP `14.0119` edge `0.0669` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0376` n `40` status `ready` deltaP `13.5976` edge `0.127` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7648` n `40` status `ready` deltaP `8.5061` edge `0.1319` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6457` n `40` status `ready` deltaP `20.4573` edge `0.026` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.4466` n `42` status `ready` deltaP `9.2387` edge `0.0331` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.3962` n `42` status `ready` deltaP `12.803` edge `0.0032` maxDD `-0.6874`
- `news_risk_high->equity_1h` score `0.2965` n `61` status `ready` deltaP `6.6138` edge `0.0629` maxDD `-2.916`
- `news_risk_high->fx_1h` score `-0.0404` n `61` status `ready` deltaP `3.3572` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `-0.0416` n `61` status `ready` deltaP `10.4983` edge `0.0223` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.1096` n `61` status `ready` deltaP `2.0026` edge `0.0049` maxDD `-0.5845`
- `news_risk_high->metal_4h` score `-0.2004` n `61` status `ready` deltaP `2.1167` edge `0.0078` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `-0.2167` n `61` status `ready` deltaP `4.2481` edge `0.0121` maxDD `-3.1233`
- `news_risk_high->commodity_1h` score `-0.3049` n `61` status `ready` deltaP `6.1942` edge `-0.0126` maxDD `-2.0891`
- `news_risk_high->metal_1h` score `-0.3685` n `61` status `ready` deltaP `-0.9767` edge `-0.0004` maxDD `-0.5599`
- `market_context_high->crypto_alt_1h` score `-0.3949` n `42` status `ready` deltaP `0.1497` edge `0.0111` maxDD `-3.0178`
- `news_risk_high->crypto_major_1h` score `-0.5538` n `61` status `ready` deltaP `-0.0712` edge `0.0015` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

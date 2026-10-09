# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T00:52:29.338944+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.8212` n `91` status `ready` deltaP `-3.5965` edge `3.3963` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.111` n `49` status `ready` deltaP `43.2927` edge `0.8873` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.6366` n `49` status `ready` deltaP `44.2416` edge `0.8482` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.8511` n `49` status `ready` deltaP `28.2318` edge `0.726` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.3194` n `90` status `ready` deltaP `21.9122` edge `1.3461` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.1826` n `90` status `ready` deltaP `27.5062` edge `0.5414` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.7807` n `49` status `ready` deltaP `48.3536` edge `0.2427` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8579` n `49` status `ready` deltaP `32.233` edge `0.2938` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5417` n `49` status `ready` deltaP `45.3677` edge `0.0805` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.1282` n `90` status `ready` deltaP `13.6145` edge `0.9041` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.051` n `49` status `ready` deltaP `11.863` edge `0.2107` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.5591` n `49` status `ready` deltaP `5.8903` edge `0.2057` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4266` n `49` status `ready` deltaP `29.986` edge `0.0163` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.1561` n `49` status `ready` deltaP `29.194` edge `-0.0065` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.6645` n `91` status `ready` deltaP `17.554` edge `0.2294` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.247` n `90` status `ready` deltaP `21.5655` edge `0.1646` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1566` n `49` status `ready` deltaP `18.1433` edge `0.0689` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5271` n `91` status `ready` deltaP `15.9911` edge `0.012` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4009` n `91` status `ready` deltaP `8.3438` edge `0.002` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2717` n `91` status `ready` deltaP `10.2932` edge `0.0551` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

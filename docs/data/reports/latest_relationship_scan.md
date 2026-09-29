# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T13:22:38.913914+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7522`

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

- `news_risk_high->unknown_24h` score `2587.956` n `139` status `ready` deltaP `1.2153` edge `215.6549` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9798` n `139` status `ready` deltaP `32.9349` edge `1.5906` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.6391` n `139` status `ready` deltaP `36.0049` edge `0.9022` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.7993` n `139` status `ready` deltaP `26.2827` edge `1.0015` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.3581` n `139` status `ready` deltaP `39.9006` edge `0.1667` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.9072` n `139` status `ready` deltaP `31.9332` edge `0.2982` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.7504` n `142` status `ready` deltaP `27.9801` edge `0.2036` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0127` n `142` status `ready` deltaP `8.6332` edge `0.2928` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7477` n `142` status `ready` deltaP `6.8209` edge `0.1079` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6602` n `142` status `ready` deltaP `7.8519` edge `0.0688` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4802` n `142` status `ready` deltaP `8.7501` edge `0.0107` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0247` n `142` status `ready` deltaP `8.6826` edge `0.0295` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.425` n `142` status `ready` deltaP `1.8407` edge `0.0615` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5085` n `142` status `ready` deltaP `1.1638` edge `0.0128` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.327` n `142` status `ready` deltaP `8.674` edge `-0.0066` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3681` n `142` status `ready` deltaP `-8.1544` edge `0.0284` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7778` n `142` status `ready` deltaP `-4.8352` edge `0.0758` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8073` n `142` status `ready` deltaP `-8.845` edge `-0.0036` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9476` n `142` status `ready` deltaP `-10.5022` edge `-0.0122` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.4411` n `142` status `ready` deltaP `-10.6793` edge `0.0001` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

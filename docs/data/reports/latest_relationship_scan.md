# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T01:52:26.657611+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_1h` score `350.8647` n `53` status `ready` deltaP `11.6456` edge `29.166` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.715` n `50` status `ready` deltaP `12.9573` edge `26.7232` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.2312` n `50` status `ready` deltaP `29.286` edge `1.0777` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.0907` n `50` status `ready` deltaP `35.0329` edge `0.8323` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `11.0049` n `61` status `ready` deltaP `29.5053` edge `0.756` maxDD `-2.1837`
- `news_risk_high->crypto_major_4h` score `10.485` n `67` status `ready` deltaP `37.5705` edge `0.6436` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.179` n `67` status `ready` deltaP `24.8043` edge `0.5673` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.035` n `50` status `ready` deltaP `16.0183` edge `0.5498` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.43` n `50` status `ready` deltaP `14.2073` edge `0.4867` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6278` n `61` status `ready` deltaP `32.9431` edge `0.1771` maxDD `-0.2189`
- `news_risk_high->equity_4h` score `3.8242` n `67` status `ready` deltaP `26.7223` edge `0.2018` maxDD `-2.9013`
- `news_risk_high->index_4h` score `2.9958` n `67` status `ready` deltaP `32.6924` edge `0.0579` maxDD `-0.4296`
- `market_context_high->fx_4h` score `2.959` n `50` status `ready` deltaP `33.1463` edge `0.0391` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.849` n `67` status `ready` deltaP `12.3827` edge `0.1904` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.5314` n `53` status `ready` deltaP `10.4678` edge `0.1862` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.484` n `53` status `ready` deltaP `9.4199` edge `0.2105` maxDD `-3.6376`
- `news_risk_high->metal_4h` score `2.4425` n `67` status `ready` deltaP `20.8227` edge `0.1063` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1045` n `67` status `ready` deltaP `25.9608` edge `0.0173` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.3864` n `50` status `ready` deltaP `7.3414` edge `0.315` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.3526` n `67` status `ready` deltaP `3.8721` edge `0.1388` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

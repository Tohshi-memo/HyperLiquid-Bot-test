# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T00:37:31.039520+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4256`

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

- `market_context_high->unknown_1h` score `382.1371` n `50` status `ready` deltaP `12.9701` edge `31.7632` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.6666` n `50` status `ready` deltaP `12.6524` edge `26.7212` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.272` n `50` status `ready` deltaP `29.286` edge `1.0811` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.1978` n `50` status `ready` deltaP `35.7262` edge `0.8366` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.6165` n `62` status `ready` deltaP `28.9177` edge `0.7404` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4956` n `68` status `ready` deltaP `38.3339` edge `0.6394` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1866` n `68` status `ready` deltaP `25.3946` edge `0.564` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0957` n `50` status `ready` deltaP `16.628` edge `0.5508` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.47` n `50` status `ready` deltaP `14.5122` edge `0.488` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.4553` n `62` status `ready` deltaP `32.0764` edge `0.1733` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8291` n `68` status `ready` deltaP `26.9637` edge `0.2006` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `2.9845` n `50` status `ready` deltaP `12.5569` edge `0.2313` maxDD `-3.6376`
- `news_risk_high->index_4h` score `2.9595` n `68` status `ready` deltaP `32.3888` edge `0.0569` maxDD `-0.4296`
- `market_context_high->fx_4h` score `2.9468` n `50` status `ready` deltaP `32.9939` edge `0.0391` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.8767` n `68` status `ready` deltaP `12.7598` edge `0.1902` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8119` n `50` status `ready` deltaP `12.0539` edge `0.199` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3868` n `68` status `ready` deltaP `20.2924` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9959` n `68` status `ready` deltaP `24.6478` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5454` n `50` status `ready` deltaP `21.5389` edge `0.0116` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.4728` n `50` status `ready` deltaP `8.208` edge `0.3203` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T06:07:27.084750+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4826`

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

- `market_context_high->unknown_1h` score `366.2242` n `50` status `ready` deltaP `11.024` edge `30.4501` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.5922` n `50` status `ready` deltaP `11.4329` edge `24.3898` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.7146` n `50` status `ready` deltaP `24.1736` edge `0.9854` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.7462` n `70` status `ready` deltaP `33.7351` edge `0.7191` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.2778` n `50` status `ready` deltaP `31.8264` edge `0.7026` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `8.9735` n `85` status `ready` deltaP `35.6868` edge `0.5302` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.7121` n `85` status `ready` deltaP `31.0474` edge `0.5701` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.2685` n `50` status `ready` deltaP `16.628` edge `0.5652` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.9055` n `50` status `ready` deltaP `16.3415` edge `0.5121` maxDD `-7.6465`
- `news_risk_high->index_24h` score `3.9684` n `70` status `ready` deltaP `33.0407` edge `0.1263` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8123` n `85` status `ready` deltaP `30.5039` edge `0.1756` maxDD `-2.9013`
- `news_risk_high->crypto_alt_24h` score `3.7122` n `70` status `ready` deltaP `11.6022` edge `0.7024` maxDD `-18.3063`
- `market_context_high->crypto_alt_1h` score `3.1954` n `50` status `ready` deltaP `14.3533` edge `0.2369` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9222` n `50` status `ready` deltaP `12.8024` edge `0.2032` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8165` n `50` status `ready` deltaP `31.4695` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.5946` n `85` status `ready` deltaP `13.5083` edge `0.1617` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `1.779` n `85` status `ready` deltaP `14.9444` edge `0.0902` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.6985` n `85` status `ready` deltaP `7.1768` edge `0.1456` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `1.3577` n `85` status `ready` deltaP `13.894` edge `0.0567` maxDD `-0.8948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

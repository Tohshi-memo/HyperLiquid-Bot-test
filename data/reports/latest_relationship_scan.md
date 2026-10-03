# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T07:37:29.253384+00:00`
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

- `market_context_high->unknown_1h` score `366.1954` n `50` status `ready` deltaP `11.024` edge `30.4477` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.8272` n `50` status `ready` deltaP `12.1951` edge `24.4043` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.1148` n `50` status `ready` deltaP `25.2153` edge `1.0118` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.8986` n `70` status `ready` deltaP `33.7351` edge `0.7318` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.6168` n `50` status `ready` deltaP `32.8681` edge `0.7239` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `9.4061` n `79` status `ready` deltaP `36.5796` edge `0.5603` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5897` n `79` status `ready` deltaP `30.3431` edge `0.5646` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3437` n `50` status `ready` deltaP `17.2378` edge `0.5674` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.0345` n `50` status `ready` deltaP `16.7988` edge `0.5198` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.164` n `70` status `ready` deltaP `33.0407` edge `0.1426` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9221` n `79` status `ready` deltaP `30.4357` edge `0.1852` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2865` n `50` status `ready` deltaP `14.9521` edge `0.2405` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9881` n `50` status `ready` deltaP `13.4012` edge `0.2047` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8811` n `50` status `ready` deltaP `32.2317` edge `0.0387` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.7002` n `79` status `ready` deltaP `13.9582` edge `0.1675` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.1691` n `79` status `ready` deltaP `19.0703` edge `0.0952` maxDD `-0.993`
- `news_risk_high->index_4h` score `1.772` n `79` status `ready` deltaP `22.231` edge `0.0465` maxDD `-0.4296`
- `news_risk_high->crypto_alt_1h` score `1.6868` n `79` status `ready` deltaP `7.1799` edge `0.1446` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4484` n `50` status `ready` deltaP `20.3413` edge `0.0115` maxDD `-0.113`
- `market_context_high->fx_24h` score `1.3212` n `50` status `ready` deltaP `25.5417` edge `0.1009` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

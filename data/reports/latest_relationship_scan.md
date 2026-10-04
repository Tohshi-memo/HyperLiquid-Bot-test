# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T02:37:30.396143+00:00`
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

- `market_context_high->unknown_1h` score `323.1153` n `56` status `ready` deltaP `11.8478` edge `26.8522` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.769` n `50` status `ready` deltaP `12.9573` edge `26.7277` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.0792` n `50` status `ready` deltaP `28.766` edge `1.0685` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `12.1282` n `59` status `ready` deltaP `32.0418` edge `0.8071` maxDD `-0.1353`
- `market_context_high->crypto_major_24h` score `10.94` n `50` status `ready` deltaP `34.513` edge `0.8232` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.9222` n `65` status `ready` deltaP `40.0211` edge `0.6637` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3209` n `65` status `ready` deltaP `24.2073` edge `0.5831` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.007` n `50` status `ready` deltaP `15.7134` edge `0.5495` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.43` n `50` status `ready` deltaP `14.2073` edge `0.4867` maxDD `-7.6465`
- `news_risk_high->index_24h` score `5.1098` n `59` status `ready` deltaP `35.7019` edge `0.1878` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8586` n `65` status `ready` deltaP `26.522` edge `0.206` maxDD `-2.9013`
- `news_risk_high->crypto_major_1h` score `3.049` n `65` status `ready` deltaP `13.9083` edge `0.1969` maxDD `-1.5096`
- `news_risk_high->index_4h` score `3.0258` n `65` status `ready` deltaP `32.8284` edge `0.0595` maxDD `-0.4296`
- `market_context_high->fx_4h` score `2.9956` n `50` status `ready` deltaP `33.6037` edge `0.0391` maxDD `-0.0791`
- `news_risk_high->metal_4h` score `2.6036` n `65` status `ready` deltaP `22.432` edge `0.109` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.5684` n `56` status `ready` deltaP `12.0402` edge `0.1788` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.104` n `56` status `ready` deltaP `7.7203` edge `0.1985` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.0842` n `65` status `ready` deltaP `25.6172` edge `0.0179` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5906` n `65` status `ready` deltaP `5.4675` edge `0.148` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.3087` n `50` status `ready` deltaP `6.8215` edge `0.3085` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

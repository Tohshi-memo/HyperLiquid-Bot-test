# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T16:52:32.345960+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6796`

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

- `market_context_high->unknown_1h` score `334.5782` n `50` status `ready` deltaP `7.8802` edge `27.8339` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `284.4304` n `50` status `ready` deltaP `6.8598` edge `23.6568` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.1088` n `111` status `ready` deltaP `34.4829` edge `1.4668` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.0474` n `50` status `ready` deltaP `32.5208` edge `0.7621` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.5168` n `50` status `ready` deltaP `20.2866` edge `0.5615` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.238` n `50` status `ready` deltaP `17.1037` edge `0.4518` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `5.0452` n `111` status `ready` deltaP `21.692` edge `0.5912` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.8217` n `50` status `ready` deltaP `10.2847` edge `0.5042` maxDD `-11.6768`
- `market_context_high->equity_24h` score `4.0167` n `50` status `ready` deltaP `19.3889` edge `0.5719` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.4205` n `124` status `ready` deltaP `27.0506` edge `0.1743` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1516` n `50` status `ready` deltaP `35.4329` edge `0.0399` maxDD `-0.0791`
- `news_risk_high->equity_24h` score `3.1224` n `111` status `ready` deltaP `22.5601` edge `0.4848` maxDD `-9.4579`
- `market_context_high->crypto_major_1h` score `3.0803` n `50` status `ready` deltaP `14.8982` edge `0.2024` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.989` n `50` status `ready` deltaP `13.7545` edge `0.2237` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5285` n `111` status `ready` deltaP `24.7983` edge `0.0932` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2874` n `111` status `ready` deltaP `26.9942` edge `0.2407` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5514` n `50` status `ready` deltaP `21.5389` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.8819` n `50` status `ready` deltaP `14.6181` edge `0.0727` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.5385` n `124` status `ready` deltaP `7.3402` edge `0.0496` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.5227` n `50` status `ready` deltaP `14.4306` edge `0.0726` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

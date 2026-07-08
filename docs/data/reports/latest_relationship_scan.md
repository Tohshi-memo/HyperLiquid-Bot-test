# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T13:22:29.362275+00:00`
- Price records: `672`
- Market context records: `6091`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11095`

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

- `news_risk_high->fx_24h` score `8.1618` n `30` status `ready` deltaP `72.7431` edge `0.1952` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.4625` n `30` status `ready` deltaP `32.743` edge `0.335` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3005` n `32` status `ready` deltaP `44.7409` edge `0.0647` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4314` n `32` status `ready` deltaP `29.1916` edge `0.0219` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.8501` n `196` status `ready` deltaP `9.8992` edge `0.1799` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.2082` n `32` status `ready` deltaP `13.3795` edge `0.1124` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6634` n `32` status `ready` deltaP `9.0756` edge `0.0707` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.3401` n `30` status `ready` deltaP `17.7431` edge `-0.0694` maxDD `-0.3101`
- `news_risk_high->index_24h` score `0.1171` n `30` status `ready` deltaP `9.2361` edge `0.0406` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2631` n `196` status `ready` deltaP `1.6406` edge `-0.0001` maxDD `-0.5659`
- `market_context_high->metal_1h` score `-0.4246` n `196` status `ready` deltaP `3.8158` edge `0.0` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.5095` n `196` status `ready` deltaP `2.2241` edge `0.0314` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.5294` n `196` status `ready` deltaP `4.511` edge `0.0208` maxDD `-3.4996`
- `market_context_high->index_4h` score `-0.6673` n `196` status `ready` deltaP `4.4519` edge `0.0312` maxDD `-1.381`
- `market_context_high->commodity_1h` score `-0.6938` n `196` status `ready` deltaP `-1.497` edge `-0.0032` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.6983` n `32` status `ready` deltaP `-1.7964` edge `-0.0278` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.7147` n `196` status `ready` deltaP `-1.442` edge `0.0049` maxDD `-0.9531`
- `market_context_high->crypto_alt_1h` score `-0.8653` n `196` status `ready` deltaP `4.2924` edge `0.0357` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9516` n `196` status `ready` deltaP `4.3872` edge `0.0255` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0369` n `32` status `ready` deltaP `-8.7762` edge `-0.0181` maxDD `-1.1725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

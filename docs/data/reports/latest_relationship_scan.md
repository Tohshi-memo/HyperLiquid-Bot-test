# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T15:06:16.024154+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4822`

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

- `market_context_high->unknown_1h` score `359.5005` n `50` status `ready` deltaP `11.1737` edge `29.8888` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.4734` n `50` status `ready` deltaP `11.128` edge `24.2986` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.2881` n `73` status `ready` deltaP `39.795` edge `1.0296` maxDD `-1.005`
- `news_risk_high->equity_24h` score `9.4358` n `73` status `ready` deltaP `33.7947` edge `0.6095` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.1846` n `50` status `ready` deltaP `32.5208` edge `0.6902` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.9627` n `50` status `ready` deltaP `16.5347` edge `0.807` maxDD `-11.6271`
- `market_context_high->crypto_major_4h` score `6.6174` n `50` status `ready` deltaP `16.0183` edge `0.515` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.6388` n `50` status `ready` deltaP `13.9024` edge `0.4228` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.4598` n `116` status `ready` deltaP `19.7645` edge `0.3743` maxDD `-6.4195`
- `market_context_high->fx_4h` score `2.8895` n `50` status `ready` deltaP `32.2317` edge `0.0394` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8825` n `50` status `ready` deltaP `13.7006` edge `0.1939` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8572` n `50` status `ready` deltaP `13.4551` edge `0.2147` maxDD `-3.6376`
- `news_risk_high->equity_4h` score `2.4655` n `116` status `ready` deltaP `22.4033` edge `0.1257` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.9599` n `50` status `ready` deltaP `10.0139` edge `0.3707` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.6348` n `73` status `ready` deltaP `6.6852` edge `0.4804` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.262` n `73` status `ready` deltaP `12.3145` edge `0.2071` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.8707` n `116` status `ready` deltaP `12.6735` edge `0.2581` maxDD `-10.477`
- `market_context_high->index_24h` score `0.805` n `50` status `ready` deltaP `14.4444` edge `0.064` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.7097` n `116` status `ready` deltaP `4.3517` edge `0.0862` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T15:22:46.463068+00:00`
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

- `market_context_high->unknown_1h` score `359.4573` n `50` status `ready` deltaP `11.1737` edge `29.8852` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.471` n `50` status `ready` deltaP `11.128` edge `24.2984` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3085` n `73` status `ready` deltaP `39.795` edge `1.0313` maxDD `-1.005`
- `news_risk_high->equity_24h` score `9.401` n `73` status `ready` deltaP `33.7947` edge `0.6066` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.1491` n `50` status `ready` deltaP `32.3472` edge `0.6884` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.9831` n `50` status `ready` deltaP `16.5347` edge `0.8087` maxDD `-11.6271`
- `market_context_high->crypto_major_4h` score `6.656` n `50` status `ready` deltaP `16.1707` edge `0.5172` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.669` n `50` status `ready` deltaP `14.0549` edge `0.4243` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.49` n `116` status `ready` deltaP `19.917` edge `0.3758` maxDD `-6.4195`
- `market_context_high->crypto_major_1h` score `2.9029` n `50` status `ready` deltaP `13.7006` edge `0.1956` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8883` n `50` status `ready` deltaP `13.6048` edge `0.2163` maxDD `-3.6376`
- `market_context_high->fx_4h` score `2.8761` n `50` status `ready` deltaP `32.0793` edge `0.0393` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4643` n `116` status `ready` deltaP `22.4033` edge `0.1256` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.9372` n `50` status `ready` deltaP `10.0139` edge `0.3678` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.6117` n `73` status `ready` deltaP `6.5116` edge `0.4786` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2742` n `73` status `ready` deltaP `12.4881` edge `0.2075` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.8958` n `116` status `ready` deltaP `12.8259` edge `0.2603` maxDD `-10.477`
- `market_context_high->index_24h` score `0.7996` n `50` status `ready` deltaP `14.4444` edge `0.0633` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.7409` n `116` status `ready` deltaP `4.5014` edge `0.0878` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

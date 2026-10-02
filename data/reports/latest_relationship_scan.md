# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T16:37:28.378579+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4872`

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

- `market_context_high->unknown_1h` score `359.1069` n `50` status `ready` deltaP `11.1737` edge `29.856` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.8392` n `50` status `ready` deltaP `10.9756` edge `24.3301` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.4177` n `73` status `ready` deltaP `39.795` edge `1.0404` maxDD `-1.005`
- `news_risk_high->equity_24h` score `9.1746` n `73` status `ready` deltaP `33.2739` edge `0.5912` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `9.0923` n `50` status `ready` deltaP `16.5347` edge `0.8178` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0591` n `50` status `ready` deltaP `32.3472` edge `0.6809` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.8885` n `50` status `ready` deltaP `16.9329` edge `0.5315` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8414` n `50` status `ready` deltaP `14.6646` edge `0.4346` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.6624` n `116` status `ready` deltaP `20.5267` edge `0.3861` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `2.9423` n `50` status `ready` deltaP `13.9042` edge `0.2188` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9353` n `50` status `ready` deltaP `13.7006` edge `0.1983` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8335` n `50` status `ready` deltaP `31.622` edge `0.0388` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4135` n `116` status `ready` deltaP `22.0984` edge `0.1234` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.79` n `50` status `ready` deltaP `9.4931` edge `0.3524` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5532` n `73` status `ready` deltaP `6.5116` edge `0.4711` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.307` n `73` status `ready` deltaP `12.8354` edge `0.2094` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `1.047` n `116` status `ready` deltaP `13.5881` edge `0.2746` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.7949` n `116` status `ready` deltaP `4.8008` edge `0.0903` maxDD `-2.4854`
- `market_context_high->index_24h` score `0.7503` n `50` status `ready` deltaP `14.0972` edge `0.0593` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

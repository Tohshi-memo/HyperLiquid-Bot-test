# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T03:22:17.513373+00:00`
- Price records: `672`
- Market context records: `1590`
- Flow alert records: `6492`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.8243` n `182` status `ready` deltaP `29.5463` edge `1.0551` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.4201` n `182` status `ready` deltaP `27.171` edge `1.0555` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.6804` n `182` status `ready` deltaP `26.9135` edge `0.8238` maxDD `-8.0553`
- `market_context_high->equity_24h` score `4.8601` n `182` status `ready` deltaP `20.1446` edge `0.5034` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.188` n `182` status `ready` deltaP `21.9952` edge `0.311` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.0985` n `199` status `ready` deltaP `9.3593` edge `0.1386` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2456` n `199` status `ready` deltaP `13.1021` edge `0.2761` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0965` n `199` status `ready` deltaP `9.2796` edge `0.2214` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.0109` n `182` status `ready` deltaP `9.5848` edge `0.0401` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3269` n `199` status `ready` deltaP `0.8177` edge `0.055` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5779` n `199` status `ready` deltaP `0.6139` edge `0.0286` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5946` n `199` status `ready` deltaP `-1.3954` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6973` n `199` status `ready` deltaP `0.325` edge `0.0029` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7142` n `199` status `ready` deltaP `5.4472` edge `0.0057` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8208` n `199` status `ready` deltaP `-1.6948` edge `-0.0018` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8467` n `199` status `ready` deltaP `-0.1444` edge `0.0281` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0703` n `199` status `ready` deltaP `-1.5436` edge `0.03` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.2862` n `199` status `ready` deltaP `10.516` edge `0.0919` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3704` n `199` status `ready` deltaP `-10.2448` edge `-0.0145` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2557` n `199` status `ready` deltaP `-14.7001` edge `-0.1131` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

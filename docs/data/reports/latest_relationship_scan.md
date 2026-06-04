# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T07:07:27.469573+00:00`
- Price records: `672`
- Market context records: `2843`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->unknown_24h` score `2.5221` n `142` status `ready` deltaP `3.817` edge `0.2312` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.756` n `142` status `ready` deltaP `1.4867` edge `0.5281` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8682` n `142` status `ready` deltaP `6.6429` edge `0.1334` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.7864` n `142` status `ready` deltaP `11.7322` edge `0.2967` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3041` n `142` status `ready` deltaP `12.996` edge `0.0365` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.121` n `142` status `ready` deltaP `4.7799` edge `0.0513` maxDD `-3.1801`
- `market_context_high->index_24h` score `0.0643` n `142` status `ready` deltaP `5.0298` edge `0.0699` maxDD `-2.5127`
- `market_context_high->index_1h` score `-0.1038` n `142` status `ready` deltaP `3.8986` edge `0.0101` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5886` n `142` status `ready` deltaP `-1.1364` edge `0.0029` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.607` n `142` status `ready` deltaP `-0.2825` edge `-0.0006` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.684` n `142` status `ready` deltaP `0.4322` edge `-0.006` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7311` n `142` status `ready` deltaP `4.7968` edge `0.0503` maxDD `-10.747`
- `market_context_high->equity_24h` score `-0.7715` n `142` status `ready` deltaP `2.8315` edge `0.1172` maxDD `-12.6963`
- `market_context_high->crypto_major_1h` score `-0.9264` n `142` status `ready` deltaP `3.926` edge `0.042` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9483` n `142` status `ready` deltaP `-2.7494` edge `0.0226` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.086` n `142` status `ready` deltaP `1.8099` edge `0.0354` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1835` n `142` status `ready` deltaP `-4.0579` edge `0.0063` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3782` n `142` status `ready` deltaP `1.5329` edge `0.0051` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4227` n `142` status `ready` deltaP `-1.8852` edge `-0.0188` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.4911` n `142` status `ready` deltaP `13.7281` edge `0.2183` maxDD `-28.7261`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T09:37:18.513754+00:00`
- Price records: `672`
- Market context records: `2232`
- Flow alert records: `8319`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9179`

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

- `news_risk_high->crypto_alt_24h` score `25.6529` n `33` status `ready` deltaP `56.2658` edge `1.8215` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.4679` n `33` status `ready` deltaP `46.6225` edge `0.9388` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `12.9548` n `131` status `ready` deltaP `37.1695` edge `0.9254` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `12.4557` n `33` status `ready` deltaP `37.5947` edge `0.8188` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.7627` n `131` status `ready` deltaP `42.2129` edge `0.7518` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.3923` n `33` status `ready` deltaP `37.1686` edge `0.5575` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.3964` n `33` status `ready` deltaP `19.113` edge `0.8789` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.7282` n `131` status `ready` deltaP `21.4497` edge `0.3839` maxDD `-1.6306`
- `news_risk_high->commodity_4h` score `3.9528` n `43` status `ready` deltaP `33.2246` edge `0.3524` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.7292` n `131` status `ready` deltaP `23.7595` edge `0.2381` maxDD `-3.8587`
- `market_context_high->index_4h` score `3.4624` n `131` status `ready` deltaP `27.2645` edge `0.162` maxDD `-1.4186`
- `market_context_high->crypto_major_1h` score `3.1485` n `143` status `ready` deltaP `17.3831` edge `0.1942` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.9592` n `33` status `ready` deltaP `31.0606` edge `0.058` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.9267` n `143` status `ready` deltaP `16.2839` edge `0.2217` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.5095` n `130` status `ready` deltaP `23.9984` edge `0.4642` maxDD `-28.2051`
- `news_risk_high->commodity_24h` score `2.3456` n `33` status `ready` deltaP `-1.9413` edge `0.2901` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.1622` n `43` status `ready` deltaP `27.4319` edge `0.0157` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.7907` n `130` status `ready` deltaP `8.8649` edge `0.1987` maxDD `-3.686`
- `market_context_high->metal_4h` score `1.3534` n `131` status `ready` deltaP `17.4793` edge `0.135` maxDD `-4.7664`
- `news_risk_high->index_24h` score `1.3289` n `33` status `ready` deltaP `10.0537` edge `0.0856` maxDD `-1.3507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

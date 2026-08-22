# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T22:36:20.030532+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `market_context_high->unknown_1h` score `1.6305` n `141` status `ready` deltaP `5.849` edge `0.1196` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.876` n `141` status `ready` deltaP `19.0938` edge `-0.0105` maxDD `-0.5036`
- `market_context_high->fx_4h` score `0.1298` n `141` status `ready` deltaP `8.6533` edge `0.0092` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.043` n `141` status `ready` deltaP `6.4775` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1239` n `141` status `ready` deltaP `2.3251` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3258` n `141` status `ready` deltaP `4.8626` edge `0.0328` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.3715` n `141` status `ready` deltaP `7.1159` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.5391` n `141` status `ready` deltaP `0.276` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5933` n `141` status `ready` deltaP `2.4887` edge `0.0109` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.9541` n `141` status `ready` deltaP `-5.4575` edge `-0.0009` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.0662` n `125` status `ready` deltaP `0.2806` edge `0.0093` maxDD `-2.1622`
- `market_context_high->commodity_1h` score `-1.0926` n `141` status `ready` deltaP `-7.9033` edge `-0.0024` maxDD `-1.1328`
- `market_context_high->crypto_alt_1h` score `-1.4945` n `141` status `ready` deltaP `-1.8346` edge `-0.0299` maxDD `-7.9582`
- `market_context_high->equity_4h` score `-1.7199` n `141` status `ready` deltaP `-0.9709` edge `0.0676` maxDD `-16.1967`
- `market_context_high->crypto_alt_4h` score `-1.816` n `141` status `ready` deltaP `5.4727` edge `-0.041` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.0333` n `125` status `ready` deltaP `-5.8222` edge `0.0484` maxDD `-4.6558`
- `market_context_high->crypto_major_1h` score `-2.3173` n `141` status `ready` deltaP `-5.5623` edge `-0.1123` maxDD `-7.8171`
- `market_context_high->metal_24h` score `-5.3823` n `125` status `ready` deltaP `-23.4361` edge `-0.203` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.4245` n `141` status `ready` deltaP `1.6281` edge `-0.3299` maxDD `-5.6395`
- `market_context_high->index_24h` score `-6.9251` n `125` status `ready` deltaP `-7.8556` edge `-0.044` maxDD `-21.1244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T20:52:26.033429+00:00`
- Price records: `672`
- Market context records: `7917`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `16.2416` n `86` status `ready` deltaP `27.0228` edge `1.3075` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.1574` n `86` status `ready` deltaP `39.688` edge `0.4152` maxDD `0.0`
- `market_context_high->equity_4h` score `6.5947` n `95` status `ready` deltaP `25.7009` edge `0.4675` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `2.7581` n `86` status `ready` deltaP `23.9664` edge `0.2251` maxDD `-6.736`
- `market_context_high->index_4h` score `2.6598` n `95` status `ready` deltaP `27.5004` edge `0.0743` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5816` n `95` status `ready` deltaP `23.3505` edge `0.1217` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.5933` n `95` status `ready` deltaP `12.2602` edge `0.1328` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.4785` n `86` status `ready` deltaP `28.8557` edge `0.0396` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.4269` n `95` status `ready` deltaP `10.4285` edge `0.1611` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.1981` n `86` status `ready` deltaP `9.7384` edge `0.1557` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.1035` n `95` status `ready` deltaP `11.619` edge `0.1863` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.9977` n `95` status `ready` deltaP `12.1053` edge `0.0433` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.8655` n `95` status `ready` deltaP `13.9102` edge `0.0224` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.5348` n `95` status `ready` deltaP `7.89` edge `0.0298` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.3066` n `95` status `ready` deltaP `6.2338` edge `0.041` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1607` n `95` status `ready` deltaP `2.178` edge `0.0016` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.2693` n `95` status `ready` deltaP `5.1666` edge `0.0058` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.4745` n `95` status `ready` deltaP `-0.0711` edge `-0.0035` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.5792` n `95` status `ready` deltaP `2.0843` edge `0.0143` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.921` n `95` status `ready` deltaP `8.0492` edge `-0.1714` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

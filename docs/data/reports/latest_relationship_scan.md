# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T20:37:25.717339+00:00`
- Price records: `672`
- Market context records: `7916`
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
- `market_context_high->metal_24h` score `8.1586` n `86` status `ready` deltaP `39.688` edge `0.4153` maxDD `0.0`
- `market_context_high->equity_4h` score `6.5995` n `95` status `ready` deltaP `25.7009` edge `0.4679` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `2.7473` n `86` status `ready` deltaP `23.9664` edge `0.2242` maxDD `-6.736`
- `market_context_high->index_4h` score `2.661` n `95` status `ready` deltaP `27.5004` edge `0.0744` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.595` n `95` status `ready` deltaP `23.5029` edge `0.1218` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6065` n `95` status `ready` deltaP `12.4103` edge `0.1329` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.4761` n `86` status `ready` deltaP `28.8557` edge `0.0394` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.4233` n `95` status `ready` deltaP `10.4285` edge `0.1608` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2094` n `86` status `ready` deltaP `9.912` edge `0.156` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.1035` n `95` status `ready` deltaP `11.619` edge `0.1863` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.9785` n `95` status `ready` deltaP `11.9556` edge `0.0427` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.8775` n `95` status `ready` deltaP `14.0603` edge `0.0224` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.5467` n `95` status `ready` deltaP `8.0397` edge `0.0298` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2949` n `95` status `ready` deltaP `6.0841` edge `0.0405` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1607` n `95` status `ready` deltaP `2.178` edge `0.0016` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.2693` n `95` status `ready` deltaP `5.1666` edge `0.0058` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.4729` n `95` status `ready` deltaP `-0.0711` edge `-0.0033` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.5804` n `95` status `ready` deltaP `2.0843` edge `0.0142` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.9198` n `95` status `ready` deltaP `8.0492` edge `-0.1713` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

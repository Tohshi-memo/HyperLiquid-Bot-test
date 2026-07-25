# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T17:52:25.805863+00:00`
- Price records: `672`
- Market context records: `7903`
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

- `market_context_high->equity_24h` score `15.3299` n `97` status `ready` deltaP `29.5765` edge `1.2145` maxDD `-6.0681`
- `market_context_high->metal_24h` score `6.525` n `97` status `ready` deltaP `32.1339` edge `0.361` maxDD `-0.1846`
- `market_context_high->equity_4h` score `5.7413` n `103` status `ready` deltaP `20.6289` edge `0.4302` maxDD `-5.1426`
- `market_context_high->index_4h` score `1.9819` n `103` status `ready` deltaP `21.4469` edge `0.0665` maxDD `-0.8791`
- `market_context_high->commodity_24h` score `1.9526` n `97` status `ready` deltaP `21.2646` edge `0.1793` maxDD `-7.0012`
- `market_context_high->metal_4h` score `1.8336` n `103` status `ready` deltaP `16.3805` edge `0.11` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `1.6353` n `103` status `ready` deltaP `12.5533` edge `0.1643` maxDD `-3.9374`
- `market_context_high->equity_1h` score `1.4935` n `106` status `ready` deltaP `12.842` edge `0.1206` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.4446` n `103` status `ready` deltaP `14.3988` edge `0.1962` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.2554` n `97` status `ready` deltaP `33.3172` edge `0.0476` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.2202` n `106` status `ready` deltaP `14.0464` edge `0.0489` maxDD `-1.6021`
- `market_context_high->index_24h` score `1.1279` n `97` status `ready` deltaP `5.5824` edge `0.1363` maxDD `-1.3621`
- `market_context_high->index_1h` score `0.7146` n `106` status `ready` deltaP `12.4144` edge `0.0198` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.4042` n `106` status `ready` deltaP `5.4655` edge `0.0405` maxDD `-1.4603`
- `market_context_high->metal_1h` score `0.3683` n `106` status `ready` deltaP `6.3637` edge `0.0261` maxDD `-0.6936`
- `market_context_high->commodity_4h` score `-0.1807` n `103` status `ready` deltaP `5.9203` edge `0.0199` maxDD `-2.2874`
- `market_context_high->fx_1h` score `-0.1858` n `106` status `ready` deltaP `1.8018` edge `0.0009` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.2809` n `103` status `ready` deltaP `4.9122` edge `0.006` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.4445` n `106` status `ready` deltaP `2.5072` edge `0.0031` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-1.475` n `106` status `ready` deltaP `5.8553` edge `-0.1858` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T20:22:29.728081+00:00`
- Price records: `672`
- Market context records: `7915`
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

- `market_context_high->equity_24h` score `16.1559` n `87` status `ready` deltaP `27.3168` edge `1.2984` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.095` n `87` status `ready` deltaP `39.688` edge `0.41` maxDD `0.0`
- `market_context_high->equity_4h` score `6.4902` n `96` status `ready` deltaP `25.0095` edge `0.4634` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.6666` n `96` status `ready` deltaP `27.6758` edge `0.0737` maxDD `-0.8791`
- `market_context_high->commodity_24h` score `2.5885` n `87` status `ready` deltaP `23.0843` edge `0.2179` maxDD `-6.82`
- `market_context_high->metal_4h` score `2.5248` n `96` status `ready` deltaP `22.8659` edge `0.1202` maxDD `-0.979`
- `market_context_high->index_24h` score `1.8049` n `87` status `ready` deltaP `9.4708` edge `0.1543` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.5462` n `96` status `ready` deltaP `11.8806` edge `0.1314` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.5396` n `87` status `ready` deltaP `29.4839` edge `0.0405` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.4644` n `96` status `ready` deltaP `10.8232` edge `0.1616` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.1309` n `96` status `ready` deltaP `11.9918` edge `0.1861` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.916` n `96` status `ready` deltaP `11.3086` edge `0.0418` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.9061` n `96` status `ready` deltaP `14.4331` edge `0.0223` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.4946` n `96` status `ready` deltaP `7.4476` edge `0.0294` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.3101` n `96` status `ready` deltaP `6.4059` edge `0.0403` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.141` n `96` status `ready` deltaP `2.5432` edge `0.0017` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.2392` n `96` status `ready` deltaP `5.7149` edge `0.006` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.496` n `96` status `ready` deltaP `-0.4693` edge `-0.0036` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.5611` n `96` status `ready` deltaP `2.37` edge `0.0139` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.8916` n `96` status `ready` deltaP `8.4768` edge `-0.1718` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

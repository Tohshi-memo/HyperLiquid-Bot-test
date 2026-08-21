# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T07:22:13.681998+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.2957` n `105` status `ready` deltaP `8.4203` edge `0.05` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.2951` n `105` status `ready` deltaP `10.1084` edge `0.0059` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.1039` n `105` status `ready` deltaP `4.7402` edge `0.14` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0478` n `105` status `ready` deltaP `7.333` edge `0.0075` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->commodity_24h` score `-0.2359` n `100` status `ready` deltaP `5.5903` edge `0.1264` maxDD `-4.666`
- `market_context_high->metal_4h` score `-0.2445` n `105` status `ready` deltaP `6.5302` edge `-0.0173` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3019` n `105` status `ready` deltaP `5.4283` edge `0.0175` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3156` n `105` status `ready` deltaP `2.1899` edge `-0.0022` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.3954` n `105` status `ready` deltaP `7.7802` edge `-0.0621` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6512` n `105` status `ready` deltaP `-1.4329` edge `0.0111` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.744` n `105` status `ready` deltaP `-5.7285` edge `-0.0006` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.8423` n `105` status `ready` deltaP `-2.043` edge `-0.0142` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9703` n `105` status `ready` deltaP `-1.1577` edge `-0.0322` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.7227` n `105` status `ready` deltaP `0.1655` edge `-0.101` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.0816` n `105` status `ready` deltaP `2.4143` edge `-0.1708` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3237` n `100` status `ready` deltaP `-15.625` edge `-0.0145` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8295` n `100` status `ready` deltaP `-1.0417` edge `-0.0469` maxDD `-18.6362`
- `market_context_high->metal_24h` score `-4.6551` n `100` status `ready` deltaP `-19.0069` edge `-0.1393` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.7387` n `100` status `ready` deltaP `11.5556` edge `-0.4213` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

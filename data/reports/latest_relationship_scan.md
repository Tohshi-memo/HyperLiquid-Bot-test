# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T09:49:14.619143+00:00`
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

- `market_context_high->equity_1h` score `0.4277` n `108` status `ready` deltaP `9.4256` edge `0.0543` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.304` n `108` status `ready` deltaP `10.2129` edge `0.0061` maxDD `-0.5746`
- `market_context_high->fx_4h` score `0.0803` n `105` status `ready` deltaP `7.9428` edge `0.0076` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0739` n `105` status `ready` deltaP `4.7402` edge `0.1375` maxDD `-8.3685`
- `market_context_high->fx_1h` score `-0.1376` n `108` status `ready` deltaP `2.0016` edge `0.0049` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2585` n `105` status `ready` deltaP `6.5302` edge `-0.0191` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.2925` n `105` status `ready` deltaP `5.5807` edge `0.0177` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3562` n `108` status `ready` deltaP `1.9073` edge `-0.0037` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.3853` n `103` status `ready` deltaP `4.728` edge `0.1197` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5279` n `108` status `ready` deltaP `7.8344` edge `-0.0735` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.7494` n `108` status `ready` deltaP `-5.7718` edge `-0.001` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7624` n `105` status `ready` deltaP `-2.9573` edge `0.007` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.1301` n `108` status `ready` deltaP `-3.9033` edge `-0.0387` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.1497` n `108` status `ready` deltaP `-2.1623` edge `-0.0485` maxDD `-2.7581`
- `market_context_high->fx_24h` score `-3.2178` n `103` status `ready` deltaP `-14.6171` edge `-0.0116` maxDD `-2.0613`
- `market_context_high->crypto_alt_4h` score `-3.328` n `105` status `ready` deltaP `-1.2064` edge `-0.1423` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.6368` n `105` status `ready` deltaP `0.8899` edge `-0.2069` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0468` n `103` status `ready` deltaP `-3.5396` edge `-0.045` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.4888` n `103` status `ready` deltaP `-17.6088` edge `-0.1273` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.5651` n `103` status `ready` deltaP `10.5465` edge `-0.4001` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

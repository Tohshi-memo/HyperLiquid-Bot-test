# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T18:35:03.906982+00:00`
- Price records: `672`
- Market context records: `7906`
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

- `market_context_high->equity_24h` score `15.6094` n `94` status `ready` deltaP `29.1999` edge `1.2403` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.1043` n `94` status `ready` deltaP `35.0622` edge `0.3756` maxDD `-0.0528`
- `market_context_high->equity_4h` score `5.8829` n `100` status `ready` deltaP `20.7187` edge `0.4414` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.2545` n `100` status `ready` deltaP `23.2599` edge `0.0688` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.0546` n `100` status `ready` deltaP `17.9329` edge `0.1139` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.0163` n `94` status `ready` deltaP `20.9959` edge `0.1864` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.507` n `100` status `ready` deltaP `11.4756` edge `0.1608` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.4408` n `94` status `ready` deltaP `6.7487` edge `0.1421` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.4386` n `103` status `ready` deltaP `11.8254` edge `0.1228` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.249` n `100` status `ready` deltaP `13.4085` edge `0.1865` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.1896` n `94` status `ready` deltaP `32.2917` edge `0.046` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.0813` n `103` status `ready` deltaP `13.0298` edge `0.0441` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.6971` n `103` status `ready` deltaP `12.1359` edge `0.0202` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.4037` n `103` status `ready` deltaP `6.6871` edge `0.0269` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2435` n `103` status `ready` deltaP `4.1466` edge `0.0359` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `-0.1856` n `100` status `ready` deltaP `5.1193` edge `0.0165` maxDD `-2.2874`
- `market_context_high->fx_1h` score `-0.1946` n `103` status `ready` deltaP `1.6167` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.2044` n `100` status `ready` deltaP `6.3394` edge `0.0063` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5442` n `103` status `ready` deltaP `1.516` edge `0.0014` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-2.1575` n `103` status `ready` deltaP `6.6828` edge `-0.182` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T19:07:29.806009+00:00`
- Price records: `672`
- Market context records: `5694`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8856`

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

- `market_context_high->crypto_major_4h` score `2.1323` n `257` status `ready` deltaP `13.2836` edge `0.2399` maxDD `-7.728`
- `market_context_high->equity_24h` score `1.1618` n `207` status `ready` deltaP `16.1761` edge `0.549` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `1.0924` n `257` status `ready` deltaP `10.3712` edge `0.1828` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2278` n `257` status `ready` deltaP `6.5323` edge `0.1393` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `-0.1038` n `269` status `ready` deltaP `4.7865` edge `0.0467` maxDD `-3.9811`
- `market_context_high->crypto_alt_1h` score `-0.1914` n `269` status `ready` deltaP `3.1348` edge `0.045` maxDD `-3.8812`
- `market_context_high->fx_1h` score `-0.252` n `269` status `ready` deltaP `2.117` edge `0.0012` maxDD `-0.4764`
- `market_context_high->metal_1h` score `-0.4626` n `269` status `ready` deltaP `1.2911` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5702` n `269` status `ready` deltaP `3.6413` edge `0.0289` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6055` n `269` status `ready` deltaP `0.6923` edge `0.0046` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.6485` n `269` status `ready` deltaP `-0.4029` edge `-0.0039` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-0.9025` n `207` status `ready` deltaP `13.5115` edge `0.0464` maxDD `-3.1741`
- `market_context_high->fx_4h` score `-1.1384` n `257` status `ready` deltaP `4.5589` edge `0.0071` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2969` n `257` status `ready` deltaP `-0.8767` edge `0.0076` maxDD `-3.1083`
- `market_context_high->metal_4h` score `-2.7735` n `257` status `ready` deltaP `-9.8421` edge `-0.0524` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.7791` n `207` status `ready` deltaP `3.6685` edge `0.0293` maxDD `-17.8038`
- `market_context_high->commodity_4h` score `-3.9091` n `257` status `ready` deltaP `-3.7202` edge `-0.0334` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-3.9935` n `207` status `ready` deltaP `5.8499` edge `0.0739` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.138` n `207` status `ready` deltaP `-9.8355` edge `-0.2459` maxDD `-32.5493`
- `market_context_high->commodity_24h` score `-12.2202` n `207` status `ready` deltaP `-11.7679` edge `-0.079` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

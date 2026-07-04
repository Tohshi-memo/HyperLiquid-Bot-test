# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T19:22:25.198846+00:00`
- Price records: `672`
- Market context records: `5695`
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

- `market_context_high->crypto_major_4h` score `2.3058` n `257` status `ready` deltaP `13.5202` edge `0.2421` maxDD `-6.8734`
- `market_context_high->equity_24h` score `1.1641` n `207` status `ready` deltaP `16.1761` edge `0.5493` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `1.1378` n `257` status `ready` deltaP `10.6079` edge `0.185` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2491` n `257` status `ready` deltaP `6.769` edge `0.1395` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `-0.0978` n `269` status `ready` deltaP `4.7865` edge `0.0472` maxDD `-3.9811`
- `market_context_high->crypto_alt_1h` score `-0.1902` n `269` status `ready` deltaP `3.1348` edge `0.0451` maxDD `-3.8812`
- `market_context_high->fx_1h` score `-0.252` n `269` status `ready` deltaP `2.117` edge `0.0012` maxDD `-0.4764`
- `market_context_high->metal_1h` score `-0.4511` n `269` status `ready` deltaP `1.5132` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5489` n `269` status `ready` deltaP `3.8633` edge `0.0292` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6178` n `269` status `ready` deltaP `0.4703` edge `0.0045` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.6623` n `269` status `ready` deltaP `-0.625` edge `-0.0042` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-0.9023` n `207` status `ready` deltaP `13.5115` edge `0.0466` maxDD `-3.1889`
- `market_context_high->fx_4h` score `-1.1507` n `257` status `ready` deltaP `4.3223` edge `0.0071` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2985` n `257` status `ready` deltaP `-0.8767` edge `0.0077` maxDD `-3.1328`
- `market_context_high->metal_4h` score `-2.7597` n `257` status `ready` deltaP `-9.6054` edge `-0.0522` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8108` n `207` status `ready` deltaP `3.359` edge `0.0281` maxDD `-17.8679`
- `market_context_high->crypto_major_24h` score `-3.874` n `207` status `ready` deltaP `6.1594` edge `0.0818` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-3.9328` n `257` status `ready` deltaP `-3.9569` edge `-0.0338` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.1186` n `207` status `ready` deltaP `-9.526` edge `-0.2455` maxDD `-32.547`
- `market_context_high->commodity_24h` score `-12.2593` n `207` status `ready` deltaP `-12.0773` edge `-0.0802` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

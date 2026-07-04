# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T19:52:29.255829+00:00`
- Price records: `672`
- Market context records: `5697`
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

- `market_context_high->crypto_major_4h` score `2.3557` n `257` status `ready` deltaP `13.5202` edge `0.2433` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.168` n `207` status `ready` deltaP `16.1761` edge `0.5498` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `1.1615` n `257` status `ready` deltaP `10.8445` edge `0.1854` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2681` n `257` status `ready` deltaP `7.0057` edge `0.1395` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `-0.155` n `269` status `ready` deltaP `4.3424` edge `0.0454` maxDD `-3.9811`
- `market_context_high->crypto_alt_1h` score `-0.2533` n `269` status `ready` deltaP `2.6907` edge `0.0428` maxDD `-3.8812`
- `market_context_high->fx_1h` score `-0.2536` n `269` status `ready` deltaP `2.117` edge `0.001` maxDD `-0.4764`
- `market_context_high->metal_1h` score `-0.4503` n `269` status `ready` deltaP `1.5132` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5501` n `269` status `ready` deltaP `3.8633` edge `0.0291` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6178` n `269` status `ready` deltaP `0.4703` edge `0.0045` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.914` n `207` status `ready` deltaP `13.5115` edge `0.0465` maxDD `-3.3006`
- `market_context_high->commodity_1h` score `-1.1081` n `269` status `ready` deltaP `-1.0691` edge `-0.0045` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1645` n `257` status `ready` deltaP `4.0856` edge `0.0069` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.3396` n `257` status `ready` deltaP `-1.35` edge `0.0059` maxDD `-3.1577`
- `market_context_high->metal_4h` score `-2.7597` n `257` status `ready` deltaP `-9.6054` edge `-0.0522` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8727` n `207` status `ready` deltaP `2.74` edge `0.0256` maxDD `-17.9732`
- `market_context_high->crypto_major_24h` score `-3.6673` n `207` status `ready` deltaP `6.7784` edge `0.0949` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-3.9827` n `257` status `ready` deltaP `-4.4302` edge `-0.0348` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0664` n `207` status `ready` deltaP `-9.2165` edge `-0.2451` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.3388` n `207` status `ready` deltaP `-12.6962` edge `-0.0827` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

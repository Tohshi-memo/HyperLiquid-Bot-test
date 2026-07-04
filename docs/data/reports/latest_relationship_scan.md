# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T19:37:29.481863+00:00`
- Price records: `672`
- Market context records: `5696`
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

- `market_context_high->crypto_major_4h` score `2.3449` n `257` status `ready` deltaP `13.5202` edge `0.2424` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.1649` n `207` status `ready` deltaP `16.1761` edge `0.5494` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `1.139` n `257` status `ready` deltaP `10.6079` edge `0.1851` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2693` n `257` status `ready` deltaP `7.0057` edge `0.1396` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `-0.1288` n `269` status `ready` deltaP `4.5645` edge `0.0461` maxDD `-3.9811`
- `market_context_high->crypto_alt_1h` score `-0.226` n `269` status `ready` deltaP `2.9128` edge `0.0436` maxDD `-3.8812`
- `market_context_high->fx_1h` score `-0.2528` n `269` status `ready` deltaP `2.117` edge `0.0011` maxDD `-0.4764`
- `market_context_high->metal_1h` score `-0.4503` n `269` status `ready` deltaP `1.5132` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5489` n `269` status `ready` deltaP `3.8633` edge `0.0292` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6178` n `269` status `ready` deltaP `0.4703` edge `0.0045` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.9076` n `207` status `ready` deltaP `13.5115` edge `0.0466` maxDD `-3.2427`
- `market_context_high->commodity_1h` score `-1.0379` n `269` status `ready` deltaP `-0.847` edge `-0.0043` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1637` n `257` status `ready` deltaP `4.0856` edge `0.007` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.3196` n `257` status `ready` deltaP `-1.1133` edge `0.0068` maxDD `-3.1517`
- `market_context_high->metal_4h` score `-2.7597` n `257` status `ready` deltaP `-9.6054` edge `-0.0522` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8418` n `207` status `ready` deltaP `3.0495` edge `0.0269` maxDD `-17.9247`
- `market_context_high->crypto_major_24h` score `-3.7796` n `207` status `ready` deltaP `6.4689` edge `0.0876` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-3.9577` n `257` status `ready` deltaP `-4.1935` edge `-0.0343` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.117` n `207` status `ready` deltaP `-9.526` edge `-0.2453` maxDD `-32.547`
- `market_context_high->commodity_24h` score `-12.2985` n `207` status `ready` deltaP `-12.3867` edge `-0.0814` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

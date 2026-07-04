# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T17:37:23.203620+00:00`
- Price records: `672`
- Market context records: `5686`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8784`

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

- `market_context_high->equity_24h` score `1.7621` n `207` status `ready` deltaP `16.1761` edge `0.5469` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9685` n `257` status `ready` deltaP `11.8635` edge `0.2161` maxDD `-12.8252`
- `market_context_high->crypto_alt_4h` score `0.5203` n `257` status `ready` deltaP `8.9512` edge `0.1588` maxDD `-8.6763`
- `market_context_high->equity_4h` score `0.159` n `257` status `ready` deltaP `5.8224` edge `0.1383` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2636` n `269` status `ready` deltaP `1.8949` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.4256` n `269` status `ready` deltaP `2.6907` edge `0.0395` maxDD `-4.7655`
- `market_context_high->metal_1h` score `-0.4996` n `269` status `ready` deltaP `0.625` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5928` n `269` status `ready` deltaP `3.4192` edge `0.0285` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.6388` n `269` status `ready` deltaP `4.1204` edge `0.0395` maxDD `-6.6163`
- `market_context_high->index_1h` score `-0.6424` n `269` status `ready` deltaP `0.0262` edge `0.0043` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.9597` n `269` status `ready` deltaP `0.0412` edge `-0.0037` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1384` n `257` status `ready` deltaP `4.5589` edge `0.0071` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2918` n `257` status `ready` deltaP `-0.8767` edge `0.0074` maxDD `-3.04`
- `market_context_high->fx_24h` score `-1.4045` n `207` status `ready` deltaP `13.202` edge `0.0462` maxDD `-3.1001`
- `market_context_high->index_24h` score `-2.5756` n `207` status `ready` deltaP `5.5254` edge `0.0372` maxDD `-17.3392`
- `market_context_high->metal_4h` score `-2.8536` n `257` status `ready` deltaP `-11.2621` edge `-0.0532` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.8105` n `257` status `ready` deltaP `-2.7736` edge `-0.0315` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.8609` n `207` status `ready` deltaP `3.9931` edge `0.014` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2607` n `207` status `ready` deltaP `-11.6923` edge `-0.2471` maxDD `-32.7213`
- `market_context_high->commodity_24h` score `-11.9984` n `207` status `ready` deltaP `-9.9109` edge `-0.0729` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T15:52:31.492292+00:00`
- Price records: `672`
- Market context records: `5158`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5612`

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

- `market_context_high->unknown_24h` score `30.2265` n `63` status `ready` deltaP `34.1022` edge `2.3105` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.2277` n `135` status `ready` deltaP `19.9796` edge `0.488` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.8571` n `135` status `ready` deltaP `15.1614` edge `0.4636` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `4.7771` n `63` status `ready` deltaP `19.7173` edge `0.8197` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.533` n `63` status `ready` deltaP `17.7331` edge `0.8291` maxDD `-22.6266`
- `market_context_high->unknown_1h` score `4.3791` n `146` status `ready` deltaP `9.911` edge `0.363` maxDD `-2.7986`
- `market_context_high->crypto_major_4h` score `3.9788` n `135` status `ready` deltaP `13.8325` edge `0.4686` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0285` n `63` status `ready` deltaP `20.2381` edge `0.1574` maxDD `-5.1955`
- `market_context_high->metal_24h` score `0.952` n `63` status `ready` deltaP `0.9424` edge `0.2466` maxDD `-5.4668`
- `market_context_high->crypto_major_1h` score `0.8061` n `146` status `ready` deltaP `7.8931` edge `0.1391` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.7701` n `146` status `ready` deltaP `5.4343` edge `0.1241` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.5451` n `135` status `ready` deltaP `8.5185` edge `0.1525` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.1294` n `146` status `ready` deltaP `6.9765` edge `0.0608` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.0883` n `146` status `ready` deltaP `4.8765` edge `0.0146` maxDD `-2.0075`
- `market_context_high->index_1h` score `-0.1167` n `146` status `ready` deltaP `4.2367` edge `0.0124` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.1935` n `146` status `ready` deltaP `2.9756` edge `0.0006` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4439` n `135` status `ready` deltaP `3.9194` edge `0.0287` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.465` n `63` status `ready` deltaP `6.5229` edge `0.0073` maxDD `-0.8294`
- `market_context_high->fx_4h` score `-0.5377` n `135` status `ready` deltaP `4.1193` edge `0.007` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5895` n `146` status `ready` deltaP `0.7485` edge `0.0003` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

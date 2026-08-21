# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T12:22:36.323889+00:00`
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

- `market_context_high->index_1h` score `0.4769` n `118` status `ready` deltaP `12.212` edge `0.0071` maxDD `-0.5685`
- `market_context_high->equity_1h` score `0.4023` n `118` status `ready` deltaP `9.1673` edge `0.0539` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.1744` n `106` status `ready` deltaP `9.5577` edge `0.0089` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0584` n `118` status `ready` deltaP `3.5395` edge `0.0048` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.1113` n `106` status `ready` deltaP `3.8801` edge `0.1278` maxDD `-8.3685`
- `market_context_high->metal_4h` score `-0.2793` n `106` status `ready` deltaP `6.0716` edge `-0.0187` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3176` n `106` status `ready` deltaP `5.2318` edge `0.0168` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3756` n `118` status `ready` deltaP `1.7431` edge `-0.0033` maxDD `-0.503`
- `market_context_high->commodity_24h` score `-0.442` n `105` status `ready` deltaP `4.5883` edge `0.1159` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.4542` n `118` status `ready` deltaP `10.2101` edge `-0.0832` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.6907` n `118` status `ready` deltaP `-4.8386` edge `0.0003` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7459` n `106` status `ready` deltaP `-2.5799` edge `0.0066` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.2047` n `118` status `ready` deltaP `-1.6543` edge `-0.0092` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.5902` n `118` status `ready` deltaP `-4.392` edge `-0.0721` maxDD `-4.1996`
- `market_context_high->fx_24h` score `-3.1061` n `105` status `ready` deltaP `-13.3433` edge `-0.0089` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.6211` n `106` status `ready` deltaP `-1.6452` edge `-0.1638` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-4.1154` n `106` status `ready` deltaP `-0.7881` edge `-0.2356` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.1187` n `105` status `ready` deltaP `-4.7272` edge `-0.0463` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.4255` n `105` status `ready` deltaP `-16.7212` edge `-0.1251` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.6794` n `105` status `ready` deltaP `9.1617` edge `-0.4004` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

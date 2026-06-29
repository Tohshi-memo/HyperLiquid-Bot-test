# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T21:07:34.776536+00:00`
- Price records: `672`
- Market context records: `5182`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `22.9426` n `79` status `ready` deltaP `32.7839` edge `1.7123` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `11.6774` n `79` status `ready` deltaP `25.0176` edge `1.1725` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.5938` n `79` status `ready` deltaP `26.0373` edge `0.9646` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.8014` n `150` status `ready` deltaP `19.5406` edge `0.4554` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.8051` n `150` status `ready` deltaP `14.496` edge `0.4637` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.5392` n `150` status `ready` deltaP `13.9817` edge `0.5143` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6371` n `155` status `ready` deltaP `9.5866` edge `0.22` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.2782` n `150` status `ready` deltaP `8.7418` edge `0.2121` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5565` n `155` status `ready` deltaP `4.3539` edge `0.1135` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5465` n `155` status `ready` deltaP `6.553` edge `0.1264` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.3364` n `155` status `ready` deltaP `8.3639` edge `0.0688` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.0442` n `79` status `ready` deltaP `10.5925` edge `0.0226` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0358` n `155` status `ready` deltaP `5.933` edge `0.0138` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0358` n `155` status `ready` deltaP `5.4587` edge `0.0182` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2658` n `155` status `ready` deltaP `1.6593` edge `0.0001` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4447` n `150` status `ready` deltaP `5.7723` edge `0.0362` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5581` n `150` status `ready` deltaP `3.7704` edge `0.0067` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6047` n `155` status `ready` deltaP `0.5756` edge `-0.0005` maxDD `-2.4692`
- `market_context_high->index_24h` score `-1.12` n `79` status `ready` deltaP `5.3709` edge `-0.0159` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2588` n `150` status `ready` deltaP `0.3841` edge `0.0364` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

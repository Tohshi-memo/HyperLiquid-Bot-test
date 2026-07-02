# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T11:52:34.842097+00:00`
- Price records: `672`
- Market context records: `5451`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->crypto_major_24h` score `3.3885` n `189` status `ready` deltaP `17.295` edge `0.6211` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.9262` n `197` status `ready` deltaP `15.435` edge `0.3702` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.4577` n `197` status `ready` deltaP `12.5356` edge `0.2851` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.2257` n `197` status `ready` deltaP `10.5083` edge `0.2795` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.7858` n `189` status `ready` deltaP `10.1191` edge `0.5428` maxDD `-28.9154`
- `market_context_high->equity_1h` score `0.5075` n `199` status `ready` deltaP `8.1628` edge `0.0844` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2054` n `189` status `ready` deltaP `10.9127` edge `0.0339` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.157` n `199` status `ready` deltaP `6.7839` edge `0.0172` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.2653` n `199` status `ready` deltaP `3.9614` edge `0.019` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.3297` n `199` status `ready` deltaP `0.9569` edge `0.0623` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4423` n `199` status `ready` deltaP `2.1439` edge `0.0734` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5788` n `199` status `ready` deltaP `0.1121` edge `-0.0001` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8287` n `197` status `ready` deltaP `7.4656` edge `0.0421` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1011` n `197` status `ready` deltaP `1.0585` edge `0.0037` maxDD `-1.5345`
- `market_context_high->index_24h` score `-1.2821` n `189` status `ready` deltaP `14.6412` edge `0.0809` maxDD `-14.7639`
- `market_context_high->commodity_1h` score `-1.3828` n `199` status `ready` deltaP `-2.2718` edge `-0.0053` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6112` n `197` status `ready` deltaP `-7.9671` edge `-0.0292` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3168` n `197` status `ready` deltaP `-6.5386` edge `-0.0447` maxDD `-14.3822`
- `market_context_high->metal_24h` score `-7.3033` n `189` status `ready` deltaP `-4.5387` edge `-0.1683` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.3446` n `189` status `ready` deltaP `8.259` edge `0.2026` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

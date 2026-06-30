# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T04:22:23.905188+00:00`
- Price records: `672`
- Market context records: `5214`
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

- `market_context_high->unknown_24h` score `16.8597` n `108` status `ready` deltaP `33.6227` edge `1.1998` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.2392` n `108` status `ready` deltaP `31.5393` edge `1.3425` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.2685` n `108` status `ready` deltaP `27.0254` edge `0.9309` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `4.6343` n `155` status `ready` deltaP `18.8119` edge `0.363` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.4111` n `155` status `ready` deltaP `13.8464` edge `0.4352` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.305` n `155` status `ready` deltaP `14.0696` edge `0.4942` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.3276` n `155` status `ready` deltaP `8.9878` edge `0.1982` maxDD `-2.7986`
- `market_context_high->crypto_alt_1h` score `0.6404` n `155` status `ready` deltaP `4.9527` edge `0.1165` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.598` n `155` status `ready` deltaP `6.7027` edge `0.1297` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.5808` n `108` status `ready` deltaP `13.7153` edge `0.0465` maxDD `-0.8294`
- `market_context_high->equity_4h` score `0.3206` n `155` status `ready` deltaP `7.0928` edge `0.1433` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.1263` n `155` status `ready` deltaP `5.2202` edge `0.0512` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.134` n `155` status `ready` deltaP `3.9617` edge `0.0156` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.2122` n `155` status `ready` deltaP `3.3881` edge `0.0101` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2604` n `155` status `ready` deltaP `1.809` edge `-0.0002` maxDD `-0.6194`
- `market_context_high->index_24h` score `-0.5222` n `108` status `ready` deltaP `13.2523` edge `0.0082` maxDD `-7.413`
- `market_context_high->fx_4h` score `-0.6097` n `155` status `ready` deltaP `3.034` edge `0.005` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6141` n `155` status `ready` deltaP `0.4259` edge `-0.0007` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.736` n `155` status `ready` deltaP `4.3814` edge `0.0212` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-1.3597` n `155` status `ready` deltaP `-0.1023` edge `0.0267` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

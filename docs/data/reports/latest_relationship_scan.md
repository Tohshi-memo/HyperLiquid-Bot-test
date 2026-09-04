# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T16:07:24.985405+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10784`

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

- `risk_on_high->unknown_4h` score `20.3402` n `133` status `ready` deltaP `7.6265` edge `1.706` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.3402` n `133` status `ready` deltaP `7.6265` edge `1.706` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4633` n `133` status `ready` deltaP `-1.5027` edge `1.023` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4633` n `133` status `ready` deltaP `-1.5027` edge `1.023` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.2878` n `212` status `ready` deltaP `-0.8785` edge `0.8429` maxDD `-2.0446`
- `market_context_high->unknown_4h` score `9.1468` n `209` status `ready` deltaP `9.1303` edge `0.7709` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `2.6223` n `54` status `ready` deltaP `19.618` edge `0.1147` maxDD `-0.8236`
- `news_risk_high->commodity_4h` score `1.5414` n `54` status `ready` deltaP `12.2911` edge `0.0666` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.2175` n `54` status `ready` deltaP `9.6065` edge `0.0547` maxDD `-0.0495`
- `news_risk_high->equity_1h` score `0.565` n `54` status `ready` deltaP `9.032` edge `0.0513` maxDD `-0.7924`
- `news_risk_high->index_1h` score `0.5117` n `54` status `ready` deltaP `10.7175` edge `0.0079` maxDD `-0.1`
- `news_risk_high->metal_4h` score `0.1149` n `54` status `ready` deltaP `6.2331` edge `0.0215` maxDD `-1.1994`
- `risk_on_high->metal_1h` score `0.0937` n `133` status `ready` deltaP `12.2631` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0937` n `133` status `ready` deltaP `12.2631` edge `0.0015` maxDD `-1.699`
- `news_risk_high->metal_1h` score `-0.0398` n `54` status `ready` deltaP `3.9089` edge `0.0038` maxDD `-0.7973`
- `news_risk_high->commodity_1h` score `-0.0566` n `54` status `ready` deltaP `6.0768` edge `-0.0006` maxDD `-0.9036`
- `news_risk_high->equity_24h` score `-0.0667` n `54` status `ready` deltaP `4.2245` edge `0.0766` maxDD `-5.0655`
- `news_risk_high->fx_4h` score `-0.0808` n `54` status `ready` deltaP `6.2048` edge `-0.0008` maxDD `-1.1172`
- `market_context_high->equity_24h` score `-0.0849` n `167` status `ready` deltaP `12.4636` edge `0.3444` maxDD `-20.7654`
- `risk_on_high->index_1h` score `-0.1956` n `133` status `ready` deltaP `3.3936` edge `-0.0032` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

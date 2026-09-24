# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T12:07:31.446337+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `66.135` n `47` status `ready` deltaP `10.2657` edge `5.4499` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.3482` n `46` status `ready` deltaP `30.548` edge `3.4243` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `29.1281` n `46` status `ready` deltaP `25.5208` edge `2.2572` maxDD `0.0`
- `market_context_high->equity_24h` score `25.0132` n `46` status `ready` deltaP `27.9439` edge `1.9082` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `9.607` n `103` status `ready` deltaP `2.857` edge `1.6858` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.2148` n `46` status `ready` deltaP `36.9716` edge `0.4468` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `6.866` n `103` status `ready` deltaP `0.2781` edge `1.2716` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.5716` n `46` status `ready` deltaP `30.9481` edge `0.1147` maxDD `-0.2042`
- `market_context_high->index_4h` score `3.076` n `47` status `ready` deltaP `34.941` edge `0.0388` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6587` n `47` status `ready` deltaP `17.7542` edge `0.145` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.4235` n `116` status `ready` deltaP `13.1685` edge `0.1632` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.0017` n `116` status `ready` deltaP `14.4023` edge `0.1143` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6693` n `114` status `ready` deltaP `24.5561` edge `0.039` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.3304` n `103` status `ready` deltaP `17.4976` edge `0.1121` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.3188` n `103` status `ready` deltaP `30.3584` edge `0.1298` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.029` n `47` status `ready` deltaP `15.3586` edge `0.0112` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.9884` n `103` status `ready` deltaP `22.8223` edge `0.1194` maxDD `-7.2536`
- `market_context_high->equity_1h` score `0.9427` n `47` status `ready` deltaP `11.167` edge `0.0444` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.8136` n `114` status `ready` deltaP `12.9386` edge `0.1947` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.7803` n `116` status `ready` deltaP `16.2244` edge `0.0162` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

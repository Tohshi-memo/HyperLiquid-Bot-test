# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T10:07:30.412069+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `47.2582` n `46` status `ready` deltaP `7.3171` edge `3.8894` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `32.5805` n `46` status `ready` deltaP `18.7425` edge `2.6057` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.4444` n `46` status `ready` deltaP `17.5347` edge `1.3368` maxDD `0.0`
- `market_context_high->equity_24h` score `16.7297` n `46` status `ready` deltaP `14.055` edge `1.3105` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5968` n `46` status `ready` deltaP `20.1314` edge `0.3409` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.8634` n `101` status `ready` deltaP `-6.6127` edge `1.1352` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.0225` n `101` status `ready` deltaP `36.9121` edge `0.272` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4995` n `101` status `ready` deltaP `12.3641` edge `0.2468` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.221` n `101` status `ready` deltaP `13.8362` edge `0.1394` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1911` n `46` status `ready` deltaP `25.2982` edge `0.0273` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `2.1208` n `101` status `ready` deltaP `16.0227` edge `0.1957` maxDD `-8.0625`
- `market_context_high->equity_4h` score `1.5551` n `46` status `ready` deltaP `9.9682` edge `0.0938` maxDD `-0.4529`
- `news_risk_high->crypto_major_1h` score `1.5448` n `101` status `ready` deltaP `15.3332` edge `0.0788` maxDD `-2.8494`
- `market_context_high->equity_1h` score `0.9732` n `46` status `ready` deltaP `7.6608` edge `0.0543` maxDD `-0.2751`
- `news_risk_high->crypto_alt_24h` score `0.9634` n `101` status `ready` deltaP `-6.2277` edge `0.6099` maxDD `-32.7147`
- `market_context_high->crypto_alt_4h` score `0.9439` n `46` status `ready` deltaP `8.0593` edge `0.0844` maxDD `-2.7574`
- `news_risk_high->fx_4h` score `0.9043` n `101` status `ready` deltaP `15.6529` edge `0.0346` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6854` n `46` status `ready` deltaP `10.6548` edge `0.0114` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5694` n `101` status `ready` deltaP `14.1489` edge `0.0133` maxDD `-0.8144`
- `market_context_high->metal_24h` score `0.5632` n `46` status `ready` deltaP `19.1426` edge `-0.0573` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

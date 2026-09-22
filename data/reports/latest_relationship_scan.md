# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T09:52:33.607130+00:00`
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

- `market_context_high->unknown_4h` score `47.2858` n `46` status `ready` deltaP `7.3171` edge `3.8917` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `32.6988` n `46` status `ready` deltaP `18.9161` edge `2.6144` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.5411` n `46` status `ready` deltaP `17.7083` edge `1.3437` maxDD `0.0`
- `market_context_high->equity_24h` score `16.7688` n `46` status `ready` deltaP `14.2286` edge `1.3126` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.6004` n `46` status `ready` deltaP `20.1314` edge `0.3412` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9817` n `101` status `ready` deltaP `-6.4391` edge `1.1439` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.0017` n `101` status `ready` deltaP `36.7385` edge `0.2705` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.5225` n `101` status `ready` deltaP `12.5166` edge `0.2477` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2054` n `101` status `ready` deltaP `13.6865` edge `0.1391` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1923` n `46` status `ready` deltaP `25.2982` edge `0.0274` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `2.1474` n `101` status `ready` deltaP `16.1751` edge `0.1969` maxDD `-8.0625`
- `market_context_high->equity_4h` score `1.5769` n `46` status `ready` deltaP `10.1207` edge `0.0946` maxDD `-0.4529`
- `news_risk_high->crypto_major_1h` score `1.5448` n `101` status `ready` deltaP `15.3332` edge `0.0788` maxDD `-2.8494`
- `news_risk_high->crypto_alt_24h` score `1.0601` n `101` status `ready` deltaP `-6.0541` edge `0.6168` maxDD `-32.7147`
- `market_context_high->equity_1h` score `0.9756` n `46` status `ready` deltaP `7.6608` edge `0.0545` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.9669` n `46` status `ready` deltaP `8.2118` edge `0.0853` maxDD `-2.7574`
- `news_risk_high->fx_4h` score `0.8897` n `101` status `ready` deltaP `15.5004` edge `0.0344` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6854` n `46` status `ready` deltaP `10.6548` edge `0.0114` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5694` n `101` status `ready` deltaP `14.1489` edge `0.0133` maxDD `-0.8144`
- `market_context_high->metal_24h` score `0.5325` n `46` status `ready` deltaP `18.9689` edge `-0.0587` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

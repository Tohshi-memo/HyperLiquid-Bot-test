# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T11:52:33.699256+00:00`
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

- `market_context_high->unknown_1h` score `65.9226` n `47` status `ready` deltaP `10.2657` edge `5.4322` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.1759` n `46` status `ready` deltaP `30.3744` edge `3.4111` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `28.9174` n `46` status `ready` deltaP `25.3472` edge `2.2408` maxDD `0.0`
- `market_context_high->equity_24h` score `24.9345` n `46` status `ready` deltaP `27.7703` edge `1.9028` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `9.4347` n `103` status `ready` deltaP `2.6834` edge `1.6726` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.1913` n `46` status `ready` deltaP `36.798` edge `0.446` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `6.6553` n `103` status `ready` deltaP `0.1045` edge `1.2552` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.5397` n `46` status `ready` deltaP `30.7745` edge `0.1132` maxDD `-0.2042`
- `market_context_high->index_4h` score `3.0602` n `47` status `ready` deltaP `34.7885` edge `0.0385` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6273` n `47` status `ready` deltaP `17.6018` edge `0.1434` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.4937` n `115` status `ready` deltaP `13.641` edge `0.1659` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.0557` n `115` status `ready` deltaP `14.8672` edge `0.1157` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6839` n `114` status `ready` deltaP `24.7085` edge `0.0392` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.3376` n `103` status `ready` deltaP `17.4976` edge `0.1127` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.3066` n `103` status `ready` deltaP `30.1847` edge `0.1294` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.0146` n `47` status `ready` deltaP `15.2089` edge `0.011` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.9676` n `103` status `ready` deltaP `22.6487` edge `0.1179` maxDD `-7.2536`
- `market_context_high->equity_1h` score `0.9199` n `47` status `ready` deltaP `11.0173` edge `0.0435` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.7546` n `114` status `ready` deltaP `12.7862` edge `0.1908` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.7485` n `115` status `ready` deltaP `15.9021` edge `0.0157` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T08:37:28.756207+00:00`
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

- `market_context_high->unknown_1h` score `66.0522` n `47` status `ready` deltaP `10.5651` edge `5.441` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `40.7333` n `46` status `ready` deltaP `28.1175` edge `3.2226` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `25.9204` n `46` status `ready` deltaP `23.0903` edge `2.0061` maxDD `0.0`
- `market_context_high->equity_24h` score `23.6319` n `46` status `ready` deltaP `25.5133` edge `1.8093` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.8236` n `46` status `ready` deltaP `34.5411` edge `0.4304` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `6.9922` n `103` status `ready` deltaP `0.4265` edge `1.4841` maxDD `-63.6743`
- `news_risk_high->crypto_major_4h` score `4.6088` n `104` status `ready` deltaP `18.2106` edge `0.3204` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.6033` n `104` status `ready` deltaP `13.5906` edge `0.3928` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `3.6583` n `103` status `ready` deltaP `-2.1524` edge `1.0205` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.0484` n `46` status `ready` deltaP `28.5176` edge `0.0873` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.8345` n `47` status `ready` deltaP `32.8068` edge `0.0329` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.3902` n `114` status `ready` deltaP `13.2472` edge `0.1599` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.1567` n `47` status `ready` deltaP `15.6201` edge `0.1174` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0253` n `114` status `ready` deltaP `15.343` edge `0.11` maxDD `-1.8141`
- `news_risk_high->commodity_24h` score `1.7449` n `103` status `ready` deltaP `19.7546` edge `0.1316` maxDD `-2.431`
- `news_risk_high->fx_4h` score `1.6156` n `104` status `ready` deltaP `23.5694` edge `0.0411` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.277` n `103` status `ready` deltaP `30.1847` edge `0.1256` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9044` n `47` status `ready` deltaP `14.0113` edge `0.0098` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8432` n `47` status `ready` deltaP `10.5682` edge `0.0401` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.6482` n `103` status `ready` deltaP `20.3918` edge `0.092` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

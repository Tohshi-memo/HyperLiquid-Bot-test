# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T18:37:33.652079+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9883`

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

- `market_context_high->unknown_1h` score `82.6171` n `47` status `ready` deltaP `9.8166` edge `6.8264` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `32.4916` n `46` status `ready` deltaP `18.3953` edge `2.6006` maxDD `-0.5817`
- `market_context_high->equity_24h` score `18.3854` n `46` status `ready` deltaP `15.7911` edge `1.4369` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.197` n `46` status `ready` deltaP `13.3681` edge `1.1773` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `7.798` n `96` status `ready` deltaP `-4.3402` edge `1.3646` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.2274` n `46` status `ready` deltaP `24.8189` edge `0.3622` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.35` n `103` status `ready` deltaP `16.6706` edge `0.3091` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `3.942` n `103` status `ready` deltaP `11.6402` edge `0.3507` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `3.0024` n `96` status `ready` deltaP `27.7778` edge `0.1829` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.3207` n `103` status `ready` deltaP `12.2595` edge `0.1607` maxDD `-1.5895`
- `news_risk_high->crypto_alt_24h` score `2.3061` n `96` status `ready` deltaP `-6.4236` edge `0.7231` maxDD `-32.7147`
- `market_context_high->index_4h` score `2.2537` n `47` status `ready` deltaP `27.1666` edge `0.0221` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0001` n `103` status `ready` deltaP `15.7026` edge `0.1055` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3663` n `103` status `ready` deltaP `20.6326` edge `0.0399` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2014` n `96` status `ready` deltaP `28.6458` edge `0.122` maxDD `-1.7159`
- `market_context_high->metal_24h` score `0.8114` n `46` status `ready` deltaP `18.7953` edge `-0.0343` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.7716` n `47` status `ready` deltaP `7.8457` edge `0.0538` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6408` n `47` status `ready` deltaP `11.167` edge `0.0068` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.5667` n `103` status `ready` deltaP `14.6038` edge `0.0092` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.3584` n `96` status `ready` deltaP `15.625` edge `0.0262` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

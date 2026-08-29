# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T20:22:24.975086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11414`

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

- `news_risk_high->unknown_24h` score `28.7146` n `55` status `ready` deltaP `1.3731` edge `2.4811` maxDD `-4.1232`
- `market_context_high->unknown_24h` score `11.8111` n `104` status `ready` deltaP `20.9535` edge `0.9178` maxDD `-3.1917`
- `risk_on_high->crypto_alt_4h` score `10.8183` n `38` status `ready` deltaP `41.8004` edge `0.6329` maxDD `-0.1367`
- `risk_on_and_context->crypto_alt_4h` score `10.8183` n `38` status `ready` deltaP `41.8004` edge `0.6329` maxDD `-0.1367`
- `news_risk_high->crypto_alt_24h` score `10.1403` n `55` status `ready` deltaP `27.4969` edge `1.4543` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `7.7857` n `38` status `ready` deltaP `39.3614` edge `0.414` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.7857` n `38` status `ready` deltaP `39.3614` edge `0.414` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.3225` n `64` status `ready` deltaP `6.4024` edge `0.5432` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.691` n `104` status `ready` deltaP `34.415` edge `0.2634` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0566` n `38` status `ready` deltaP `33.7212` edge `0.0385` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0566` n `38` status `ready` deltaP `33.7212` edge `0.0385` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.6358` n `64` status `ready` deltaP `-1.5531` edge `0.2657` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `1.8481` n `138` status `ready` deltaP `16.6379` edge `0.0901` maxDD `-1.0945`
- `news_risk_high->fx_4h` score `1.4413` n `64` status `ready` deltaP `33.003` edge `0.0197` maxDD `-0.3953`
- `risk_on_high->equity_4h` score `1.4227` n `38` status `ready` deltaP `11.3688` edge `0.0677` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.4227` n `38` status `ready` deltaP `11.3688` edge `0.0677` maxDD `-0.3281`
- `risk_on_high->metal_1h` score `1.3117` n `48` status `ready` deltaP `18.2884` edge `0.0088` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3117` n `48` status `ready` deltaP `18.2884` edge `0.0088` maxDD `-0.0463`
- `risk_on_high->index_4h` score `0.8163` n `38` status `ready` deltaP `14.1528` edge `0.0046` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `0.8163` n `38` status `ready` deltaP `14.1528` edge `0.0046` maxDD `-0.1405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

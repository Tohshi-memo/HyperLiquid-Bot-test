# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T05:52:41.155447+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11724`

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

- `risk_on_high->crypto_alt_24h` score `21.5976` n `55` status `ready` deltaP `47.7525` edge `1.5295` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.5976` n `55` status `ready` deltaP `47.7525` edge `1.5295` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `9.6781` n `55` status `ready` deltaP `29.0404` edge `0.7547` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `9.6781` n `55` status `ready` deltaP `29.0404` edge `0.7547` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.4149` n `100` status `ready` deltaP `24.2256` edge `0.6014` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.4149` n `100` status `ready` deltaP `24.2256` edge `0.6014` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.6814` n `152` status `ready` deltaP `21.173` edge `0.485` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.2754` n `55` status `ready` deltaP `70.3125` edge `0.0542` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2754` n `55` status `ready` deltaP `70.3125` edge `0.0542` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2276` n `96` status `ready` deltaP `37.1527` edge `0.2488` maxDD `-1.8678`
- `risk_on_high->metal_24h` score `4.408` n `55` status `ready` deltaP `40.5808` edge `0.144` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.408` n `55` status `ready` deltaP `40.5808` edge `0.144` maxDD `-0.7767`
- `market_context_high->crypto_alt_24h` score `4.3281` n `96` status `ready` deltaP `22.2222` edge `0.8257` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `3.7388` n `96` status `ready` deltaP `20.1389` edge `0.4264` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.6372` n `107` status `ready` deltaP `7.8628` edge `0.225` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.6372` n `107` status `ready` deltaP `7.8628` edge `0.225` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.4146` n `159` status `ready` deltaP `7.2045` edge `0.2162` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0216` n `96` status `ready` deltaP `36.9792` edge `0.0303` maxDD `-1.6688`
- `risk_on_high->equity_24h` score `0.8075` n `55` status `ready` deltaP `18.7153` edge `0.0233` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `0.8075` n `55` status `ready` deltaP `18.7153` edge `0.0233` maxDD `-3.7955`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

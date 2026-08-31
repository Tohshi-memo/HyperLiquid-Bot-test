# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T07:37:31.167820+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11586`

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

- `risk_on_high->crypto_alt_24h` score `21.9647` n `55` status `ready` deltaP `48.6205` edge `1.5543` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.9647` n `55` status `ready` deltaP `48.6205` edge `1.5543` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `10.4281` n `55` status `ready` deltaP `30.2557` edge `0.8091` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `10.4281` n `55` status `ready` deltaP `30.2557` edge `0.8091` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.0652` n `107` status `ready` deltaP `25.4032` edge `0.5644` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0652` n `107` status `ready` deltaP `25.4032` edge `0.5644` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5192` n `159` status `ready` deltaP `22.0998` edge `0.4653` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.3942` n `55` status `ready` deltaP `71.5278` edge `0.056` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.3942` n `55` status `ready` deltaP `71.5278` edge `0.056` maxDD `0.0`
- `market_context_high->metal_24h` score `5.242` n `96` status `ready` deltaP `37.1527` edge `0.25` maxDD `-1.8678`
- `market_context_high->crypto_alt_24h` score `4.5667` n `96` status `ready` deltaP `23.0902` edge `0.8505` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `4.4888` n `96` status `ready` deltaP `21.3542` edge `0.4808` maxDD `-17.2607`
- `risk_on_high->metal_24h` score `4.4224` n `55` status `ready` deltaP `40.5808` edge `0.1452` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.4224` n `55` status `ready` deltaP `40.5808` edge `0.1452` maxDD `-0.7767`
- `risk_on_high->unknown_1h` score `2.5294` n `107` status `ready` deltaP `6.8149` edge `0.223` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.5294` n `107` status `ready` deltaP `6.8149` edge `0.223` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.3068` n `159` status `ready` deltaP `6.1566` edge `0.2142` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0988` n `96` status `ready` deltaP `38.1945` edge `0.0321` maxDD `-1.6688`
- `risk_on_high->equity_24h` score `0.9508` n `55` status `ready` deltaP `19.7569` edge `0.0283` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `0.9508` n `55` status `ready` deltaP `19.7569` edge `0.0283` maxDD `-3.7955`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

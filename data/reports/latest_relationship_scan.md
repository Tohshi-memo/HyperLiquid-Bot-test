# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T18:52:28.891322+00:00`
- Price records: `672`
- Market context records: `3307`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.7983` n `32` status `ready` deltaP `29.5732` edge `1.2316` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.7983` n `32` status `ready` deltaP `29.5732` edge `1.2316` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.4535` n `123` status `ready` deltaP `20.2152` edge `2.7024` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.2462` n `123` status `ready` deltaP `31.9952` edge `0.896` maxDD `-16.1026`
- `market_context_high->equity_24h` score `8.2347` n `123` status `ready` deltaP `23.4375` edge `1.7411` maxDD `-53.663`
- `market_context_high->commodity_24h` score `7.7954` n `123` status `ready` deltaP `32.9268` edge `0.5998` maxDD `-8.5755`
- `risk_on_high->crypto_alt_4h` score `7.3841` n `32` status `ready` deltaP `9.9848` edge `0.7332` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3841` n `32` status `ready` deltaP `9.9848` edge `0.7332` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5609` n `32` status `ready` deltaP `13.7957` edge `0.478` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5609` n `32` status `ready` deltaP `13.7957` edge `0.478` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.2185` n `123` status `ready` deltaP `21.0662` edge `2.2139` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.0712` n `32` status `ready` deltaP `7.1669` edge `0.3247` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0712` n `32` status `ready` deltaP `7.1669` edge `0.3247` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.0523` n `184` status `ready` deltaP `19.0416` edge `0.1399` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.079` n `32` status `ready` deltaP `0.8384` edge `0.1915` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.079` n `32` status `ready` deltaP `0.8384` edge `0.1915` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2837` n `32` status `ready` deltaP `6.3997` edge `0.0622` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2837` n `32` status `ready` deltaP `6.3997` edge `0.0622` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.233` n `32` status `ready` deltaP `0.4491` edge `0.1706` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.233` n `32` status `ready` deltaP `0.4491` edge `0.1706` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T20:52:23.303581+00:00`
- Price records: `672`
- Market context records: `3315`
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

- `risk_on_high->crypto_major_4h` score `15.9157` n `32` status `ready` deltaP `30.3354` edge `1.2363` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.9157` n `32` status `ready` deltaP `30.3354` edge `1.2363` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.1863` n `131` status `ready` deltaP `21.557` edge `2.7874` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.7396` n `131` status `ready` deltaP `33.1371` edge `0.9295` maxDD `-16.1026`
- `market_context_high->equity_24h` score `9.1104` n `131` status `ready` deltaP `25.4731` edge `1.8398` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3357` n `32` status `ready` deltaP `9.6799` edge `0.7312` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3357` n `32` status `ready` deltaP `9.6799` edge `0.7312` maxDD `-11.7537`
- `market_context_high->commodity_24h` score `4.9183` n `131` status `ready` deltaP `28.2098` edge `0.5211` maxDD `-16.2781`
- `risk_on_high->equity_4h` score `3.5749` n `32` status `ready` deltaP `13.7957` edge `0.4798` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5749` n `32` status `ready` deltaP `13.7957` edge `0.4798` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.1438` n `131` status `ready` deltaP `22.7059` edge `2.3216` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.0704` n `32` status `ready` deltaP `7.1669` edge `0.3246` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0704` n `32` status `ready` deltaP `7.1669` edge `0.3246` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.9798` n `185` status `ready` deltaP `18.5102` edge `0.1374` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.0884` n `32` status `ready` deltaP `0.8384` edge `0.1927` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0884` n `32` status `ready` deltaP `0.8384` edge `0.1927` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2876` n `32` status `ready` deltaP `6.3997` edge `0.0627` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2876` n `32` status `ready` deltaP `6.3997` edge `0.0627` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2415` n `32` status `ready` deltaP `0.5988` edge `0.1707` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2415` n `32` status `ready` deltaP `0.5988` edge `0.1707` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

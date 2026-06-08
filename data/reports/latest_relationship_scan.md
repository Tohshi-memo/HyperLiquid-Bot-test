# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T04:52:25.142122+00:00`
- Price records: `672`
- Market context records: `3249`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10598`

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

- `risk_on_high->crypto_major_4h` score `16.7154` n `31` status `ready` deltaP `30.8517` edge `1.2995` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.7154` n `31` status `ready` deltaP `30.8517` edge `1.2995` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.9688` n `103` status `ready` deltaP `17.088` edge `2.6611` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.3695` n `103` status `ready` deltaP `47.647` edge `0.8393` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.31` n `103` status `ready` deltaP `30.4477` edge `0.8283` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.2647` n `103` status `ready` deltaP `17.8331` edge `1.5259` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `5.1632` n `31` status `ready` deltaP `12.1312` edge `0.7655` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.1632` n `31` status `ready` deltaP `12.1312` edge `0.7655` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.2131` n `31` status `ready` deltaP `18.809` edge `0.5282` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.2131` n `31` status `ready` deltaP `18.809` edge `0.5282` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.6149` n `31` status `ready` deltaP `10.5273` edge `0.372` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.6149` n `31` status `ready` deltaP `10.5273` edge `0.372` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.1532` n `147` status `ready` deltaP `18.8485` edge `0.1496` maxDD `-3.9989`
- `market_context_high->crypto_major_24h` score `1.9261` n `103` status `ready` deltaP `21.1586` edge `2.1758` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.5803` n `31` status `ready` deltaP `5.7533` edge `0.223` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.5803` n `31` status `ready` deltaP `5.7533` edge `0.223` maxDD `-1.7001`
- `risk_on_high->crypto_alt_1h` score `0.716` n `31` status `ready` deltaP `3.7087` edge `0.2108` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.716` n `31` status `ready` deltaP `3.7087` edge `0.2108` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4849` n `31` status `ready` deltaP `8.2142` edge `0.0759` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4849` n `31` status `ready` deltaP `8.2142` edge `0.0759` maxDD `-1.4793`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

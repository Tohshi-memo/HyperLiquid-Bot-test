# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T08:37:25.592543+00:00`
- Price records: `672`
- Market context records: `3366`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `56.9147` n `32` status `ready` deltaP `60.0694` edge `4.3467` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.9147` n `32` status `ready` deltaP `60.0694` edge `4.3467` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.6635` n `32` status `ready` deltaP `55.0347` edge `4.1202` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.6635` n `32` status `ready` deltaP `55.0347` edge `4.1202` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.0305` n `32` status `ready` deltaP `56.7708` edge `3.4574` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.0305` n `32` status `ready` deltaP `56.7708` edge `3.4574` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1794` n `32` status `ready` deltaP `50.8681` edge `1.5925` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1794` n `32` status `ready` deltaP `50.8681` edge `1.5925` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `15.3968` n `32` status `ready` deltaP `28.0488` edge `1.2083` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.3968` n `32` status `ready` deltaP `28.0488` edge `1.2083` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `15.0897` n `32` status `ready` deltaP `32.9861` edge `1.0637` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.0897` n `32` status `ready` deltaP `32.9861` edge `1.0637` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `13.3485` n `159` status `ready` deltaP `17.9081` edge `2.4752` maxDD `-63.6589`
- `market_context_high->index_24h` score `11.9885` n `159` status `ready` deltaP `35.7738` edge `1.016` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.6809` n `159` status `ready` deltaP `30.9846` edge `2.0044` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.292` n `32` status `ready` deltaP `8.3079` edge `0.7367` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.292` n `32` status `ready` deltaP `8.3079` edge `0.7367` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5502` n `32` status `ready` deltaP `14.1006` edge `0.4746` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5502` n `32` status `ready` deltaP `14.1006` edge `0.4746` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.4404` n `159` status `ready` deltaP `21.056` edge `2.0855` maxDD `-131.4499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

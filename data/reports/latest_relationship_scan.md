# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T17:52:29.227627+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12899`

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

- `market_context_high->unknown_24h` score `8132.0177` n `84` status `ready` deltaP `13.0704` edge `677.5862` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `5354.9065` n `43` status `ready` deltaP `15.4514` edge `446.1392` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5354.9065` n `43` status `ready` deltaP `15.4514` edge `446.1392` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.1591` n `82` status `ready` deltaP `-5.2505` edge `32.0071` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `21.0566` n `67` status `ready` deltaP `46.3257` edge `1.5655` maxDD `-6.9028`
- `news_risk_high->crypto_alt_24h` score `17.0087` n `67` status `ready` deltaP `29.2781` edge `1.271` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.6031` n `43` status `ready` deltaP `38.5457` edge `1.1496` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.6031` n `43` status `ready` deltaP `38.5457` edge `1.1496` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.552` n `84` status `ready` deltaP `31.126` edge `1.0879` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `9.7663` n `67` status `ready` deltaP `26.0468` edge `0.7069` maxDD `-2.668`
- `risk_on_high->equity_24h` score `9.687` n `43` status `ready` deltaP `40.9722` edge `0.5341` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.687` n `43` status `ready` deltaP `40.9722` edge `0.5341` maxDD `0.0`
- `market_context_high->equity_24h` score `9.3594` n `84` status `ready` deltaP `40.9722` edge `0.5068` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4637` n `46` status `ready` deltaP `41.8015` edge `0.4638` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4637` n `46` status `ready` deltaP `41.8015` edge `0.4638` maxDD `-1.9733`
- `news_risk_high->index_24h` score `6.9117` n `67` status `ready` deltaP `44.8305` edge `0.2906` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.6772` n `67` status `ready` deltaP `42.5736` edge `0.3122` maxDD `-0.5008`
- `risk_on_high->index_24h` score `4.9264` n `43` status `ready` deltaP `49.7941` edge `0.0828` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9264` n `43` status `ready` deltaP `49.7941` edge `0.0828` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1043` n `46` status `ready` deltaP `36.4263` edge `0.1085` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

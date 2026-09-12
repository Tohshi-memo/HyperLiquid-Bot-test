# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T17:07:28.582635+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12401`

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

- `market_context_high->unknown_24h` score `7405.6883` n `87` status `ready` deltaP `13.1525` edge `617.0582` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `5354.4025` n `43` status `ready` deltaP `15.4514` edge `446.0972` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5354.4025` n `43` status `ready` deltaP `15.4514` edge `446.0972` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.0223` n `82` status `ready` deltaP `-5.1008` edge `31.9947` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `22.4491` n `64` status `ready` deltaP `49.8264` edge `1.6328` maxDD `-5.8705`
- `news_risk_high->crypto_alt_24h` score `16.9964` n `64` status `ready` deltaP `28.2986` edge `1.2765` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.5659` n `43` status `ready` deltaP `38.5457` edge `1.1465` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.5659` n `43` status `ready` deltaP `38.5457` edge `1.1465` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.8158` n `87` status `ready` deltaP `31.7828` edge `1.1055` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `10.8683` n `64` status `ready` deltaP `29.5139` edge `0.7485` maxDD `-1.4989`
- `risk_on_high->equity_24h` score `9.6081` n `43` status `ready` deltaP `40.4514` edge `0.531` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.6081` n `43` status `ready` deltaP `40.4514` edge `0.531` maxDD `0.0`
- `market_context_high->equity_24h` score `9.2157` n `87` status `ready` deltaP `40.4514` edge `0.4983` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4957` n `43` status `ready` deltaP `41.3465` edge `0.4695` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4957` n `43` status `ready` deltaP `41.3465` edge `0.4695` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.3526` n `64` status `ready` deltaP `48.4375` edge `0.3033` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `7.3202` n `64` status `ready` deltaP `46.7014` edge `0.3234` maxDD `-0.3112`
- `risk_on_high->index_24h` score `4.8823` n `43` status `ready` deltaP `49.2733` edge `0.0826` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8823` n `43` status `ready` deltaP `49.2733` edge `0.0826` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1339` n `43` status `ready` deltaP `35.9721` edge `0.114` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

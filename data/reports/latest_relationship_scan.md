# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T08:07:27.451170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->crypto_alt_4h` score `7.6024` n `132` status `ready` deltaP `18.4775` edge `0.6018` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0557` n `54` status `ready` deltaP `38.5017` edge `0.3313` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0557` n `54` status `ready` deltaP `38.5017` edge `0.3313` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `6.5844` n `58` status `ready` deltaP `36.2647` edge `0.3922` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.5844` n `58` status `ready` deltaP `36.2647` edge `0.3922` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `6.2121` n `132` status `ready` deltaP `23.9606` edge `0.4901` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.2024` n `58` status `ready` deltaP `17.746` edge `0.3599` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.2024` n `58` status `ready` deltaP `17.746` edge `0.3599` maxDD `-1.907`
- `market_context_high->crypto_alt_1h` score `1.2784` n `144` status `ready` deltaP `11.2608` edge `0.1379` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1543` n `144` status `ready` deltaP `8.7824` edge `0.1182` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4186` n `132` status `ready` deltaP `13.1883` edge `0.0515` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `0.0007` n `70` status `ready` deltaP `7.592` edge `0.0217` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `0.0007` n `70` status `ready` deltaP `7.592` edge `0.0217` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.0527` n `70` status `ready` deltaP `4.4273` edge `0.0045` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0527` n `70` status `ready` deltaP `4.4273` edge `0.0045` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.2118` n `144` status `ready` deltaP `6.5503` edge `0.004` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2382` n `144` status `ready` deltaP `8.6993` edge `0.0091` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4509` n `70` status `ready` deltaP `1.7151` edge `0.0039` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4509` n `70` status `ready` deltaP `1.7151` edge `0.0039` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.5126` n `144` status `ready` deltaP `7.6577` edge `0.0342` maxDD `-7.0778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

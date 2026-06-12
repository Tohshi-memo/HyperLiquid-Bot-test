# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T10:07:35.017818+00:00`
- Price records: `672`
- Market context records: `3675`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `33.46` n `32` status `ready` deltaP `37.5` edge `2.5426` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.46` n `32` status `ready` deltaP `37.5` edge `2.5426` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `27.7614` n `32` status `ready` deltaP `39.7569` edge `2.0484` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `27.7614` n `32` status `ready` deltaP `39.7569` edge `2.0484` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `25.2537` n `32` status `ready` deltaP `36.6319` edge `1.8754` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `25.2537` n `32` status `ready` deltaP `36.6319` edge `1.8754` maxDD `-0.8779`
- `risk_on_high->index_24h` score `15.3683` n `32` status `ready` deltaP `39.5833` edge `1.0168` maxDD `0.0`
- `risk_on_and_context->index_24h` score `15.3683` n `32` status `ready` deltaP `39.5833` edge `1.0168` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.4654` n `32` status `ready` deltaP `20.4268` edge `0.9315` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.4654` n `32` status `ready` deltaP `20.4268` edge `0.9315` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `6.5759` n `32` status `ready` deltaP `25.1736` edge `0.4063` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `6.5759` n `32` status `ready` deltaP `25.1736` edge `0.4063` maxDD `-0.7574`
- `market_context_high->index_24h` score `4.9722` n `157` status `ready` deltaP `24.9336` edge `0.4197` maxDD `-11.3924`
- `market_context_high->equity_24h` score `3.4734` n `157` status `ready` deltaP `16.827` edge `0.7437` maxDD `-35.3144`
- `risk_on_high->equity_4h` score `2.6001` n `32` status `ready` deltaP `10.2896` edge `0.3782` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6001` n `32` status `ready` deltaP `10.2896` edge `0.3782` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.5876` n `32` status `ready` deltaP `0.5335` edge `0.3965` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.5876` n `32` status `ready` deltaP `0.5335` edge `0.3965` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.2386` n `32` status `ready` deltaP `2.8256` edge `0.2469` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2386` n `32` status `ready` deltaP `2.8256` edge `0.2469` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

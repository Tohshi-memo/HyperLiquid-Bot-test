# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T20:22:26.443600+00:00`
- Price records: `672`
- Market context records: `3720`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13025`

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

- `risk_on_high->crypto_major_24h` score `29.5633` n `32` status `ready` deltaP `31.0764` edge `2.2607` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.5633` n `32` status `ready` deltaP `31.0764` edge `2.2607` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.3431` n `32` status `ready` deltaP `33.3333` edge `1.6397` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.3431` n `32` status `ready` deltaP `33.3333` edge `1.6397` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.7876` n `32` status `ready` deltaP `31.0764` edge `1.6236` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.7876` n `32` status `ready` deltaP `31.0764` edge `1.6236` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.7294` n `32` status `ready` deltaP `32.8125` edge `0.7587` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.7294` n `32` status `ready` deltaP `32.8125` edge `0.7587` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.2415` n `32` status `ready` deltaP `17.6829` edge `0.8478` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.2415` n `32` status `ready` deltaP `17.6829` edge `0.8478` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.0027` n `158` status `ready` deltaP `17.5105` edge `0.6272` maxDD `-13.1633`
- `market_context_high->index_24h` score `4.8316` n `158` status `ready` deltaP `23.9517` edge `0.3569` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.5071` n `158` status `ready` deltaP `19.5588` edge `0.2717` maxDD `-9.1203`
- `risk_on_high->metal_24h` score `2.0416` n `32` status `ready` deltaP `18.0556` edge `0.0759` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.0416` n `32` status `ready` deltaP `18.0556` edge `0.0759` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.9515` n `32` status `ready` deltaP `-0.5335` edge `0.3506` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.9515` n `32` status `ready` deltaP `-0.5335` edge `0.3506` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `1.5453` n `32` status `ready` deltaP `8.1555` edge `0.2572` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5453` n `32` status `ready` deltaP `8.1555` edge `0.2572` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.104` n `158` status `ready` deltaP `3.1887` edge `0.6106` maxDD `-36.8551`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

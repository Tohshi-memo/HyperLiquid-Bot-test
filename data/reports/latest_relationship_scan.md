# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T14:52:25.288306+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12636`

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

- `market_context_high->unknown_24h` score `5493.8139` n `96` status `ready` deltaP `13.3681` edge `457.7339` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `3107.9845` n `49` status `ready` deltaP `15.4514` edge `258.8957` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3107.9845` n `49` status `ready` deltaP `15.4514` edge `258.8957` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.1891` n `82` status `ready` deltaP `-5.1008` edge `32.0086` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.8768` n `59` status `ready` deltaP `55.5467` edge `1.7928` maxDD `-5.8705`
- `news_risk_high->crypto_alt_24h` score `17.8773` n `59` status `ready` deltaP `30.8351` edge `1.333` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `17.7282` n `49` status `ready` deltaP `39.2751` edge `1.2385` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.7282` n `49` status `ready` deltaP `39.2751` edge `1.2385` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.5246` n `96` status `ready` deltaP `32.8125` edge `1.1577` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.5365` n `59` status `ready` deltaP `35.4991` edge `0.8179` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.1387` n `49` status `ready` deltaP `38.8889` edge `0.5023` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1387` n `49` status `ready` deltaP `38.8889` edge `0.5023` maxDD `0.0`
- `market_context_high->equity_24h` score `8.8291` n `96` status `ready` deltaP `38.8889` edge `0.4765` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6637` n `49` status `ready` deltaP `42.2008` edge `0.4778` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6637` n `49` status `ready` deltaP `42.2008` edge `0.4778` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.5054` n `59` status `ready` deltaP `54.6875` edge `0.3442` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9522` n `59` status `ready` deltaP `51.9921` edge `0.3254` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8512` n `49` status `ready` deltaP `49.2595` edge `0.0801` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8512` n `49` status `ready` deltaP `49.2595` edge `0.0801` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1105` n `49` status `ready` deltaP `36.6538` edge `0.1075` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

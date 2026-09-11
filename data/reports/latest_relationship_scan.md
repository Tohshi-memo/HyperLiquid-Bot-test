# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T07:22:27.073965+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12358`

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

- `news_risk_high->unknown_1h` score `750.8525` n `59` status `ready` deltaP `-6.3585` edge `62.6556` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `21.6181` n `91` status `ready` deltaP `38.4291` edge `1.5683` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.6181` n `91` status `ready` deltaP `38.4291` edge `1.5683` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.7543` n `178` status `ready` deltaP `34.9348` edge `1.4127` maxDD `-3.9523`
- `market_context_high->equity_24h` score `8.9761` n `178` status `ready` deltaP `32.9861` edge `0.5281` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9123` n `91` status `ready` deltaP `41.1837` edge `0.5053` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9123` n `91` status `ready` deltaP `41.1837` edge `0.5053` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `8.3401` n `91` status `ready` deltaP `32.9861` edge `0.4751` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.3401` n `91` status `ready` deltaP `32.9861` edge `0.4751` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.6511` n `91` status `ready` deltaP `32.0491` edge `0.5098` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6511` n `91` status `ready` deltaP `32.0491` edge `0.5098` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2932` n `91` status `ready` deltaP `25.021` edge `1.175` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2932` n `91` status `ready` deltaP `25.021` edge `1.175` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.267` n `91` status `ready` deltaP `48.7866` edge `0.1179` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.267` n `91` status `ready` deltaP `48.7866` edge `0.1179` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.2246` n `178` status `ready` deltaP `41.9709` edge `0.1116` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.707` n `91` status `ready` deltaP `34.5651` edge `0.0878` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.707` n `91` status `ready` deltaP `34.5651` edge `0.0878` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.339` n `178` status `ready` deltaP `27.1136` edge `0.0997` maxDD `-2.843`
- `risk_on_high->equity_1h` score `1.601` n `91` status `ready` deltaP `21.0338` edge `0.021` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

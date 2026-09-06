# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T19:22:31.333210+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10365`

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

- `risk_on_high->unknown_24h` score `239.9877` n `103` status `ready` deltaP `25.2124` edge `19.8408` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `239.9877` n `103` status `ready` deltaP `25.2124` edge `19.8408` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `19.764` n `103` status `ready` deltaP `32.376` edge `1.4915` maxDD `-3.1605`
- `risk_on_and_context->crypto_major_24h` score `19.764` n `103` status `ready` deltaP `32.376` edge `1.4915` maxDD `-3.1605`
- `risk_on_high->crypto_alt_24h` score `11.4161` n `103` status `ready` deltaP `24.1774` edge `0.8737` maxDD `-4.35`
- `risk_on_and_context->crypto_alt_24h` score `11.4161` n `103` status `ready` deltaP `24.1774` edge `0.8737` maxDD `-4.35`
- `market_context_high->crypto_alt_24h` score `6.9356` n `196` status `ready` deltaP `20.2097` edge `0.5521` maxDD `-5.7094`
- `market_context_high->equity_24h` score `6.2694` n `196` status `ready` deltaP `21.7439` edge `0.4013` maxDD `-0.5715`
- `risk_on_high->equity_24h` score `5.324` n `103` status `ready` deltaP `19.9012` edge `0.3348` maxDD `-0.5715`
- `risk_on_and_context->equity_24h` score `5.324` n `103` status `ready` deltaP `19.9012` edge `0.3348` maxDD `-0.5715`
- `risk_on_high->index_24h` score `1.7716` n `103` status `ready` deltaP `18.6927` edge `0.0755` maxDD `-1.1989`
- `risk_on_and_context->index_24h` score `1.7716` n `103` status `ready` deltaP `18.6927` edge `0.0755` maxDD `-1.1989`
- `market_context_high->index_24h` score `1.6139` n `196` status `ready` deltaP `19.2673` edge `0.0899` maxDD `-1.7083`
- `risk_on_high->crypto_alt_4h` score `0.8248` n `118` status `ready` deltaP `24.5866` edge `0.1996` maxDD `-20.5825`
- `risk_on_and_context->crypto_alt_4h` score `0.8248` n `118` status `ready` deltaP `24.5866` edge `0.1996` maxDD `-20.5825`
- `risk_on_high->metal_24h` score `0.7199` n `103` status `ready` deltaP `14.7013` edge `0.0883` maxDD `-4.4387`
- `risk_on_and_context->metal_24h` score `0.7199` n `103` status `ready` deltaP `14.7013` edge `0.0883` maxDD `-4.4387`
- `risk_on_high->crypto_alt_1h` score `0.2857` n `129` status `ready` deltaP `3.8516` edge `0.0686` maxDD `-3.971`
- `risk_on_and_context->crypto_alt_1h` score `0.2857` n `129` status `ready` deltaP `3.8516` edge `0.0686` maxDD `-3.971`
- `risk_on_high->index_1h` score `0.1071` n `129` status `ready` deltaP `9.1712` edge `-0.0027` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

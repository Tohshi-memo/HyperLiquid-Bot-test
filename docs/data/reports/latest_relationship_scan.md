# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T06:07:28.795204+00:00`
- Price records: `672`
- Market context records: `3557`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13220`

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

- `risk_on_high->crypto_major_24h` score `51.3941` n `32` status `ready` deltaP `56.1471` edge `3.9128` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `51.3941` n `32` status `ready` deltaP `56.1471` edge `3.9128` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `46.0568` n `32` status `ready` deltaP `55.8005` edge `3.4812` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `46.0568` n `32` status `ready` deltaP `55.8005` edge `3.4812` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.6464` n `32` status `ready` deltaP `53.8995` edge `3.3612` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.6464` n `32` status `ready` deltaP `53.8995` edge `3.3612` maxDD `0.0`
- `risk_on_high->index_24h` score `25.6048` n `32` status `ready` deltaP `53.8995` edge `1.7744` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.6048` n `32` status `ready` deltaP `53.8995` edge `1.7744` maxDD `0.0`
- `market_context_high->equity_24h` score `19.0024` n `156` status `ready` deltaP `30.8226` edge `2.0193` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6499` n `32` status `ready` deltaP `37.0342` edge `1.3334` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6499` n `32` status `ready` deltaP `37.0342` edge `1.3334` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `15.96` n `156` status `ready` deltaP `21.4516` edge `1.9601` maxDD `-54.8486`
- `market_context_high->index_24h` score `14.2201` n `156` status `ready` deltaP `38.5149` edge `1.1499` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.8284` n `32` status `ready` deltaP `26.2195` edge `1.0898` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.8284` n `32` status `ready` deltaP `26.2195` edge `1.0898` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `11.9696` n `156` status `ready` deltaP `15.9768` edge `1.6952` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.614` n `156` status `ready` deltaP `31.1047` edge `1.2228` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.4092` n `32` status `ready` deltaP `6.4787` edge `0.592` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.4092` n `32` status `ready` deltaP `6.4787` edge `0.592` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7785` n `32` status `ready` deltaP `15.625` edge `0.4937` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

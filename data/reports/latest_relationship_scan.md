# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T02:37:25.155223+00:00`
- Price records: `672`
- Market context records: `7311`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14799`

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

- `risk_on_high->crypto_major_1h` score `1.2949` n `32` status `ready` deltaP `20.156` edge `0.0561` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2949` n `32` status `ready` deltaP `20.156` edge `0.0561` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2736` n `32` status `ready` deltaP `4.7226` edge `0.0413` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2736` n `32` status `ready` deltaP `4.7226` edge `0.0413` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2214` n `32` status `ready` deltaP `4.0761` edge `0.0192` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2214` n `32` status `ready` deltaP `4.0761` edge `0.0192` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.1212` n `32` status `ready` deltaP `0.0747` edge `0.0521` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1212` n `32` status `ready` deltaP `0.0747` edge `0.0521` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.2136` n `129` status `ready` deltaP `3.2635` edge `-0.0002` maxDD `-0.5821`
- `market_context_high->commodity_1h` score `-0.7321` n `129` status `ready` deltaP `-3.3367` edge `-0.0144` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7386` n `129` status `ready` deltaP `-4.1921` edge `-0.0059` maxDD `-1.868`
- `market_context_high->fx_24h` score `-0.773` n `111` status `ready` deltaP `3.0877` edge `0.0031` maxDD `-2.1564`
- `market_context_high->crypto_major_1h` score `-0.7942` n `129` status `ready` deltaP `3.3198` edge `0.0171` maxDD `-7.6171`
- `market_context_high->commodity_4h` score `-0.8655` n `121` status `ready` deltaP `0.2516` edge `-0.0158` maxDD `-2.4139`
- `risk_on_high->index_1h` score `-0.9426` n `32` status `ready` deltaP `-14.0274` edge `0.0055` maxDD `-0.2932`
- `risk_on_and_context->index_1h` score `-0.9426` n `32` status `ready` deltaP `-14.0274` edge `0.0055` maxDD `-0.2932`
- `market_context_high->crypto_alt_1h` score `-1.0721` n `129` status `ready` deltaP `-1.0881` edge `0.0218` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-1.0975` n `121` status `ready` deltaP `1.7057` edge `0.0079` maxDD `-1.4649`
- `risk_on_high->fx_1h` score `-1.2055` n `32` status `ready` deltaP `-9.5999` edge `-0.0081` maxDD `-0.2687`
- `risk_on_and_context->fx_1h` score `-1.2055` n `32` status `ready` deltaP `-9.5999` edge `-0.0081` maxDD `-0.2687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T23:37:45.793605+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8526`

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

- `market_context_high->commodity_24h` score `1.9781` n `97` status `ready` deltaP `16.2887` edge `0.1414` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.7198` n `97` status `ready` deltaP `16.1161` edge `0.4535` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.5629` n `64` status `ready` deltaP `16.5625` edge `0.0996` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.5629` n `64` status `ready` deltaP `16.5625` edge `0.0996` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `0.9788` n `64` status `ready` deltaP `14.6341` edge `0.276` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.9788` n `64` status `ready` deltaP `14.6341` edge `0.276` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.4915` n `97` status `ready` deltaP `5.5204` edge `0.1151` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.0061` n `64` status `ready` deltaP `5.4946` edge `0.001` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0061` n `64` status `ready` deltaP `5.4946` edge `0.001` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.3096` n `64` status `ready` deltaP `0.0` edge `-0.0029` maxDD `-0.2766`
- `risk_on_and_context->fx_1h` score `-0.3096` n `64` status `ready` deltaP `0.0` edge `-0.0029` maxDD `-0.2766`
- `market_context_high->index_1h` score `-0.531` n `97` status `ready` deltaP `1.387` edge `-0.0025` maxDD `-1.3195`
- `market_context_high->crypto_alt_1h` score `-0.6493` n `97` status `ready` deltaP `-1.4615` edge `0.0765` maxDD `-7.3329`
- `market_context_high->metal_1h` score `-0.6726` n `97` status `ready` deltaP `-0.747` edge `0.0057` maxDD `-0.9556`
- `market_context_high->fx_4h` score `-0.7167` n `97` status `ready` deltaP `-4.3681` edge `0.0003` maxDD `-0.7115`
- `risk_on_high->crypto_major_1h` score `-0.7281` n `64` status `ready` deltaP `-1.7122` edge `0.01` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.7281` n `64` status `ready` deltaP `-1.7122` edge `0.01` maxDD `-4.6876`
- `risk_on_high->fx_4h` score `-0.8754` n `64` status `ready` deltaP `-6.0111` edge `-0.0021` maxDD `-0.462`
- `risk_on_and_context->fx_4h` score `-0.8754` n `64` status `ready` deltaP `-6.0111` edge `-0.0021` maxDD `-0.462`
- `market_context_high->fx_1h` score `-0.9393` n `97` status `ready` deltaP `-3.6082` edge `-0.0021` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

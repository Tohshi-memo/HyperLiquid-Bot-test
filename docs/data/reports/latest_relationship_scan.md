# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T20:37:30.177688+00:00`
- Price records: `672`
- Market context records: `5593`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11423`

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

- `market_context_high->equity_24h` score `3.7399` n `174` status `ready` deltaP `15.0084` edge `0.7195` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2449` n `207` status `ready` deltaP `11.9388` edge `0.2534` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.0839` n `174` status `ready` deltaP `19.8755` edge `0.0552` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.603` n `207` status `ready` deltaP `6.7817` edge `0.1689` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.5649` n `207` status `ready` deltaP `6.9834` edge `0.1646` maxDD `-9.46`
- `market_context_high->crypto_major_24h` score `-0.218` n `174` status `ready` deltaP `11.8894` edge `0.3566` maxDD `-29.6555`
- `market_context_high->equity_1h` score `-0.237` n `219` status `ready` deltaP `5.3564` edge `0.0346` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.2885` n `219` status `ready` deltaP `1.3138` edge `0.0011` maxDD `-0.4148`
- `market_context_high->index_1h` score `-0.3688` n `219` status `ready` deltaP `1.8005` edge `0.0066` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.5945` n `219` status `ready` deltaP `1.052` edge `0.0396` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5979` n `219` status `ready` deltaP `4.0385` edge `0.0478` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.607` n `219` status `ready` deltaP `-1.6057` edge `0.0004` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-1.0044` n `207` status `ready` deltaP `3.5503` edge `0.0086` maxDD `-0.9444`
- `market_context_high->commodity_1h` score `-1.1813` n `219` status `ready` deltaP `-2.2045` edge `-0.0072` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.4966` n `207` status `ready` deltaP `3.2712` edge `0.0144` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.2604` n `174` status `ready` deltaP `11.1291` edge `0.0347` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9266` n `207` status `ready` deltaP `-11.8873` edge `-0.0576` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1463` n `207` status `ready` deltaP `-5.0511` edge `-0.0443` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0239` n `174` status `ready` deltaP `-8.3273` edge `-0.2371` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.3097` n `174` status `ready` deltaP `1.6763` edge `-0.0006` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T22:37:28.889992+00:00`
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

- `market_context_high->commodity_24h` score `1.94` n `101` status `ready` deltaP `16.532` edge `0.1366` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.8693` n `101` status `ready` deltaP `17.79` edge `0.4615` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `1.2554` n `68` status `ready` deltaP `17.2076` edge `0.2943` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.2554` n `68` status `ready` deltaP `17.2076` edge `0.2943` maxDD `-11.1788`
- `risk_on_high->commodity_24h` score `1.0319` n `68` status `ready` deltaP `17.2455` edge `0.0971` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.0319` n `68` status `ready` deltaP `17.2455` edge `0.0971` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.6171` n `101` status `ready` deltaP `7.276` edge `0.1195` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.161` n `68` status `ready` deltaP `8.3775` edge `0.0032` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.161` n `68` status `ready` deltaP `8.3775` edge `0.0032` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.3201` n `68` status `ready` deltaP `-0.1502` edge `-0.0028` maxDD `-0.3121`
- `risk_on_and_context->fx_1h` score `-0.3201` n `68` status `ready` deltaP `-0.1502` edge `-0.0028` maxDD `-0.3121`
- `market_context_high->index_1h` score `-0.4109` n `101` status `ready` deltaP `3.4416` edge `-0.0008` maxDD `-1.3195`
- `market_context_high->crypto_alt_1h` score `-0.4326` n `101` status `ready` deltaP `0.7841` edge `0.0893` maxDD `-7.3329`
- `risk_on_high->crypto_major_1h` score `-0.483` n `68` status `ready` deltaP `1.3209` edge `0.0212` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.483` n `68` status `ready` deltaP `1.3209` edge `0.0212` maxDD `-4.6876`
- `risk_on_high->equity_1h` score `-0.6354` n `68` status `ready` deltaP `9.6405` edge `0.0124` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.6354` n `68` status `ready` deltaP `9.6405` edge `0.0124` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.6405` n `68` status `ready` deltaP `-1.9902` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.6405` n `68` status `ready` deltaP `-1.9902` edge `0.0043` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.7811` n `101` status `ready` deltaP `-1.2512` edge `0.0419` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

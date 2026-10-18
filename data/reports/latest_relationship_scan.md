# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T23:22:32.915232+00:00`
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

- `market_context_high->commodity_24h` score `1.9776` n `98` status `ready` deltaP `16.3567` edge `0.1409` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.761` n `98` status `ready` deltaP `16.5474` edge `0.4559` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.5862` n `65` status `ready` deltaP `16.7492` edge `0.1003` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.5862` n `65` status `ready` deltaP `16.7492` edge `0.1003` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `1.0505` n `65` status `ready` deltaP `15.3072` edge `0.2807` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.0505` n `65` status `ready` deltaP `15.3072` edge `0.2807` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.5236` n `98` status `ready` deltaP `5.9727` edge `0.1162` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0375` n `65` status `ready` deltaP `6.2879` edge `0.0013` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0375` n `65` status `ready` deltaP `6.2879` edge `0.0013` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.3512` n `65` status `ready` deltaP `-0.7692` edge `-0.003` maxDD `-0.2851`
- `risk_on_and_context->fx_1h` score `-0.3512` n `65` status `ready` deltaP `-0.7692` edge `-0.003` maxDD `-0.2851`
- `market_context_high->index_1h` score `-0.4999` n `98` status `ready` deltaP `1.9551` edge `-0.0023` maxDD `-1.3195`
- `market_context_high->crypto_alt_1h` score `-0.602` n `98` status `ready` deltaP `-0.8829` edge `0.0787` maxDD `-7.3329`
- `market_context_high->metal_1h` score `-0.6358` n `98` status `ready` deltaP `-0.1894` edge `0.0067` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.6642` n `65` status `ready` deltaP `-0.9189` edge `0.0129` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.6642` n `65` status `ready` deltaP `-0.9189` edge `0.0129` maxDD `-4.6876`
- `market_context_high->fx_4h` score `-0.7438` n `98` status `ready` deltaP `-4.7994` edge `-0.0003` maxDD `-0.7115`
- `market_context_high->metal_4h` score `-0.9108` n `98` status `ready` deltaP `-3.0395` edge `0.0372` maxDD `-1.6961`
- `risk_on_high->equity_1h` score `-0.9406` n `65` status `ready` deltaP `7.2649` edge `0.0028` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.9406` n `65` status `ready` deltaP `7.2649` edge `0.0028` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

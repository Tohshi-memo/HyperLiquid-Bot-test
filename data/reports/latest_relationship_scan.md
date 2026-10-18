# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T15:22:32.676282+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `market_context_high->commodity_24h` score `2.1369` n `129` status `ready` deltaP `19.2935` edge `0.1346` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.9061` n `90` status `ready` deltaP `20.7922` edge `0.1` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.9061` n `90` status `ready` deltaP `20.7922` edge `0.1` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `0.9442` n `130` status `ready` deltaP `15.4808` edge `0.3583` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.6817` n `130` status `ready` deltaP `5.3846` edge `0.1098` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.6128` n `91` status `ready` deltaP `15.5907` edge `0.2227` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.6128` n `91` status `ready` deltaP `15.5907` edge `0.2227` maxDD `-11.1788`
- `risk_on_high->index_1h` score `0.086` n `91` status `ready` deltaP `5.907` edge `0.0062` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.086` n `91` status `ready` deltaP `5.907` edge `0.0062` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.2401` n `130` status `ready` deltaP `3.2727` edge `0.0974` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.2406` n `91` status `ready` deltaP `1.4982` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2406` n `91` status `ready` deltaP `1.4982` edge `-0.0028` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.3107` n `91` status `ready` deltaP `10.6096` edge `0.033` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.3107` n `91` status `ready` deltaP `10.6096` edge `0.033` maxDD `-5.3696`
- `market_context_high->index_1h` score `-0.3406` n `130` status `ready` deltaP `4.1488` edge `0.0035` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.4759` n `91` status `ready` deltaP `1.1449` edge `0.0045` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4759` n `91` status `ready` deltaP `1.1449` edge `0.0045` maxDD `-0.8513`
- `market_context_high->metal_1h` score `-0.6252` n `130` status `ready` deltaP `3.8922` edge `0.0089` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.6551` n `91` status `ready` deltaP `-0.5495` edge `0.0116` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.6551` n `91` status `ready` deltaP `-0.5495` edge `0.0116` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

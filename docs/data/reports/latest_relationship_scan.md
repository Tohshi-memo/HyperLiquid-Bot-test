# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T00:37:17.096545+00:00`
- Price records: `672`
- Market context records: `1271`
- Flow alert records: `5567`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `18.0109` n `128` status `ready` deltaP `41.5798` edge `1.3369` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.2585` n `128` status `ready` deltaP `5.7292` edge `0.9834` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.6474` n `128` status `ready` deltaP `25.0868` edge `0.755` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `7.8616` n `129` status `ready` deltaP `6.1933` edge `0.7355` maxDD `-6.7322`
- `market_context_high->index_24h` score `5.0797` n `128` status `ready` deltaP `26.7361` edge `0.3537` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8308` n `128` status `ready` deltaP `24.8264` edge `0.5583` maxDD `-14.2815`
- `market_context_high->equity_4h` score `3.7588` n `129` status `ready` deltaP `18.9993` edge `0.2529` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3406` n `128` status `ready` deltaP `1.5625` edge `0.4576` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.934` n `128` status `ready` deltaP `-11.9792` edge `0.3892` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.9219` n `129` status `ready` deltaP `15.0843` edge `0.1279` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.9095` n `129` status `ready` deltaP `18.269` edge `0.0971` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.6176` n `141` status `ready` deltaP `9.0245` edge `0.0241` maxDD `-0.6235`
- `market_context_high->equity_1h` score `0.5538` n `141` status `ready` deltaP `5.8097` edge `0.0457` maxDD `-1.3957`
- `market_context_high->metal_1h` score `0.5092` n `141` status `ready` deltaP `12.3254` edge `0.0213` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.3321` n `129` status `ready` deltaP `8.7978` edge `0.1827` maxDD `-8.9022`
- `market_context_high->fx_24h` score `0.0686` n `128` status `ready` deltaP `3.3855` edge `0.0296` maxDD `-0.3831`
- `market_context_high->crypto_alt_4h` score `-0.2734` n `129` status `ready` deltaP `9.8944` edge `0.2011` maxDD `-17.1694`
- `market_context_high->crypto_alt_1h` score `-0.3308` n `141` status `ready` deltaP `1.2061` edge `0.0366` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.3753` n `141` status `ready` deltaP `2.4748` edge `-0.0022` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.6679` n `141` status `ready` deltaP `0.8037` edge `0.0044` maxDD `-5.2976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T20:22:29.238146+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11555`

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

- `risk_on_high->unknown_4h` score `7.2691` n `107` status `ready` deltaP `19.763` edge `0.5358` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2691` n `107` status `ready` deltaP `19.763` edge `0.5358` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8157` n `151` status `ready` deltaP `16.0556` edge `0.4471` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.9392` n `107` status `ready` deltaP `3.6712` edge `0.1948` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.9392` n `107` status `ready` deltaP `3.6712` edge `0.1948` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.8084` n `151` status `ready` deltaP `3.0337` edge `0.1935` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.2289` n `59` status `ready` deltaP `1.1367` edge `0.1295` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1391` n `59` status `ready` deltaP `10.4873` edge `0.001` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.1232` n `107` status `ready` deltaP `12.5441` edge `0.0034` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1232` n `107` status `ready` deltaP `12.5441` edge `0.0034` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.1072` n `107` status `ready` deltaP `8.2433` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1072` n `107` status `ready` deltaP `8.2433` edge `0.0033` maxDD `-0.5605`
- `risk_on_high->commodity_24h` score `0.031` n `107` status `ready` deltaP `6.5226` edge `0.0579` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.031` n `107` status `ready` deltaP `6.5226` edge `0.0579` maxDD `-0.5706`
- `risk_on_high->index_4h` score `0.0261` n `107` status `ready` deltaP `19.4111` edge `0.007` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0261` n `107` status `ready` deltaP `19.4111` edge `0.007` maxDD `-3.6448`
- `risk_on_high->equity_1h` score `-0.1605` n `107` status `ready` deltaP `7.7173` edge `0.0109` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1605` n `107` status `ready` deltaP `7.7173` edge `0.0109` maxDD `-2.3009`
- `market_context_high->commodity_1h` score `-0.18` n `151` status `ready` deltaP `6.4768` edge `0.0068` maxDD `-1.5315`
- `news_risk_high->index_1h` score `-0.1841` n `59` status `ready` deltaP `2.8418` edge `-0.0072` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

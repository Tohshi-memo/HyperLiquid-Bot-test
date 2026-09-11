# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T08:52:40.836839+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12372`

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

- `news_risk_high->unknown_1h` score `750.8489` n `59` status `ready` deltaP `-6.5082` edge `62.6563` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `21.9607` n `91` status `ready` deltaP `39.4708` edge `1.5899` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.9607` n `91` status `ready` deltaP `39.4708` edge `1.5899` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.1678` n `172` status `ready` deltaP `35.663` edge `1.4423` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.117` n `172` status `ready` deltaP `34.0278` edge `0.5329` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9173` n `91` status `ready` deltaP `41.3361` edge `0.5047` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9173` n `91` status `ready` deltaP `41.3361` edge `0.5047` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `8.697` n `91` status `ready` deltaP `34.0278` edge `0.4979` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.697` n `91` status `ready` deltaP `34.0278` edge `0.4979` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.5607` n `91` status `ready` deltaP `31.7442` edge `0.5043` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.5607` n `91` status `ready` deltaP `31.7442` edge `0.5043` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.3197` n `91` status `ready` deltaP `25.021` edge `1.1784` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3197` n `91` status `ready` deltaP `25.021` edge `1.1784` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.3839` n `91` status `ready` deltaP `49.8283` edge `0.1207` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3839` n `91` status `ready` deltaP `49.8283` edge `0.1207` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.3061` n `172` status `ready` deltaP `42.6599` edge `0.1138` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.5854` n `91` status `ready` deltaP `34.2603` edge `0.0797` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.5854` n `91` status `ready` deltaP `34.2603` edge `0.0797` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.3861` n `172` status `ready` deltaP `27.4816` edge `0.0983` maxDD `-2.6138`
- `risk_on_high->equity_1h` score `1.6166` n `91` status `ready` deltaP `21.1835` edge `0.0213` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

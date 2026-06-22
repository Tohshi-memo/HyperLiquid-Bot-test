# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T09:37:31.453939+00:00`
- Price records: `672`
- Market context records: `4403`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11123`

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

- `risk_on_high->unknown_4h` score `122.3619` n `48` status `ready` deltaP `2.8455` edge `10.3597` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `122.3619` n `48` status `ready` deltaP `2.8455` edge `10.3597` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.229` n `229` status `ready` deltaP `2.3907` edge `2.7361` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `12.5546` n `220` status `ready` deltaP `5.5349` edge `1.5523` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.2392` n `48` status `ready` deltaP `33.8923` edge `0.0487` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2392` n `48` status `ready` deltaP `33.8923` edge `0.0487` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.982` n `44` status `ready` deltaP `-15.3567` edge `0.5461` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.982` n `44` status `ready` deltaP `-15.3567` edge `0.5461` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.4303` n `48` status `ready` deltaP `20.4268` edge `0.1329` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.4303` n `48` status `ready` deltaP `20.4268` edge `0.1329` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.6977` n `44` status `ready` deltaP `20.4861` edge `0.0049` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6977` n `44` status `ready` deltaP `20.4861` edge `0.0049` maxDD `0.0`
- `risk_on_high->index_24h` score `1.5138` n `44` status `ready` deltaP `23.4375` edge `-0.0301` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.5138` n `44` status `ready` deltaP `23.4375` edge `-0.0301` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.763` n `49` status `ready` deltaP `12.5016` edge `0.0192` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.763` n `49` status `ready` deltaP `12.5016` edge `0.0192` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.4903` n `48` status `ready` deltaP `8.0284` edge `0.0429` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4903` n `48` status `ready` deltaP `8.0284` edge `0.0429` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.4487` n `48` status `ready` deltaP `13.7195` edge `0.005` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.4487` n `48` status `ready` deltaP `13.7195` edge `0.005` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

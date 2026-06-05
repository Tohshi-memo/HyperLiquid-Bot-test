# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T11:07:22.020672+00:00`
- Price records: `672`
- Market context records: `2963`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.1651` n `119` status `ready` deltaP `11.7603` edge `1.7437` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.9787` n `119` status `ready` deltaP `16.9643` edge `0.6816` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.7523` n `119` status `ready` deltaP `17.3246` edge `0.7309` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `7.5443` n `119` status `ready` deltaP `28.853` edge `0.534` maxDD `-3.1465`
- `market_context_high->equity_4h` score `3.4435` n `120` status `ready` deltaP `17.1443` edge `0.2116` maxDD `-0.7819`
- `market_context_high->index_24h` score `3.3264` n `119` status `ready` deltaP `13.6161` edge `0.2845` maxDD `-2.5127`
- `market_context_high->crypto_alt_4h` score `2.9953` n `120` status `ready` deltaP `24.4411` edge `0.5428` maxDD `-30.8239`
- `market_context_high->index_4h` score `0.8341` n `120` status `ready` deltaP `14.6951` edge `0.0878` maxDD `-1.9733`
- `market_context_high->equity_1h` score `0.6374` n `120` status `ready` deltaP `4.6108` edge `0.0576` maxDD `-1.1513`
- `market_context_high->unknown_4h` score `0.4158` n `120` status `ready` deltaP `5.1423` edge `0.1057` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0133` n `120` status `ready` deltaP `4.8703` edge `0.0185` maxDD `-1.2743`
- `market_context_high->crypto_alt_1h` score `-0.1284` n `120` status `ready` deltaP `7.2006` edge `0.1048` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.1686` n `120` status `ready` deltaP `1.8563` edge `0.0043` maxDD `-0.1244`
- `market_context_high->crypto_major_1h` score `-0.2103` n `120` status `ready` deltaP `6.8613` edge `0.0809` maxDD `-9.622`
- `market_context_high->crypto_major_4h` score `-0.4902` n `120` status `ready` deltaP `12.4796` edge `0.3665` maxDD `-33.6701`
- `market_context_high->commodity_1h` score `-0.535` n `120` status `ready` deltaP `-0.8782` edge `-0.0002` maxDD `-3.3365`
- `market_context_high->commodity_4h` score `-0.6545` n `120` status `ready` deltaP `6.0976` edge `0.0435` maxDD `-8.4449`
- `market_context_high->metal_1h` score `-0.7843` n `120` status `ready` deltaP `-1.4721` edge `-0.002` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.8896` n `120` status `ready` deltaP `1.2375` edge `-0.0093` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-0.9922` n `120` status `ready` deltaP `-1.9817` edge `0.0084` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

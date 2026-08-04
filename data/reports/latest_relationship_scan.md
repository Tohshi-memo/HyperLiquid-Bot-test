# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T08:07:56.753229+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `37.2725` n `46` status `ready` deltaP `25.4303` edge `2.9408` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.6771` n `46` status `ready` deltaP `43.4783` edge `0.4506` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9666` n `46` status `ready` deltaP `36.5262` edge `0.4383` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.7401` n `88` status `ready` deltaP `1.6629` edge `0.5668` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.181` n `88` status `ready` deltaP `15.2162` edge `0.0816` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.301` n `88` status `ready` deltaP `17.3226` edge `0.0091` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2325` n `88` status `ready` deltaP `5.6818` edge `0.0231` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.182` n `88` status `ready` deltaP `7.9818` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4663` n `88` status `ready` deltaP `1.5787` edge `-0.0169` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5308` n `88` status `ready` deltaP `-1.4698` edge `-0.0088` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.5598` n `88` status `ready` deltaP `4.7395` edge `0.0201` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9749` n `88` status `ready` deltaP `3.1042` edge `-0.0067` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2647` n `88` status `ready` deltaP `-3.4703` edge `-0.0112` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5557` n `88` status `ready` deltaP `5.4641` edge `-0.0823` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.8079` n `46` status `ready` deltaP `-5.4423` edge `0.0062` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.8491` n `88` status `ready` deltaP `-9.964` edge `-0.0452` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3896` n `88` status `ready` deltaP `2.8988` edge `-0.2571` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6319` n `88` status `ready` deltaP `-12.9491` edge `-0.079` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8818` n `46` status `ready` deltaP `-24.1621` edge `-0.1289` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.606` n `88` status `ready` deltaP `0.6374` edge `-0.3181` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

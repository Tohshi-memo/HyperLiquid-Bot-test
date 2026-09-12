# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T02:37:27.322174+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11257`

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

- `news_risk_high->unknown_1h` score `383.0677` n `82` status `ready` deltaP `-3.4541` edge `31.9875` maxDD `-1.7068`
- `market_context_high->unknown_24h` score `190.4043` n `145` status `ready` deltaP `14.0721` edge `15.7784` maxDD `-0.082`
- `risk_on_high->crypto_alt_24h` score `25.2703` n `91` status `ready` deltaP `43.1166` edge `1.8414` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `25.2703` n `91` status `ready` deltaP `43.1166` edge `1.8414` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `23.218` n `51` status `ready` deltaP `53.4416` edge `1.6686` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.2673` n `145` status `ready` deltaP `37.5766` edge `1.6045` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `15.6959` n `51` status `ready` deltaP `27.0425` edge `1.1765` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `11.3644` n `51` status `ready` deltaP `33.0576` edge `0.7365` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.2463` n `91` status `ready` deltaP `36.9792` edge `0.524` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2463` n `91` status `ready` deltaP `36.9792` edge `0.524` maxDD `0.0`
- `market_context_high->equity_24h` score `8.9319` n `145` status `ready` deltaP `36.9792` edge `0.4978` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9302` n `91` status `ready` deltaP `43.9276` edge `0.4885` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9302` n `91` status `ready` deltaP `43.9276` edge `0.4885` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1153` n `51` status `ready` deltaP `51.0417` edge `0.336` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.946` n `91` status `ready` deltaP `25.021` edge `1.2587` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.946` n `91` status `ready` deltaP `25.021` edge `1.2587` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.8812` n `51` status `ready` deltaP `50.9395` edge `0.3265` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.7991` n `91` status `ready` deltaP `32.0491` edge `0.4388` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.7991` n `91` status `ready` deltaP `32.0491` edge `0.4388` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.2876` n `91` status `ready` deltaP `51.5644` edge `0.1011` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

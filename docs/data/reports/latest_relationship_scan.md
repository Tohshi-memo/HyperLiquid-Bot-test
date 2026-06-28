# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T09:47:53.767471+00:00`
- Price records: `672`
- Market context records: `5027`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10174`

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

- `market_context_high->unknown_1h` score `15.2311` n `93` status `ready` deltaP `3.9679` edge `1.2929` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0129` n `93` status `ready` deltaP `21.4496` edge `0.7103` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.5591` n `93` status `ready` deltaP `17.0994` edge `0.5077` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3639` n `93` status `ready` deltaP `14.7883` edge `0.4878` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.283` n `93` status `ready` deltaP `13.6965` edge `0.1235` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.85` n `93` status `ready` deltaP `8.0371` edge `0.0746` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7685` n `93` status `ready` deltaP `6.1039` edge `0.1151` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.4475` n `93` status `ready` deltaP `3.2734` edge `0.1737` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.388` n `93` status `ready` deltaP `6.553` edge `0.0383` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.189` n `93` status `ready` deltaP `5.2604` edge `0.0914` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0541` n `74` status `ready` deltaP `9.3844` edge `0.0067` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.0973` n `93` status `ready` deltaP `4.1716` edge `0.0402` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3205` n `93` status `ready` deltaP `1.5582` edge `0.0145` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5599` n `93` status `ready` deltaP `2.2117` edge `0.0127` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.8193` n `93` status `ready` deltaP `3.393` edge `-0.0024` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0196` n `93` status `ready` deltaP `-4.3732` edge `-0.0027` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.8216` n `93` status `ready` deltaP `-12.7471` edge `-0.0058` maxDD `-0.5482`
- `market_context_high->unknown_24h` score `-2.6858` n `74` status `ready` deltaP `27.0364` edge `-0.3698` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.782` n `74` status `ready` deltaP `4.8611` edge `0.0282` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.546` n `74` status `ready` deltaP `1.6282` edge `-0.0828` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

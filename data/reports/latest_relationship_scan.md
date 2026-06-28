# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T08:07:32.298747+00:00`
- Price records: `672`
- Market context records: `5020`
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

- `market_context_high->unknown_1h` score `15.4795` n `93` status `ready` deltaP `4.1176` edge `1.3126` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0381` n `93` status `ready` deltaP `21.4496` edge `0.7124` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.7125` n `93` status `ready` deltaP `17.8616` edge `0.5154` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3625` n `93` status `ready` deltaP `14.6358` edge `0.4887` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.3499` n `93` status `ready` deltaP `14.4587` edge `0.124` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8848` n `93` status `ready` deltaP `8.3365` edge `0.0755` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7493` n `93` status `ready` deltaP `5.9542` edge `0.1145` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5113` n `93` status `ready` deltaP `4.0356` edge `0.1768` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3628` n `93` status `ready` deltaP `6.2536` edge `0.0382` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1687` n `93` status `ready` deltaP `5.1107` edge `0.0898` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0425` n `93` status `ready` deltaP `4.7813` edge `0.0407` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.0933` n `74` status `ready` deltaP `8.69` edge `0.0063` maxDD `-1.7626`
- `market_context_high->unknown_24h` score `-0.2635` n `74` status `ready` deltaP `27.21` edge `-0.1691` maxDD `-1.4072`
- `market_context_high->commodity_1h` score `-0.3322` n `93` status `ready` deltaP `1.4085` edge `0.014` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5575` n `93` status `ready` deltaP `2.2117` edge `0.0129` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.8137` n `93` status `ready` deltaP `3.5454` edge `-0.0027` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0006` n `93` status `ready` deltaP `-4.0683` edge `-0.0023` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7833` n `93` status `ready` deltaP `-12.298` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.8874` n `74` status `ready` deltaP `3.6458` edge `0.0228` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.4446` n `74` status `ready` deltaP `2.8434` edge `-0.0779` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

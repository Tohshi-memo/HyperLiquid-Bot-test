# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T21:52:24.966131+00:00`
- Price records: `672`
- Market context records: `4763`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `7.4129` n `130` status `ready` deltaP `12.69` edge `0.5749` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.8852` n `129` status `ready` deltaP `16.2613` edge `0.5864` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.6072` n `115` status `ready` deltaP `13.6654` edge `0.2185` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.1414` n `130` status `ready` deltaP `3.2519` edge `0.0253` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `-0.2874` n `129` status `ready` deltaP `9.3815` edge `0.0378` maxDD `-5.975`
- `market_context_high->equity_4h` score `-0.396` n `129` status `ready` deltaP `8.0131` edge `0.0644` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.4757` n `129` status `ready` deltaP `6.1189` edge `0.0051` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.5585` n `129` status `ready` deltaP `0.8449` edge `0.0004` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.9993` n `130` status `ready` deltaP `0.4906` edge `-0.0098` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.0874` n `130` status `ready` deltaP `-3.3095` edge `-0.0036` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.5249` n `130` status `ready` deltaP `-2.8443` edge `-0.0077` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.3014` n `115` status `ready` deltaP `18.8436` edge `0.0902` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3335` n `130` status `ready` deltaP `-1.6421` edge `-0.0681` maxDD `-14.2761`
- `market_context_high->crypto_major_1h` score `-3.463` n `130` status `ready` deltaP `-1.6007` edge `-0.0902` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-3.7522` n `115` status `ready` deltaP `-14.8747` edge `-0.0203` maxDD `-3.7908`
- `market_context_high->crypto_alt_1h` score `-4.6323` n `130` status `ready` deltaP `-2.4781` edge `-0.077` maxDD `-19.7337`
- `market_context_high->crypto_alt_4h` score `-5.2561` n `129` status `ready` deltaP `3.1575` edge `-0.035` maxDD `-47.4598`
- `market_context_high->index_24h` score `-6.363` n `115` status `ready` deltaP `-8.9388` edge `-0.1105` maxDD `-20.8129`
- `market_context_high->crypto_major_4h` score `-8.1574` n `129` status `ready` deltaP `3.2969` edge `-0.1447` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.3402` n `129` status `ready` deltaP `5.4181` edge `-0.2813` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

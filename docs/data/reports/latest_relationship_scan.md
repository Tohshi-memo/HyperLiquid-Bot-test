# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T17:37:28.841275+00:00`
- Price records: `672`
- Market context records: `5062`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10310`

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

- `market_context_high->unknown_1h` score `13.1335` n `97` status `ready` deltaP `2.8428` edge `1.1256` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0806` n `97` status `ready` deltaP `20.7207` edge `0.7208` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.2364` n `97` status `ready` deltaP `18.4546` edge `0.5186` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.561` n `97` status `ready` deltaP `17.0025` edge `0.5085` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `1.1683` n `97` status `ready` deltaP `8.5483` edge `0.122` maxDD `-3.8637`
- `market_context_high->metal_4h` score `0.9836` n `97` status `ready` deltaP `10.5843` edge `0.1193` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8747` n `97` status `ready` deltaP `8.6302` edge `0.0727` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.7074` n `97` status `ready` deltaP `6.0112` edge `0.1721` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.6379` n `97` status `ready` deltaP `6.5853` edge `0.1016` maxDD `-4.7207`
- `market_context_high->metal_1h` score `0.4555` n `97` status `ready` deltaP `7.5174` edge `0.0375` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.0234` n `97` status `ready` deltaP `5.8147` edge `0.0393` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1056` n `74` status `ready` deltaP `8.2442` edge `0.0077` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.2743` n `97` status `ready` deltaP `1.9955` edge `0.0126` maxDD `-0.552`
- `market_context_high->commodity_1h` score `-0.5678` n `97` status `ready` deltaP `0.6991` edge `0.014` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8589` n `97` status `ready` deltaP `7.1426` edge `0.0057` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.9417` n `97` status `ready` deltaP `-3.2232` edge `-0.0003` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4699` n `97` status `ready` deltaP `-8.5792` edge `-0.0043` maxDD `-0.5464`
- `market_context_high->unknown_24h` score `-3.0518` n `74` status `ready` deltaP `27.0364` edge `-0.4003` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.726` n `74` status `ready` deltaP `4.664` edge `0.0367` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.0036` n `74` status `ready` deltaP `1.6516` edge `-0.0702` maxDD `-24.3277`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

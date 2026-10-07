# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T11:37:34.347423+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_4h` score `36.7785` n `92` status `ready` deltaP `-5.3154` edge `3.1542` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.4898` n `62` status `ready` deltaP `36.2953` edge `0.6525` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.2164` n `62` status `ready` deltaP `23.6969` edge `0.5778` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.6682` n `62` status `ready` deltaP `26.5625` edge `0.1286` maxDD `0.0`
- `news_risk_high->index_4h` score `2.9513` n `62` status `ready` deltaP `32.917` edge `0.0527` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.9415` n `62` status `ready` deltaP `7.4373` edge `0.2055` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.3065` n `62` status `ready` deltaP `8.9772` edge `0.1679` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.1399` n `62` status `ready` deltaP `18.8435` edge `0.1125` maxDD `-2.7837`
- `news_risk_high->index_1h` score `2.0103` n `62` status `ready` deltaP `25.3236` edge `0.0137` maxDD `-0.1997`
- `market_context_high->crypto_major_4h` score `1.9645` n `92` status `ready` deltaP `13.925` edge `0.1673` maxDD `-4.047`
- `news_risk_high->metal_4h` score `1.4476` n `62` status `ready` deltaP `20.4858` edge `0.0906` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.2684` n `92` status `ready` deltaP `4.6648` edge `0.4289` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `1.2054` n `62` status `ready` deltaP `3.6073` edge `0.1283` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.8113` n `92` status `ready` deltaP `13.2648` edge `0.0034` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.65` n `92` status `ready` deltaP `17.272` edge `0.0145` maxDD `-0.372`
- `market_context_high->metal_24h` score `0.5132` n `92` status `ready` deltaP `17.3384` edge `0.0987` maxDD `-3.5466`
- `news_risk_high->commodity_24h` score `0.3016` n `62` status `ready` deltaP `25.6329` edge `0.0244` maxDD `-8.196`
- `news_risk_high->metal_1h` score `0.188` n `62` status `ready` deltaP `7.3498` edge `0.0085` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.0868` n `92` status `ready` deltaP `9.6785` edge `0.0355` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `0.0117` n `92` status `ready` deltaP `4.7969` edge `0.0066` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

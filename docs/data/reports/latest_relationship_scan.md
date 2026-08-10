# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T00:38:03.887070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.3379` n `153` status `ready` deltaP `15.493` edge `0.0755` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7861` n `165` status `ready` deltaP `10.3357` edge `0.0309` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.4269` n `132` status `ready` deltaP `18.1186` edge `0.0206` maxDD `-1.9329`
- `market_context_high->metal_24h` score `-0.166` n `132` status `ready` deltaP `0.0789` edge `0.0599` maxDD `-2.2743`
- `market_context_high->fx_1h` score `-0.2887` n `165` status `ready` deltaP `2.2854` edge `-0.0027` maxDD `-0.9639`
- `market_context_high->equity_24h` score `-0.3645` n `132` status `ready` deltaP `1.8466` edge `0.2633` maxDD `-21.1456`
- `market_context_high->index_24h` score `-0.4769` n `132` status `ready` deltaP `2.4148` edge `0.0973` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5861` n `165` status `ready` deltaP `-3.2752` edge `-0.0056` maxDD `-0.8168`
- `market_context_high->fx_4h` score `-0.6319` n `153` status `ready` deltaP `3.5948` edge `-0.0013` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.7382` n `165` status `ready` deltaP `-4.3231` edge `-0.0094` maxDD `-1.5133`
- `market_context_high->index_4h` score `-0.7393` n `153` status `ready` deltaP `-3.5051` edge `-0.0109` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-1.1743` n `165` status `ready` deltaP `-1.5196` edge `-0.0007` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.3149` n `153` status `ready` deltaP `-4.2653` edge `-0.0251` maxDD `-3.8697`
- `market_context_high->crypto_alt_1h` score `-1.6089` n `165` status `ready` deltaP `-9.1571` edge `-0.0431` maxDD `-5.5029`
- `market_context_high->equity_4h` score `-2.9251` n `153` status `ready` deltaP `-4.3739` edge `-0.0767` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.757` n `165` status `ready` deltaP `-11.0406` edge `-0.0661` maxDD `-10.5372`
- `market_context_high->crypto_major_24h` score `-4.475` n `132` status `ready` deltaP `0.0315` edge `-0.1237` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.6274` n `132` status `ready` deltaP `-12.4211` edge `-0.1585` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.9735` n `153` status `ready` deltaP `-10.5632` edge `-0.1413` maxDD `-9.5522`
- `market_context_high->unknown_1h` score `-7.5265` n `165` status `ready` deltaP `-4.5455` edge `-0.5512` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

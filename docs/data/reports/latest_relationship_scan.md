# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T09:07:33.723138+00:00`
- Price records: `672`
- Market context records: `7012`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11541`

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

- `market_context_high->fx_1h` score `-0.2764` n `230` status `ready` deltaP `1.8107` edge `0.001` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.3242` n `217` status `ready` deltaP `-5.6339` edge `0.451` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.5138` n `230` status `ready` deltaP `1.8172` edge `0.0315` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6269` n `230` status `ready` deltaP `1.3265` edge `0.0019` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6314` n `230` status `ready` deltaP `-0.8188` edge `0.0013` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.9905` n `230` status `ready` deltaP `3.7347` edge `0.0278` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-1.0056` n `230` status `ready` deltaP `10.688` edge `0.0062` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.2244` n `230` status `ready` deltaP `-2.2025` edge `-0.0152` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3121` n `230` status `ready` deltaP `-2.0307` edge `-0.0057` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6831` n `230` status `ready` deltaP `-4.2908` edge `-0.0382` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7591` n `230` status `ready` deltaP `8.0965` edge `-0.0096` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.7689` n `230` status `ready` deltaP `4.3556` edge `-0.0004` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8571` n `230` status `ready` deltaP `7.3104` edge `0.0115` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.5191` n `230` status `ready` deltaP `-6.2355` edge `0.0682` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6855` n `230` status `ready` deltaP `1.8969` edge `0.0216` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.191` n `217` status `ready` deltaP `-4.7355` edge `-0.0868` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.2509` n `217` status `ready` deltaP `-6.0412` edge `-0.0159` maxDD `-5.1787`
- `market_context_high->crypto_major_4h` score `-4.8367` n `230` status `ready` deltaP `1.8743` edge `0.0129` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-11.2861` n `230` status `ready` deltaP `5.3406` edge `-0.0544` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.3611` n `217` status `ready` deltaP `-9.2694` edge `-0.0547` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

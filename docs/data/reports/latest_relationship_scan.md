# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T05:07:28.700479+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `29.8787` n `135` status `ready` deltaP `-16.8` edge `2.8473` maxDD `-9.6329`
- `market_context_high->commodity_4h` score `0.7094` n `169` status `ready` deltaP `10.7662` edge `0.0588` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6741` n `180` status `ready` deltaP `9.3114` edge `0.0284` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5865` n `135` status `ready` deltaP `18.489` edge `0.0327` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.5714` n `30` status `ready` deltaP `16.1078` edge `-0.0032` maxDD `-0.808`
- `risk_on_and_context->index_1h` score `0.5714` n `30` status `ready` deltaP `16.1078` edge `-0.0032` maxDD `-0.808`
- `risk_on_high->commodity_1h` score `0.4671` n `30` status `ready` deltaP `7.6447` edge `0.0322` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `0.4671` n `30` status `ready` deltaP `7.6447` edge `0.0322` maxDD `-0.1957`
- `market_context_high->commodity_24h` score `-0.1766` n `135` status `ready` deltaP `11.2444` edge `0.1462` maxDD `-13.5047`
- `market_context_high->fx_4h` score `-0.2193` n `169` status `ready` deltaP `4.2077` edge `0.0043` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.2747` n `180` status `ready` deltaP `1.6866` edge `-0.0013` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.8412` n `180` status `ready` deltaP `-6.67` edge `-0.0046` maxDD `-1.0359`
- `risk_on_high->crypto_major_1h` score `-0.8824` n `30` status `ready` deltaP `4.2715` edge `-0.072` maxDD `-3.5689`
- `risk_on_and_context->crypto_major_1h` score `-0.8824` n `30` status `ready` deltaP `4.2715` edge `-0.072` maxDD `-3.5689`
- `market_context_high->index_4h` score `-0.9766` n `169` status `ready` deltaP `-3.9412` edge `-0.0095` maxDD `-1.4875`
- `risk_on_high->fx_1h` score `-1.0747` n `30` status `ready` deltaP `-8.3134` edge `-0.009` maxDD `-0.3443`
- `risk_on_and_context->fx_1h` score `-1.0747` n `30` status `ready` deltaP `-8.3134` edge `-0.009` maxDD `-0.3443`
- `risk_on_high->equity_1h` score `-1.0909` n `30` status `ready` deltaP `1.3174` edge `-0.0701` maxDD `-3.9505`
- `risk_on_and_context->equity_1h` score `-1.0909` n `30` status `ready` deltaP `1.3174` edge `-0.0701` maxDD `-3.9505`
- `market_context_high->metal_1h` score `-1.3742` n `180` status `ready` deltaP `-6.0312` edge `-0.0107` maxDD `-2.0884`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

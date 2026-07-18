# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T03:37:22.760895+00:00`
- Price records: `672`
- Market context records: `7098`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.4246` n `157` status `ready` deltaP `16.5799` edge `0.0139` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1671` n `157` status `ready` deltaP `4.2135` edge `0.0031` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.1849` n `157` status `ready` deltaP `-0.0219` edge `0.0406` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.4516` n `157` status `ready` deltaP `0.3948` edge `0.0259` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4861` n `157` status `ready` deltaP `0.8` edge `-0.0057` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6109` n `157` status `ready` deltaP `3.2419` edge `0.0353` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8546` n `157` status `ready` deltaP `-4.2488` edge `-0.0196` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3681` n `157` status `ready` deltaP `-4.3149` edge `-0.0431` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5014` n `157` status `ready` deltaP `-6.4705` edge `-0.0052` maxDD `-2.1427`
- `market_context_high->unknown_4h` score `-1.6307` n `157` status `ready` deltaP `-7.3297` edge `0.0` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.1103` n `157` status `ready` deltaP `2.0739` edge `-0.0421` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.406` n `157` status `ready` deltaP `0.5311` edge `-0.0421` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-3.026` n `157` status `ready` deltaP `3.9605` edge `0.0141` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.1547` n `157` status `ready` deltaP `-6.6768` edge `-0.0875` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.1848` n `157` status `ready` deltaP `-1.271` edge `-0.0213` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.2737` n `157` status `ready` deltaP `-8.1343` edge `-0.0192` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.3549` n `157` status `ready` deltaP `-8.1133` edge `-0.0105` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.502` n `157` status `ready` deltaP `0.3514` edge `-0.2053` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.8329` n `157` status `ready` deltaP `-23.3701` edge `-0.0656` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.0257` n `157` status `ready` deltaP `-24.9956` edge `-0.1368` maxDD `-43.2296`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

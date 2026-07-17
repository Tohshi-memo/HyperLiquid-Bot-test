# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T19:37:14.521344+00:00`
- Price records: `672`
- Market context records: `7061`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.5902` n `188` status `ready` deltaP `16.1974` edge `0.0112` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2183` n `188` status `ready` deltaP `3.7234` edge `0.0021` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.2936` n `188` status `ready` deltaP `2.1595` edge `0.0344` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5554` n `188` status `ready` deltaP `4.3541` edge `0.035` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-0.6066` n `188` status `ready` deltaP `-0.8632` edge `0.0247` maxDD `-1.8929`
- `market_context_high->metal_1h` score `-0.7652` n `188` status `ready` deltaP `-2.9877` edge `-0.0014` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7971` n `188` status `ready` deltaP `-1.0766` edge `-0.0039` maxDD `-2.2895`
- `market_context_high->unknown_4h` score `-0.9771` n `188` status `ready` deltaP `-5.4424` edge `0.1183` maxDD `-4.742`
- `market_context_high->commodity_1h` score `-1.3456` n `188` status `ready` deltaP `-4.7554` edge `-0.0188` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.6383` n `188` status `ready` deltaP `-7.3949` edge `-0.0447` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.9129` n `188` status `ready` deltaP `3.8763` edge `-0.0288` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.2909` n `188` status `ready` deltaP `0.9633` edge `-0.0018` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.3214` n `188` status `ready` deltaP `0.853` edge `-0.0334` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4243` n `188` status `ready` deltaP `-2.2718` edge `-0.056` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.8149` n `188` status `ready` deltaP `1.2974` edge `0.009` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.9651` n `188` status `ready` deltaP `3.4964` edge `0.025` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.5243` n `188` status `ready` deltaP `0.0332` edge `-0.0112` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-3.7394` n `188` status `ready` deltaP `-14.7348` edge `0.1335` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.8942` n `188` status `ready` deltaP `4.1191` edge `-0.1525` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.3847` n `188` status `ready` deltaP `-19.7547` edge `-0.091` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

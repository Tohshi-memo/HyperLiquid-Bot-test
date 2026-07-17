# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T16:52:26.638911+00:00`
- Price records: `672`
- Market context records: `7048`
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

- `market_context_high->fx_4h` score `0.3419` n `199` status `ready` deltaP `14.4342` edge `0.0106` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2922` n `199` status `ready` deltaP `2.8601` edge `0.0017` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.5392` n `199` status `ready` deltaP `1.4699` edge `0.0317` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.6029` n `199` status `ready` deltaP `3.726` edge `0.0331` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.7685` n `199` status `ready` deltaP `-3.149` edge `-0.0159` maxDD `-1.9306`
- `market_context_high->index_1h` score `-0.7821` n `199` status `ready` deltaP `-0.8922` edge `-0.0032` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8291` n `199` status `ready` deltaP `-4.0675` edge `-0.0024` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-0.8933` n `199` status `ready` deltaP `-2.3787` edge `0.0148` maxDD `-2.204`
- `market_context_high->unknown_4h` score `-1.4201` n `199` status `ready` deltaP `-5.7062` edge `0.1014` maxDD `-6.203`
- `market_context_high->equity_1h` score `-1.9135` n `199` status `ready` deltaP `3.5341` edge `-0.0266` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.0941` n `199` status `ready` deltaP `3.7566` edge `0.0048` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.1419` n `199` status `ready` deltaP `3.1813` edge `-0.0259` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.2412` n `198` status `ready` deltaP `-0.5524` edge `-0.0522` maxDD `-4.4704`
- `market_context_high->commodity_4h` score `-2.2445` n `199` status `ready` deltaP `-5.0106` edge `-0.0376` maxDD `-2.9494`
- `market_context_high->crypto_alt_4h` score `-2.5764` n `199` status `ready` deltaP `2.6903` edge `0.0303` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.7874` n `199` status `ready` deltaP `4.3334` edge `0.0422` maxDD `-24.6094`
- `market_context_high->unknown_24h` score `-2.9399` n `198` status `ready` deltaP `-11.8845` edge `0.2143` maxDD `-23.2919`
- `market_context_high->fx_24h` score `-3.5554` n `198` status `ready` deltaP `-0.5051` edge `-0.0102` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.6245` n `199` status `ready` deltaP `3.441` edge `-0.1134` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.9874` n `198` status `ready` deltaP `-16.935` edge `-0.0781` maxDD `-44.303`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

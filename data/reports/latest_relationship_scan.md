# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T22:37:28.652502+00:00`
- Price records: `672`
- Market context records: `7076`
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

- `market_context_high->fx_4h` score `0.7582` n `176` status `ready` deltaP `18.0571` edge `0.0128` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.0465` n `176` status `ready` deltaP `1.1976` edge `0.044` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.0951` n `176` status `ready` deltaP `5.1443` edge `0.0029` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3835` n `176` status `ready` deltaP `1.0751` edge `0.0301` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.5551` n `176` status `ready` deltaP `-0.1123` edge `-0.0043` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6249` n `176` status `ready` deltaP `3.2288` edge `0.0336` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8795` n `176` status `ready` deltaP `-4.6985` edge `-0.0198` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-1.1413` n `176` status `ready` deltaP `-5.8897` edge `0.1076` maxDD `-4.742`
- `market_context_high->metal_1h` score `-1.3683` n `176` status `ready` deltaP `-5.0456` edge `-0.0036` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.6663` n `176` status `ready` deltaP `-8.2733` edge `-0.0466` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.9011` n `176` status `ready` deltaP `4.2528` edge `-0.0298` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2129` n `176` status `ready` deltaP `3.1042` edge `-0.0345` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4873` n `176` status `ready` deltaP `-3.0145` edge `-0.0563` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.0309` n `176` status `ready` deltaP `-0.4712` edge `-0.0069` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.13` n `176` status `ready` deltaP `2.051` edge `0.0135` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7248` n `176` status `ready` deltaP `-2.0833` edge `-0.0138` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.7317` n `176` status `ready` deltaP `-1.178` edge `-0.0048` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-4.6927` n `176` status `ready` deltaP `-17.6926` edge `0.031` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9848` n `176` status `ready` deltaP `3.5615` edge `-0.1604` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.5746` n `176` status `ready` deltaP `-22.3485` edge `-0.1078` maxDD `-44.2873`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

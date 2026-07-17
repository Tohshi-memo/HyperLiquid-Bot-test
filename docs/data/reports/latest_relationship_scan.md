# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T23:52:29.055084+00:00`
- Price records: `672`
- Market context records: `7082`
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

- `market_context_high->fx_4h` score `0.7425` n `171` status `ready` deltaP `17.756` edge `0.0135` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.0555` n `171` status `ready` deltaP `0.6198` edge `0.0471` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1078` n `171` status `ready` deltaP `4.9848` edge `0.0029` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3944` n `171` status `ready` deltaP `0.9849` edge `0.0293` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4561` n `171` status `ready` deltaP `1.1669` edge `-0.0043` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6325` n `171` status `ready` deltaP `3.0527` edge `0.0338` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.9082` n `171` status `ready` deltaP `-5.1905` edge `-0.0202` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4003` n `171` status `ready` deltaP `-5.4015` edge `-0.0039` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.5648` n `171` status `ready` deltaP `-7.5569` edge `-0.0467` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.9399` n `171` status `ready` deltaP `3.9272` edge `-0.0326` maxDD `-14.716`
- `market_context_high->unknown_4h` score `-2.0365` n `171` status `ready` deltaP `-7.4954` edge `0.0437` maxDD `-4.742`
- `market_context_high->index_4h` score `-2.1467` n `171` status `ready` deltaP `4.4831` edge `-0.0352` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.575` n `171` status `ready` deltaP `-3.6001` edge `-0.0597` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-3.0282` n `171` status `ready` deltaP `3.3938` edge `0.0176` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.0303` n `171` status `ready` deltaP `-0.2951` edge `-0.008` maxDD `-22.2831`
- `market_context_high->metal_4h` score `-3.8021` n `171` status `ready` deltaP `-1.9077` edge `-0.0058` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.8562` n `171` status `ready` deltaP `-3.5453` edge `-0.015` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-5.2273` n `171` status `ready` deltaP `-19.8282` edge `-0.0233` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-8.0414` n `171` status `ready` deltaP `3.6434` edge `-0.1682` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.4405` n `171` status `ready` deltaP `-23.0172` edge `-0.1149` maxDD `-44.1352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

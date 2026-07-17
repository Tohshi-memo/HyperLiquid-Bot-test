# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T23:37:27.764259+00:00`
- Price records: `672`
- Market context records: `7081`
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

- `market_context_high->fx_4h` score `0.7465` n `172` status `ready` deltaP `17.8212` edge `0.0134` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.0498` n `172` status `ready` deltaP `0.7659` edge `0.0466` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.0854` n `172` status `ready` deltaP `5.25` edge `0.003` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.4041` n `172` status `ready` deltaP `0.8286` edge `0.0291` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4697` n `172` status `ready` deltaP `0.9051` edge `-0.0043` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6417` n `172` status `ready` deltaP `2.8896` edge `0.0337` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8995` n `172` status `ready` deltaP `-5.0376` edge `-0.0201` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.3703` n `172` status `ready` deltaP `-5.0411` edge `-0.0038` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.5734` n `172` status `ready` deltaP `-7.707` edge `-0.0468` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.8325` n `172` status `ready` deltaP `-7.1044` edge `0.0581` maxDD `-4.742`
- `market_context_high->equity_1h` score `-1.9266` n `172` status `ready` deltaP `4.0767` edge `-0.0319` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.1598` n `172` status `ready` deltaP `4.2009` edge `-0.035` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.5469` n `172` status `ready` deltaP `-3.3995` edge `-0.0587` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.0134` n `172` status `ready` deltaP `-0.1347` edge `-0.0069` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.048` n `172` status `ready` deltaP `3.0878` edge `0.0171` maxDD `-24.6094`
- `market_context_high->metal_4h` score `-3.7673` n `172` status `ready` deltaP `-1.5031` edge `-0.0056` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.8274` n `172` status `ready` deltaP `-3.2461` edge `-0.0146` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-5.1161` n `172` status `ready` deltaP `-19.3557` edge `-0.0122` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-8.0192` n `172` status `ready` deltaP `3.8003` edge `-0.1664` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.465` n `172` status `ready` deltaP `-22.8844` edge `-0.1134` maxDD `-44.1564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T18:37:26.796157+00:00`
- Price records: `672`
- Market context records: `7057`
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

- `market_context_high->fx_4h` score `0.5317` n `192` status `ready` deltaP `15.5107` edge `0.0109` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2422` n `192` status `ready` deltaP `3.4244` edge `0.0021` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3409` n `192` status `ready` deltaP `1.6997` edge `0.0314` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5912` n `192` status `ready` deltaP `4.0107` edge `0.0327` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-0.7697` n `192` status `ready` deltaP `-1.8494` edge `0.0193` maxDD `-2.0222`
- `market_context_high->metal_1h` score `-0.7719` n `192` status `ready` deltaP `-3.0876` edge `-0.0016` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.8253` n `192` status `ready` deltaP `-1.6031` edge `-0.004` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8602` n `192` status `ready` deltaP `-4.6282` edge `-0.0178` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-1.072` n `192` status `ready` deltaP `-5.564` edge `0.1112` maxDD `-4.742`
- `market_context_high->equity_1h` score `-1.9838` n `192` status `ready` deltaP `2.8568` edge `-0.0311` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.2125` n `192` status `ready` deltaP `2.185` edge `0.0001` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.2863` n `192` status `ready` deltaP `1.2576` edge `-0.0316` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.3472` n `192` status `ready` deltaP `-1.5625` edge `-0.0543` maxDD `-4.4704`
- `market_context_high->commodity_4h` score `-2.4386` n `192` status `ready` deltaP `-6.7327` edge `-0.0423` maxDD `-2.9494`
- `market_context_high->crypto_alt_4h` score `-2.683` n `192` status `ready` deltaP `2.3501` edge `0.0189` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.8582` n `192` status `ready` deltaP `4.4716` edge `0.0322` maxDD `-24.6094`
- `market_context_high->unknown_24h` score `-3.4402` n `192` status `ready` deltaP `-13.5416` edge `0.1639` maxDD `-23.5076`
- `market_context_high->fx_24h` score `-3.4884` n `192` status `ready` deltaP `0.3472` edge `-0.0103` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.8469` n `192` status `ready` deltaP `3.7094` edge `-0.1437` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.2105` n `192` status `ready` deltaP `-18.4027` edge `-0.0855` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

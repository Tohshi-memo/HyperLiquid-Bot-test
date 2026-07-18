# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T09:22:29.715122+00:00`
- Price records: `672`
- Market context records: `7124`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11667`

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

- `market_context_high->fx_4h` score `0.4029` n `143` status `ready` deltaP `16.0584` edge `0.0146` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0595` n `151` status `ready` deltaP `5.2028` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.323` n `151` status `ready` deltaP `-1.6735` edge `0.0401` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.5472` n `151` status `ready` deltaP `-0.1814` edge `0.0254` maxDD `-5.2145`
- `market_context_high->index_1h` score `-0.7128` n `151` status `ready` deltaP `1.8103` edge `-0.005` maxDD `-2.3175`
- `market_context_high->commodity_1h` score `-0.8492` n `151` status `ready` deltaP `-4.1371` edge `-0.0192` maxDD `-1.9668`
- `market_context_high->crypto_major_1h` score `-0.9465` n `151` status `ready` deltaP `3.1298` edge `0.0355` maxDD `-7.1523`
- `market_context_high->commodity_4h` score `-1.4413` n `143` status `ready` deltaP `-5.5421` edge `-0.0443` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.4664` n `151` status `ready` deltaP `-6.0505` edge `-0.0053` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.4777` n `143` status `ready` deltaP `-6.1573` edge `0.0118` maxDD `-4.4825`
- `market_context_high->crypto_major_4h` score `-3.0706` n `143` status `ready` deltaP `3.7929` edge `0.0095` maxDD `-24.6094`
- `market_context_high->equity_1h` score `-3.2466` n `151` status `ready` deltaP `2.4953` edge `-0.044` maxDD `-14.7882`
- `market_context_high->commodity_24h` score `-3.905` n `143` status `ready` deltaP `-10.3559` edge `-0.1255` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.1802` n `143` status `ready` deltaP `-4.1319` edge `-0.0509` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.5171` n `143` status `ready` deltaP `-10.0653` edge `-0.0128` maxDD `-5.3886`
- `market_context_high->crypto_alt_4h` score `-4.722` n `143` status `ready` deltaP `0.3954` edge `-0.0176` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.7484` n `143` status `ready` deltaP `-13.4385` edge `-0.0234` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-9.5119` n `143` status `ready` deltaP `-28.1966` edge `-0.09` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.7793` n `143` status `ready` deltaP `-2.1502` edge `-0.2469` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7595` n `143` status `ready` deltaP `-28.2403` edge `-0.1677` maxDD `-41.9194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T08:22:30.023100+00:00`
- Price records: `672`
- Market context records: `7119`
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

- `market_context_high->fx_4h` score `0.3521` n `146` status `ready` deltaP `15.1562` edge `0.0141` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0754` n `150` status `ready` deltaP `4.8982` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2786` n `150` status `ready` deltaP `-1.3733` edge `0.0418` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.4014` n `150` status `ready` deltaP `1.0339` edge `0.0304` maxDD `-4.7674`
- `market_context_high->index_1h` score `-0.544` n `150` status `ready` deltaP `0.4231` edge `-0.0061` maxDD `-2.3175`
- `market_context_high->crypto_major_1h` score `-0.8079` n `150` status `ready` deltaP `4.3673` edge `0.0388` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8692` n `150` status `ready` deltaP `-4.477` edge `-0.0195` maxDD `-1.9668`
- `market_context_high->commodity_4h` score `-1.3834` n `146` status `ready` deltaP `-4.5794` edge `-0.0433` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.4153` n `150` status `ready` deltaP `-5.4272` edge `-0.0052` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5487` n `146` status `ready` deltaP `-6.8326` edge `0.0072` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0642` n `150` status `ready` deltaP `3.1716` edge `-0.0435` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0076` n `146` status `ready` deltaP `4.4938` edge `0.0129` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.734` n `146` status `ready` deltaP `-9.5082` edge `-0.1169` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.0586` n `146` status `ready` deltaP `-2.8817` edge `-0.0491` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.4748` n `146` status `ready` deltaP `-9.564` edge `-0.0123` maxDD `-5.414`
- `market_context_high->crypto_alt_4h` score `-4.6296` n `146` status `ready` deltaP `0.9209` edge `-0.0134` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.6845` n `146` status `ready` deltaP `-12.714` edge `-0.0229` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-9.4241` n `146` status `ready` deltaP `-27.8039` edge `-0.0853` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.6686` n `146` status `ready` deltaP `-2.0423` edge `-0.2384` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.8384` n `146` status `ready` deltaP `-27.7183` edge `-0.1614` maxDD `-42.2274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T07:52:26.578372+00:00`
- Price records: `672`
- Market context records: `7117`
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
- `market_context_high->fx_1h` score `-0.1007` n `148` status `ready` deltaP `4.4263` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2032` n `148` status `ready` deltaP `-0.9104` edge `0.045` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.5778` n `148` status `ready` deltaP `-0.1659` edge `-0.0065` maxDD `-2.3175`
- `market_context_high->crypto_alt_1h` score `-0.6606` n `148` status `ready` deltaP `0.526` edge `0.0302` maxDD `-4.7674`
- `market_context_high->crypto_major_1h` score `-0.8653` n `148` status `ready` deltaP `3.7547` edge `0.0381` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8668` n `148` status `ready` deltaP `-4.4951` edge `-0.0195` maxDD `-1.9332`
- `market_context_high->commodity_4h` score `-1.3827` n `146` status `ready` deltaP `-4.5794` edge `-0.0432` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.4737` n `148` status `ready` deltaP `-6.0973` edge `-0.0056` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5471` n `146` status `ready` deltaP `-6.8326` edge `0.0074` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0762` n `148` status `ready` deltaP `3.1356` edge `-0.0448` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0305` n `146` status `ready` deltaP `4.1889` edge `0.012` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.7184` n `146` status `ready` deltaP `-9.5082` edge `-0.1156` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.0708` n `146` status `ready` deltaP `-3.0341` edge `-0.0491` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.4492` n `146` status `ready` deltaP `-9.2591` edge `-0.0122` maxDD `-5.414`
- `market_context_high->crypto_alt_4h` score `-4.6708` n `146` status `ready` deltaP `0.616` edge `-0.0148` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.6833` n `146` status `ready` deltaP `-12.714` edge `-0.0228` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-9.3994` n `146` status `ready` deltaP `-27.6303` edge `-0.0844` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.688` n `146` status `ready` deltaP `-2.1947` edge `-0.239` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.795` n `146` status `ready` deltaP `-27.3711` edge `-0.1601` maxDD `-42.2274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

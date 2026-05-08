# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T08:37:11.846765+00:00`
- Price records: `630`
- Market context records: `737`
- Flow alert records: `2081`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `12.4841` n `146` status `ready` deltaP `29.7958` edge `0.8751` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5545` n `146` status `ready` deltaP `7.7421` edge `0.4994` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.0154` n `146` status `ready` deltaP `0.9744` edge `0.1943` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.3057` n `153` status `ready` deltaP `5.8727` edge `0.0088` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.4002` n `157` status `ready` deltaP `3.2932` edge `0.0025` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5899` n `157` status `ready` deltaP `1.4684` edge `0.0385` maxDD `-3.7959`
- `market_context_high->equity_24h` score `-0.6937` n `146` status `ready` deltaP `-0.6952` edge `0.2073` maxDD `-10.5047`
- `market_context_high->index_1h` score `-0.8824` n `157` status `ready` deltaP `1.1725` edge `0.004` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.0449` n `157` status `ready` deltaP `-0.7568` edge `-0.001` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0932` n `157` status `ready` deltaP `5.4079` edge `-0.0039` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4773` n `157` status `ready` deltaP `3.9539` edge `-0.018` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-1.5705` n `153` status `ready` deltaP `17.3287` edge `0.1242` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.5879` n `157` status `ready` deltaP `-4.9429` edge `-0.0222` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.8091` n `153` status `ready` deltaP `1.4272` edge `-0.008` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1687` n `153` status `ready` deltaP `2.1822` edge `0.0617` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6816` n `153` status `ready` deltaP `-1.5236` edge `0.0019` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.1446` n `157` status `ready` deltaP `-3.8431` edge `-0.0405` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6626` n `153` status `ready` deltaP `-5.5234` edge `0.0817` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.8515` n `153` status `ready` deltaP `4.7646` edge `-0.1649` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.3268` n `146` status `ready` deltaP `-15.0065` edge `-0.0657` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

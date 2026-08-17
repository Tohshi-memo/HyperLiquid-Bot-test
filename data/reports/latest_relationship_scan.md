# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T04:07:26.301477+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `market_context_high->commodity_24h` score `3.9792` n `69` status `ready` deltaP `34.8732` edge `0.134` maxDD `-0.4576`
- `market_context_high->equity_24h` score `1.6396` n `69` status `ready` deltaP `16.1307` edge `0.05` maxDD `-0.6726`
- `market_context_high->index_24h` score `1.4721` n `69` status `ready` deltaP `21.7014` edge `-0.022` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `1.4398` n `69` status `ready` deltaP `2.0607` edge `0.2439` maxDD `-5.6792`
- `market_context_high->commodity_4h` score `0.738` n `104` status `ready` deltaP `12.9925` edge `0.0567` maxDD `-0.8962`
- `market_context_high->metal_4h` score `-0.1947` n `104` status `ready` deltaP `16.3345` edge `0.0156` maxDD `-4.5909`
- `market_context_high->commodity_1h` score `-0.298` n `112` status `ready` deltaP `-0.1604` edge `0.009` maxDD `-1.0243`
- `market_context_high->fx_1h` score `-0.3466` n `112` status `ready` deltaP `-0.8982` edge `-0.0014` maxDD `-0.2968`
- `market_context_high->crypto_major_4h` score `-0.5714` n `104` status `ready` deltaP `3.037` edge `0.0273` maxDD `-4.6638`
- `market_context_high->metal_1h` score `-0.5915` n `112` status `ready` deltaP `2.9673` edge `0.0025` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.7781` n `104` status `ready` deltaP `-4.667` edge `-0.0071` maxDD `-0.59`
- `market_context_high->index_1h` score `-0.878` n `112` status `ready` deltaP `-3.0154` edge `-0.0009` maxDD `-0.5064`
- `market_context_high->equity_1h` score `-1.0517` n `112` status `ready` deltaP `-4.6674` edge `-0.0206` maxDD `-3.3165`
- `market_context_high->crypto_alt_1h` score `-1.0886` n `112` status `ready` deltaP `-4.3199` edge `-0.0098` maxDD `-4.4101`
- `market_context_high->crypto_major_1h` score `-1.7128` n `112` status `ready` deltaP `-3.7265` edge `-0.0175` maxDD `-4.0312`
- `market_context_high->index_4h` score `-1.7915` n `104` status `ready` deltaP `-9.6154` edge `-0.0043` maxDD `-0.8045`
- `market_context_high->fx_24h` score `-3.146` n `69` status `ready` deltaP `-30.1027` edge `-0.0419` maxDD `-1.8596`
- `market_context_high->equity_4h` score `-3.2984` n `104` status `ready` deltaP `-17.3663` edge `-0.1264` maxDD `-8.1221`
- `market_context_high->crypto_alt_4h` score `-3.5126` n `104` status `ready` deltaP `-7.5867` edge `-0.0316` maxDD `-16.786`
- `market_context_high->metal_24h` score `-5.4916` n `69` status `ready` deltaP `-23.196` edge `-0.0518` maxDD `-7.0954`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

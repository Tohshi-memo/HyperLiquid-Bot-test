# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T01:37:19.601590+00:00`
- Price records: `672`
- Market context records: `1688`
- Flow alert records: `6766`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `7.5211` n `147` status `ready` deltaP `26.4541` edge `0.693` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.4608` n `192` status `ready` deltaP `23.9076` edge `0.5621` maxDD `-16.3135`
- `market_context_high->unknown_24h` score `4.8214` n `147` status `ready` deltaP `16.443` edge `0.8242` maxDD `-35.8966`
- `market_context_high->index_24h` score `3.8799` n `147` status `ready` deltaP `17.8389` edge `0.3422` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.8254` n `192` status `ready` deltaP `21.4304` edge `0.4468` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.9259` n `192` status `ready` deltaP `15.7012` edge `0.2486` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9005` n `147` status `ready` deltaP `16.8479` edge `0.5359` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.5764` n `203` status `ready` deltaP `5.8199` edge `0.1116` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.3827` n `147` status `ready` deltaP `24.6299` edge `1.0486` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.2002` n `192` status `ready` deltaP `6.2373` edge `0.084` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0037` n `203` status `ready` deltaP `4.5213` edge `0.0504` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.2788` n `203` status `ready` deltaP `3.376` edge `0.0775` maxDD `-5.1926`
- `market_context_high->crypto_major_24h` score `-0.3639` n `147` status `ready` deltaP `23.1787` edge `0.6574` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.5019` n `203` status `ready` deltaP `0.8171` edge `0.0159` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5514` n `203` status `ready` deltaP `6.8678` edge `0.0171` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6142` n `192` status `ready` deltaP `12.0299` edge `0.1378` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.7161` n `147` status `ready` deltaP `5.2998` edge `0.0099` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-1.0441` n `203` status `ready` deltaP `-3.1776` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.7645` n `192` status `ready` deltaP `-6.593` edge `-0.0102` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.0699` n `203` status `ready` deltaP `1.2559` edge `-0.0283` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

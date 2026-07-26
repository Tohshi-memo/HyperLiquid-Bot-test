# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T18:22:27.756430+00:00`
- Price records: `672`
- Market context records: `8011`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11822`

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

- `market_context_high->equity_24h` score `15.9074` n `90` status `ready` deltaP `25.8156` edge `1.2877` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.7732` n `90` status `ready` deltaP `35.8752` edge `0.4086` maxDD `0.0`
- `market_context_high->equity_4h` score `6.1699` n `103` status `ready` deltaP `24.3812` edge `0.4409` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5851` n `103` status `ready` deltaP `23.9039` edge `0.1183` maxDD `-0.979`
- `market_context_high->index_4h` score `2.4172` n `103` status `ready` deltaP `25.2781` edge `0.0689` maxDD `-0.8791`
- `market_context_high->commodity_24h` score `2.3343` n `90` status `ready` deltaP `21.4423` edge `0.1962` maxDD `-6.2367`
- `market_context_high->index_24h` score `2.0675` n `90` status `ready` deltaP `12.513` edge `0.1559` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6892` n `103` status `ready` deltaP `14.373` edge `0.1267` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2491` n `90` status `ready` deltaP `25.6653` edge `0.0358` maxDD `-2.8915`
- `market_context_high->index_1h` score `0.8678` n `103` status `ready` deltaP `14.1495` edge `0.021` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7166` n `103` status `ready` deltaP `10.2674` edge `0.0291` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.6049` n `103` status `ready` deltaP `9.5876` edge `0.1583` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.5669` n `103` status `ready` deltaP `11.0148` edge `0.0403` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.5511` n `103` status `ready` deltaP `6.0661` edge `0.1172` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0353` n `103` status `ready` deltaP `1.0086` edge `0.032` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2292` n `103` status `ready` deltaP `0.936` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3255` n `103` status `ready` deltaP `6.4562` edge `0.0046` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5582` n `103` status `ready` deltaP `-0.7111` edge `-0.0045` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1921` n `103` status `ready` deltaP `0.2779` edge `-0.0045` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9438` n `103` status `ready` deltaP `7.0588` edge `-0.1667` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

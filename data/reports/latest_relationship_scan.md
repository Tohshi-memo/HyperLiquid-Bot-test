# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T23:22:32.684455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3911`

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

- `market_context_high->unknown_1h` score `32151.6086` n `45` status `ready` deltaP `1.5668` edge `2679.2997` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21812.5762` n `45` status `ready` deltaP `1.958` edge `1817.7155` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `916.6536` n `31` status `ready` deltaP `1.7819` edge `76.3935` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `559.6287` n `31` status `ready` deltaP `3.1766` edge `46.6202` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `256.5073` n `31` status `ready` deltaP `6.0764` edge `21.3351` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.7839` n `31` status `ready` deltaP `52.0833` edge `3.4681` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.0157` n `31` status `ready` deltaP `52.9514` edge `3.1483` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.3888` n `31` status `ready` deltaP `52.4306` edge `2.7662` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.5202` n `31` status `ready` deltaP `38.8049` edge `0.7288` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9061` n `31` status `ready` deltaP `26.4555` edge `0.8195` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4469` n `31` status `ready` deltaP `37.8344` edge `0.6664` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4547` n `31` status `ready` deltaP `53.2986` edge `0.2659` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7033` n `31` status `ready` deltaP `17.3879` edge `0.8852` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2412` n `31` status `ready` deltaP `44.4893` edge `0.153` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6763` n `31` status `ready` deltaP `19.9874` edge `0.1918` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3512` n `31` status `ready` deltaP `36.4625` edge `0.0622` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6734` n `31` status `ready` deltaP `31.6931` edge `0.02` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4719` n `31` status `ready` deltaP `10.31` edge `0.2943` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3291` n `45` status `ready` deltaP `28.8685` edge `0.0301` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2799` n `31` status `ready` deltaP `13.0046` edge `0.2413` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

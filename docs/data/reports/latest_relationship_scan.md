# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T22:07:20.835933+00:00`
- Price records: `672`
- Market context records: `800`
- Flow alert records: `2249`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `12.6917` n `149` status `ready` deltaP `29.9905` edge `0.8911` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.6881` n `149` status `ready` deltaP `7.1414` edge `0.4312` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.6098` n `33` status `ready` deltaP `10.1903` edge `0.2694` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.6098` n `33` status `ready` deltaP `10.1903` edge `0.2694` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.9225` n `33` status `ready` deltaP `18.2326` edge `0.1308` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.9225` n `33` status `ready` deltaP `18.2326` edge `0.1308` maxDD `-0.038`
- `risk_on_high->crypto_alt_4h` score `2.7665` n `33` status `ready` deltaP `21.092` edge `0.1104` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.7665` n `33` status `ready` deltaP `21.092` edge `0.1104` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.7562` n `33` status `ready` deltaP `19.8125` edge `0.1348` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7562` n `33` status `ready` deltaP `19.8125` edge `0.1348` maxDD `-0.9758`
- `risk_on_high->metal_1h` score `1.1051` n `33` status `ready` deltaP `12.9605` edge `0.0287` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.1051` n `33` status `ready` deltaP `12.9605` edge `0.0287` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.7736` n `33` status `ready` deltaP `4.9057` edge `0.1496` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.7736` n `33` status `ready` deltaP `4.9057` edge `0.1496` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3078` n `33` status `ready` deltaP `8.288` edge `0.0218` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3078` n `33` status `ready` deltaP `8.288` edge `0.0218` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2532` n `33` status `ready` deltaP `8.0975` edge `0.002` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2532` n `33` status `ready` deltaP `8.0975` edge `0.002` maxDD `-0.2147`
- `market_context_high->index_24h` score `-0.0296` n `149` status `ready` deltaP `1.4763` edge `0.1872` maxDD `-5.9609`
- `risk_on_high->crypto_major_1h` score `-0.1214` n `33` status `ready` deltaP `4.5818` edge `-0.0157` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

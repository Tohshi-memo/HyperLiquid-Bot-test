# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T19:22:16.468697+00:00`
- Price records: `672`
- Market context records: `786`
- Flow alert records: `2215`
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

- `market_context_high->crypto_major_24h` score `13.1585` n `149` status `ready` deltaP `31.2058` edge `0.9219` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3001` n `149` status `ready` deltaP `7.1414` edge `0.4822` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.81` n `33` status `ready` deltaP `10.4877` edge `0.2841` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.81` n `33` status `ready` deltaP `10.4877` edge `0.2841` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `3.1158` n `33` status `ready` deltaP `21.3369` edge `0.1546` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `3.1158` n `33` status `ready` deltaP `21.3369` edge `0.1546` maxDD `-0.9758`
- `risk_on_high->index_4h` score `3.0404` n `33` status `ready` deltaP `19.1517` edge `0.1345` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `3.0404` n `33` status `ready` deltaP `19.1517` edge `0.1345` maxDD `-0.038`
- `risk_on_high->crypto_alt_4h` score `3.0107` n `33` status `ready` deltaP `21.5493` edge `0.1277` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.0107` n `33` status `ready` deltaP `21.5493` edge `0.1277` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0428` n `33` status `ready` deltaP `12.8108` edge `0.0245` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0428` n `33` status `ready` deltaP `12.8108` edge `0.0245` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.6035` n `33` status `ready` deltaP `3.4943` edge `0.1372` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.6035` n `33` status `ready` deltaP `3.4943` edge `0.1372` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.4071` n `149` status `ready` deltaP `2.6752` edge `0.2156` maxDD `-5.9609`
- `risk_on_high->commodity_1h` score `0.2774` n `33` status `ready` deltaP `7.929` edge `0.0203` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2774` n `33` status `ready` deltaP `7.929` edge `0.0203` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2637` n `33` status `ready` deltaP `8.2981` edge `0.002` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2637` n `33` status `ready` deltaP `8.2981` edge `0.002` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.13` n `33` status `ready` deltaP `4.2824` edge `-0.0148` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

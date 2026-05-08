# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T16:52:20.069410+00:00`
- Price records: `663`
- Market context records: `775`
- Flow alert records: `2183`
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

- `market_context_high->crypto_major_24h` score `13.4061` n `147` status `ready` deltaP `31.7209` edge `0.9391` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5193` n `147` status `ready` deltaP `7.2562` edge `0.4997` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.6908` n `32` status `ready` deltaP `10.3178` edge `0.2753` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.6908` n `32` status `ready` deltaP `10.3178` edge `0.2753` maxDD `-0.9217`
- `risk_on_high->index_4h` score `3.0164` n `32` status `ready` deltaP `19.2117` edge `0.1321` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `3.0164` n `32` status `ready` deltaP `19.2117` edge `0.1321` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.8635` n `32` status `ready` deltaP `21.2133` edge `0.1344` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8635` n `32` status `ready` deltaP `21.2133` edge `0.1344` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.7353` n `32` status `ready` deltaP `21.6915` edge `0.1038` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.7353` n `32` status `ready` deltaP `21.6915` edge `0.1038` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0752` n `33` status `ready` deltaP `13.0961` edge `0.0253` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0752` n `33` status `ready` deltaP `13.0961` edge `0.0253` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.7749` n `32` status `ready` deltaP `4.8843` edge `0.1499` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.7749` n `32` status `ready` deltaP `4.8843` edge `0.1499` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.5112` n `147` status `ready` deltaP `2.837` edge `0.2232` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.2927` n `33` status `ready` deltaP `8.8272` edge `0.0022` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2927` n `33` status `ready` deltaP `8.8272` edge `0.0022` maxDD `-0.2147`
- `risk_on_high->commodity_1h` score `0.2329` n `33` status `ready` deltaP `7.5226` edge `0.0173` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2329` n `33` status `ready` deltaP `7.5226` edge `0.0173` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `-0.0515` n `33` status `ready` deltaP `4.9203` edge `-0.009` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

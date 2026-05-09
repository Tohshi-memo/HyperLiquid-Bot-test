# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T07:20:31.215467+00:00`
- Price records: `672`
- Market context records: `841`
- Flow alert records: `2363`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1278`

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

- `market_context_high->crypto_major_24h` score `11.7389` n `154` status `ready` deltaP `28.1002` edge `0.8243` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `4.8102` n `154` status `ready` deltaP `7.1631` edge `0.3579` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4978` n `33` status `ready` deltaP `9.8855` edge `0.2621` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4978` n `33` status `ready` deltaP `9.8855` edge `0.2621` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.4899` n `33` status `ready` deltaP `18.8978` edge `0.1187` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.4899` n `33` status `ready` deltaP `18.8978` edge `0.1187` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.4863` n `33` status `ready` deltaP `13.9644` edge `0.1229` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.4863` n `33` status `ready` deltaP `13.9644` edge `0.1229` maxDD `-0.038`
- `risk_on_high->crypto_alt_4h` score `2.1576` n `33` status `ready` deltaP `18.8054` edge `0.0749` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.1576` n `33` status `ready` deltaP `18.8054` edge `0.0749` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0776` n `33` status `ready` deltaP `12.6611` edge `0.0284` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0776` n `33` status `ready` deltaP `12.6611` edge `0.0284` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8271` n `33` status `ready` deltaP `5.363` edge `0.1534` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8271` n `33` status `ready` deltaP `5.363` edge `0.1534` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3125` n `33` status `ready` deltaP `8.288` edge `0.0224` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3125` n `33` status `ready` deltaP `8.288` edge `0.0224` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2096` n `33` status `ready` deltaP `7.349` edge `0.0014` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2096` n `33` status `ready` deltaP `7.349` edge `0.0014` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1627` n `33` status `ready` deltaP `4.4321` edge `-0.02` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.1627` n `33` status `ready` deltaP `4.4321` edge `-0.02` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

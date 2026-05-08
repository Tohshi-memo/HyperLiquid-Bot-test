# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T16:22:13.855475+00:00`
- Price records: `661`
- Market context records: `772`
- Flow alert records: `2177`
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

- `market_context_high->crypto_major_24h` score `13.4176` n `147` status `ready` deltaP `31.8645` edge `0.9391` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5779` n `147` status `ready` deltaP `7.2843` edge `0.5044` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.7204` n `32` status `ready` deltaP `10.4183` edge `0.2771` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.7204` n `32` status `ready` deltaP `10.4183` edge `0.2771` maxDD `-0.9217`
- `risk_on_high->index_4h` score `3.0335` n `32` status `ready` deltaP `19.3204` edge `0.1328` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `3.0335` n `32` status `ready` deltaP `19.3204` edge `0.1328` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.8858` n `32` status `ready` deltaP `21.3566` edge `0.1353` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8858` n `32` status `ready` deltaP `21.3566` edge `0.1353` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.779` n `32` status `ready` deltaP `21.7878` edge `0.1068` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.779` n `32` status `ready` deltaP `21.7878` edge `0.1068` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0881` n `33` status `ready` deltaP `13.2282` edge `0.0255` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0881` n `33` status `ready` deltaP `13.2282` edge `0.0255` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.7983` n `32` status `ready` deltaP `5.0653` edge `0.1517` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.7983` n `32` status `ready` deltaP `5.0653` edge `0.1517` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.5392` n `147` status `ready` deltaP `2.9466` edge `0.2248` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.292` n `33` status `ready` deltaP `8.8125` edge `0.0022` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.292` n `33` status `ready` deltaP `8.8125` edge `0.0022` maxDD `-0.2147`
- `risk_on_high->commodity_1h` score `0.2357` n `33` status `ready` deltaP `7.5317` edge `0.0176` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2357` n `33` status `ready` deltaP `7.5317` edge `0.0176` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `-0.0496` n `33` status `ready` deltaP `4.9122` edge `-0.0087` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

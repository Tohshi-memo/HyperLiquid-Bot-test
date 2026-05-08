# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T16:07:13.186752+00:00`
- Price records: `660`
- Market context records: `771`
- Flow alert records: `2174`
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

- `market_context_high->crypto_major_24h` score `13.4258` n `147` status `ready` deltaP `31.9366` edge `0.9393` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6103` n `147` status `ready` deltaP `7.2984` edge `0.507` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4136` n `31` status `ready` deltaP `9.7632` edge `0.2559` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4136` n `31` status `ready` deltaP `9.7632` edge `0.2559` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.904` n `31` status `ready` deltaP `18.871` edge `0.125` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.904` n `31` status `ready` deltaP `18.871` edge `0.125` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.7706` n `31` status `ready` deltaP `20.6221` edge `0.1306` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7706` n `31` status `ready` deltaP `20.6221` edge `0.1306` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.4994` n `31` status `ready` deltaP `21.5338` edge `0.0852` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.4994` n `31` status `ready` deltaP `21.5338` edge `0.0852` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0959` n `33` status `ready` deltaP `13.2946` edge `0.0257` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0959` n `33` status `ready` deltaP `13.2946` edge `0.0257` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5532` n `147` status `ready` deltaP `3.0017` edge `0.2256` maxDD `-5.9609`
- `risk_on_high->commodity_4h` score `0.5236` n `31` status `ready` deltaP `3.4425` edge `0.1273` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.5236` n `31` status `ready` deltaP `3.4425` edge `0.1273` maxDD `-1.3162`
- `risk_on_high->fx_1h` score `0.2956` n `33` status `ready` deltaP `8.8818` edge `0.0022` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2956` n `33` status `ready` deltaP `8.8818` edge `0.0022` maxDD `-0.2147`
- `risk_on_high->commodity_1h` score `0.2439` n `33` status `ready` deltaP `7.613` edge `0.0181` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2439` n `33` status `ready` deltaP `7.613` edge `0.0181` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `-0.0404` n `33` status `ready` deltaP `4.9843` edge `-0.008` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T06:22:24.900416+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11586`

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

- `risk_on_high->crypto_alt_24h` score `21.7178` n `55` status `ready` deltaP `48.0997` edge `1.5372` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.7178` n `55` status `ready` deltaP `48.0997` edge `1.5372` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `9.8967` n `55` status `ready` deltaP `29.3876` edge `0.7706` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `9.8967` n `55` status `ready` deltaP `29.3876` edge `0.7706` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.2908` n `102` status `ready` deltaP `24.5785` edge `0.5887` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.2908` n `102` status `ready` deltaP `24.5785` edge `0.5887` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.6217` n `154` status `ready` deltaP `21.4464` edge `0.4782` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.3092` n `55` status `ready` deltaP `70.6597` edge `0.0547` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.3092` n `55` status `ready` deltaP `70.6597` edge `0.0547` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2348` n `96` status `ready` deltaP `37.1527` edge `0.2494` maxDD `-1.8678`
- `risk_on_high->metal_24h` score `4.4152` n `55` status `ready` deltaP `40.5808` edge `0.1446` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.4152` n `55` status `ready` deltaP `40.5808` edge `0.1446` maxDD `-0.7767`
- `market_context_high->crypto_alt_24h` score `4.4062` n `96` status `ready` deltaP `22.5694` edge `0.8334` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `3.9574` n `96` status `ready` deltaP `20.4861` edge `0.4423` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.6037` n `107` status `ready` deltaP `7.5634` edge `0.2242` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.6037` n `107` status `ready` deltaP `7.5634` edge `0.2242` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.3811` n `159` status `ready` deltaP `6.9051` edge `0.2154` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0435` n `96` status `ready` deltaP `37.3264` edge `0.0308` maxDD `-1.6688`
- `risk_on_high->equity_24h` score `0.831` n `55` status `ready` deltaP `18.8889` edge `0.0241` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `0.831` n `55` status `ready` deltaP `18.8889` edge `0.0241` maxDD `-3.7955`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

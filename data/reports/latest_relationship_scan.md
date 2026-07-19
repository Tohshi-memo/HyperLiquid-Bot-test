# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T06:52:28.221731+00:00`
- Price records: `672`
- Market context records: `7224`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13679`

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

- `risk_on_high->crypto_major_4h` score `5.7843` n `34` status `ready` deltaP `26.1657` edge `0.3459` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.7843` n `34` status `ready` deltaP `26.1657` edge `0.3459` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.2747` n `34` status `ready` deltaP `17.1001` edge `0.2815` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.2747` n `34` status `ready` deltaP `17.1001` edge `0.2815` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1143` n `34` status `ready` deltaP `22.7281` edge `0.0397` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1143` n `34` status `ready` deltaP `22.7281` edge `0.0397` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.0466` n `34` status `ready` deltaP `4.9856` edge `0.1383` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.0466` n `34` status `ready` deltaP `4.9856` edge `0.1383` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.2552` n `34` status `ready` deltaP `7.4762` edge `0.0119` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2552` n `34` status `ready` deltaP `7.4762` edge `0.0119` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2376` n `34` status `ready` deltaP `2.8971` edge `0.0305` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2376` n `34` status `ready` deltaP `2.8971` edge `0.0305` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1474` n `34` status `ready` deltaP `4.2863` edge `0.0124` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1474` n `34` status `ready` deltaP `4.2863` edge `0.0124` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.3781` n `178` status `ready` deltaP `2.5096` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.561` n `178` status `ready` deltaP `0.1901` edge `-0.0111` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.5639` n `34` status `ready` deltaP `0.8967` edge `-0.0102` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.5639` n `34` status `ready` deltaP `0.8967` edge `-0.0102` maxDD `-0.7546`
- `market_context_high->crypto_major_1h` score `-0.6613` n `178` status `ready` deltaP `4.2707` edge `0.0278` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.6618` n `178` status `ready` deltaP `0.3364` edge `0.0168` maxDD `-5.9775`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

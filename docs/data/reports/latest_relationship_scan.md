# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T12:52:31.119422+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `news_risk_high->crypto_major_24h` score `21.6208` n `98` status `ready` deltaP `6.7142` edge `2.4428` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.8721` n `98` status `ready` deltaP `14.7463` edge `2.0458` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `18.7519` n `60` status `ready` deltaP `1.4024` edge `1.5683` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9017` n `101` status `ready` deltaP `22.8824` edge `0.4602` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.396` n `51` status `ready` deltaP `29.6978` edge `0.3042` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.4007` n `101` status `ready` deltaP `21.5105` edge `0.3491` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.1199` n `60` status `ready` deltaP `35.7521` edge `0.1183` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0402` n `101` status `ready` deltaP `16.5308` edge `0.1897` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.202` n `101` status `ready` deltaP `18.1775` edge `0.1146` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.9208` n `60` status `ready` deltaP `25.1118` edge `0.01` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.5852` n `51` status `ready` deltaP `18.5253` edge `0.0128` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.1483` n `62` status `ready` deltaP `13.8835` edge `0.0325` maxDD `-0.3491`
- `news_risk_high->commodity_24h` score `1.0308` n `98` status `ready` deltaP `22.775` edge `0.1109` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8067` n `62` status `ready` deltaP `12.5024` edge `0.0055` maxDD `-0.063`
- `news_risk_high->equity_24h` score `0.7433` n `98` status `ready` deltaP `16.571` edge `0.0924` maxDD `-4.941`
- `news_risk_high->metal_4h` score `0.6238` n `101` status `ready` deltaP `17.0988` edge `0.0434` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `market_context_high->metal_1h` score `0.3311` n `62` status `ready` deltaP `8.7792` edge `0.0063` maxDD `-0.4568`
- `news_risk_high->metal_24h` score `0.2975` n `98` status `ready` deltaP `15.5046` edge `0.0192` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2065` n `101` status `ready` deltaP `5.2143` edge `0.023` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T08:52:28.889735+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `66.0102` n `47` status `ready` deltaP `10.4154` edge `5.4385` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `40.8972` n `46` status `ready` deltaP `28.2911` edge `3.2351` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `26.1251` n `46` status `ready` deltaP `23.2639` edge `2.022` maxDD `0.0`
- `market_context_high->equity_24h` score `23.743` n `46` status `ready` deltaP `25.6869` edge `1.8174` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.8543` n `46` status `ready` deltaP `34.7147` edge `0.4318` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `7.1561` n `103` status `ready` deltaP `0.6001` edge `1.4966` maxDD `-63.6743`
- `news_risk_high->crypto_major_4h` score `4.4476` n `105` status `ready` deltaP `17.5755` edge `0.3112` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.3982` n `105` status `ready` deltaP `12.8122` edge `0.3809` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `3.863` n `103` status `ready` deltaP `-1.9788` edge `1.0364` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.0899` n `46` status `ready` deltaP `28.6912` edge `0.0896` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.8539` n `47` status `ready` deltaP `32.9593` edge `0.0335` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.4106` n `114` status `ready` deltaP `13.2472` edge `0.1616` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.1989` n `47` status `ready` deltaP `15.7725` edge `0.1199` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0469` n `114` status `ready` deltaP `15.343` edge `0.1118` maxDD `-1.8141`
- `news_risk_high->commodity_24h` score `1.7094` n `103` status `ready` deltaP `19.5809` edge `0.1298` maxDD `-2.431`
- `news_risk_high->fx_4h` score `1.6281` n `105` status `ready` deltaP `23.7558` edge `0.0409` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2793` n `103` status `ready` deltaP `30.1847` edge `0.1259` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.92` n `47` status `ready` deltaP `14.161` edge `0.0101` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8732` n `47` status `ready` deltaP `10.7179` edge `0.0416` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.6752` n `103` status `ready` deltaP `20.5654` edge `0.0943` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

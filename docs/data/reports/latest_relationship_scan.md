# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T20:22:29.775613+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8948`

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

- `market_context_high->unknown_24h` score `1380.805` n `40` status `ready` deltaP `-22.2222` edge `115.2516` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `52.602` n `90` status `ready` deltaP `-4.1023` edge `4.4689` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.79` n `40` status `ready` deltaP `27.6736` edge `0.5909` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3976` n `40` status `ready` deltaP `52.4306` edge `0.1836` maxDD `0.0`
- `market_context_high->unknown_1h` score `6.3191` n `102` status `ready` deltaP `-3.2376` edge `0.5818` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.1352` n `40` status `ready` deltaP `35.5556` edge `0.0372` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.4212` n `40` status `ready` deltaP `-21.1111` edge `0.574` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.8375` n `90` status `ready` deltaP `13.5535` edge `0.0078` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.5118` n `90` status `ready` deltaP `12.0732` edge `0.0155` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.3274` n `102` status `ready` deltaP `6.8246` edge `0.0999` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.2841` n `90` status `ready` deltaP `2.5474` edge `0.23` maxDD `-11.1784`
- `market_context_high->commodity_1h` score `0.2387` n `102` status `ready` deltaP `6.2933` edge `0.0063` maxDD `-0.6025`
- `market_context_high->metal_4h` score `0.1051` n `90` status `ready` deltaP `8.8245` edge `0.0222` maxDD `-1.1153`
- `market_context_high->crypto_alt_4h` score `0.037` n `90` status `ready` deltaP `-0.5861` edge `0.2645` maxDD `-13.8008`
- `market_context_high->fx_1h` score `-0.0123` n `102` status `ready` deltaP `3.2846` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.1479` n `102` status `ready` deltaP `6.4283` edge `0.0037` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.2344` n `102` status `ready` deltaP `0.3816` edge `0.0563` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.4721` n `90` status `ready` deltaP `0.437` edge `0.0066` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.6769` n `102` status `ready` deltaP `-3.0762` edge `-0.0012` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.9394` n `102` status `ready` deltaP `-5.4567` edge `0.0029` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

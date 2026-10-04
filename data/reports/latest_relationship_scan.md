# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T02:07:29.551062+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_1h` score `341.2391` n `54` status `ready` deltaP `11.7155` edge `28.3634` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.6956` n `50` status `ready` deltaP `12.8049` edge `26.7226` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.179` n `50` status `ready` deltaP `29.1127` edge `1.0745` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `11.5706` n `60` status `ready` deltaP `30.8348` edge `0.7813` maxDD `-1.1454`
- `market_context_high->crypto_major_24h` score `11.0397` n `50` status `ready` deltaP `34.8596` edge `0.8292` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.7037` n `66` status `ready` deltaP `38.775` edge `0.6538` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.2443` n `66` status `ready` deltaP `24.5103` edge `0.5747` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0204` n `50` status `ready` deltaP `15.8659` edge `0.5496` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4288` n `50` status `ready` deltaP `14.2073` edge `0.4866` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.8695` n `60` status `ready` deltaP `34.3818` edge `0.1823` maxDD `-0.1243`
- `news_risk_high->equity_4h` score `3.8307` n `66` status `ready` deltaP `26.4735` edge `0.204` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.0049` n `66` status `ready` deltaP `32.6866` edge `0.0587` maxDD `-0.4296`
- `market_context_high->fx_4h` score `2.9712` n `50` status `ready` deltaP `33.2988` edge `0.0391` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.9556` n `66` status `ready` deltaP `13.2054` edge `0.1938` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.5442` n `54` status `ready` deltaP `11.0169` edge `0.1836` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5285` n `66` status `ready` deltaP `21.6879` edge `0.1077` maxDD `-0.993`
- `market_context_high->crypto_alt_1h` score `2.2889` n `54` status `ready` deltaP `8.2668` edge `0.2061` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.096` n `66` status `ready` deltaP `25.7939` edge `0.0177` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.4741` n `66` status `ready` deltaP `4.7315` edge `0.1432` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.361` n `50` status `ready` deltaP `7.1681` edge `0.3129` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T03:07:29.072382+00:00`
- Price records: `672`
- Market context records: `4892`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8584`

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

- `market_context_high->unknown_1h` score `15.7663` n `110` status `ready` deltaP `9.5727` edge `1.2918` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.535` n `110` status `ready` deltaP `23.1624` edge `0.6933` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4858` n `110` status `ready` deltaP `21.3609` edge `0.5333` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.371` n `110` status `ready` deltaP `18.9495` edge `0.527` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1988` n `91` status `ready` deltaP `24.2541` edge `0.3058` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1053` n `110` status `ready` deltaP `7.9102` edge `0.1056` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8906` n `110` status `ready` deltaP `12.439` edge `0.1694` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5898` n `110` status `ready` deltaP `12.1452` edge `0.0409` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4414` n `110` status `ready` deltaP `6.3201` edge `0.1183` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3887` n `110` status `ready` deltaP `7.8715` edge `0.0996` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1942` n `110` status `ready` deltaP `3.9358` edge `0.0584` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.195` n `110` status `ready` deltaP `3.7316` edge `0.0161` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2351` n `110` status `ready` deltaP `-0.3539` edge `0.0302` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5328` n `110` status `ready` deltaP `-0.5879` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6996` n `110` status `ready` deltaP `0.4573` edge `0.0043` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.867` n `110` status `ready` deltaP `6.2721` edge `0.0046` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3358` n `110` status `ready` deltaP `-6.8672` edge `-0.0042` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.6534` n `91` status `ready` deltaP `-4.2526` edge `-0.0084` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5393` n `91` status `ready` deltaP `-5.2351` edge `-0.1385` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.7248` n `91` status `ready` deltaP `15.3674` edge `0.0147` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

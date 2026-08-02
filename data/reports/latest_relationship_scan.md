# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T09:22:25.595751+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5185.1798` n `60` status `ready` deltaP `30.6597` edge `431.936` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.7461` n `43` status `ready` deltaP `59.6213` edge `1.1211` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `8.4925` n `43` status `ready` deltaP `44.5171` edge `0.4648` maxDD `-2.9762`
- `news_risk_high->equity_4h` score `4.5433` n `68` status `ready` deltaP `16.5261` edge `0.3448` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5902` n `68` status `ready` deltaP `15.6115` edge `0.0665` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9965` n `43` status `ready` deltaP `13.9322` edge `0.1195` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.9117` n `43` status `ready` deltaP `19.5724` edge `0.0251` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.6312` n `68` status `ready` deltaP `9.7922` edge `0.0696` maxDD `-2.916`
- `market_context_high->commodity_1h` score `0.3393` n `43` status `ready` deltaP `7.6104` edge `0.0302` maxDD `-1.3282`
- `market_context_high->crypto_alt_4h` score `0.2399` n `43` status `ready` deltaP `3.9067` edge `0.0991` maxDD `-5.2176`
- `news_risk_high->fx_4h` score `0.182` n `68` status `ready` deltaP `12.9035` edge `0.0249` maxDD `-0.6604`
- `market_context_high->fx_1h` score `0.1441` n `43` status `ready` deltaP `9.9359` edge `0.0025` maxDD `-0.6874`
- `news_risk_high->metal_4h` score `0.1245` n `68` status `ready` deltaP `5.4698` edge `0.0271` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0757` n `68` status `ready` deltaP `6.1818` edge `0.0367` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0427` n `68` status `ready` deltaP `3.267` edge `0.005` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0863` n `68` status `ready` deltaP `2.1663` edge `0.0068` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1178` n `68` status `ready` deltaP `2.9148` edge `0.0058` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2132` n `68` status `ready` deltaP `2.3688` edge `0.0289` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3703` n `43` status `ready` deltaP `1.4622` edge `0.0055` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6373` n `68` status `ready` deltaP `3.267` edge `-0.0255` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

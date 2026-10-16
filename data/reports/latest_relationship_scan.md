# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T06:07:37.350853+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9002`

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

- `risk_on_high->commodity_24h` score `8.0709` n `54` status `ready` deltaP `43.0314` edge `0.3857` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0709` n `54` status `ready` deltaP `43.0314` edge `0.3857` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.5606` n `122` status `ready` deltaP `19.6347` edge `0.5906` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `6.0382` n `122` status `ready` deltaP `21.9962` edge `0.4887` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.3669` n `54` status `ready` deltaP `22.3973` edge `0.3426` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.3669` n `54` status `ready` deltaP `22.3973` edge `0.3426` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.135` n `54` status `ready` deltaP `35.4449` edge `0.3791` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.135` n `54` status `ready` deltaP `35.4449` edge `0.3791` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.51` n `122` status `ready` deltaP `13.8559` edge `0.1399` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9895` n `122` status `ready` deltaP `6.7071` edge `0.1183` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.253` n `122` status `ready` deltaP `11.8378` edge `0.0467` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.2806` n `122` status `ready` deltaP `0.5882` edge `-0.0015` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.3114` n `122` status `ready` deltaP `8.2041` edge `0.0063` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3675` n `54` status `ready` deltaP `3.4986` edge `0.0027` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3675` n `54` status `ready` deltaP `3.4986` edge `0.0027` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.4499` n `54` status `ready` deltaP `2.0016` edge `0.0012` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4499` n `54` status `ready` deltaP `2.0016` edge `0.0012` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.453` n `122` status `ready` deltaP `2.7151` edge `-0.0014` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.4833` n `54` status `ready` deltaP `-3.053` edge `-0.0032` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4833` n `54` status `ready` deltaP `-3.053` edge `-0.0032` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

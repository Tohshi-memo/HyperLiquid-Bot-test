# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T10:22:26.576032+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11484`

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

- `risk_on_high->unknown_4h` score `20.1547` n `133` status `ready` deltaP `8.0838` edge `1.6875` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.1547` n `133` status `ready` deltaP `8.0838` edge `1.6875` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `13.4066` n `186` status `ready` deltaP `10.7477` edge `1.1151` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.1724` n `133` status `ready` deltaP `-0.9039` edge `1.0781` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.1724` n `133` status `ready` deltaP `-0.9039` edge `1.0781` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.4308` n `198` status `ready` deltaP `-0.1558` edge `0.85` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.7201` n `167` status `ready` deltaP `16.4567` edge `0.4682` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `1.3628` n `61` status `ready` deltaP `11.4979` edge `0.057` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.5941` n `61` status `ready` deltaP `8.9538` edge `0.0071` maxDD `-0.0495`
- `risk_on_high->equity_24h` score `0.2676` n `133` status `ready` deltaP `11.072` edge `0.363` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.2676` n `133` status `ready` deltaP `11.072` edge `0.363` maxDD `-19.828`
- `risk_on_high->metal_1h` score `0.1498` n `133` status `ready` deltaP `12.8619` edge `0.0047` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1498` n `133` status `ready` deltaP `12.8619` edge `0.0047` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0431` n `61` status `ready` deltaP `4.9818` edge `-0.0034` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.0752` n `61` status `ready` deltaP `5.4089` edge `0.0023` maxDD `-0.9036`
- `news_risk_high->crypto_alt_24h` score `-0.1904` n `61` status `ready` deltaP `14.2987` edge `-0.0028` maxDD `-7.3552`
- `risk_on_high->index_1h` score `-0.1948` n `133` status `ready` deltaP `3.2439` edge `-0.0021` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1948` n `133` status `ready` deltaP `3.2439` edge `-0.0021` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.3361` n `133` status `ready` deltaP `4.1522` edge `0.046` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.3361` n `133` status `ready` deltaP `4.1522` edge `0.046` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

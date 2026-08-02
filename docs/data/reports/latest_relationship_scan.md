# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T10:52:31.949783+00:00`
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

- `news_risk_high->unknown_24h` score `5185.0521` n `60` status `ready` deltaP `29.618` edge `431.9323` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.603` n `41` status `ready` deltaP `59.1675` edge `1.1122` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `9.9557` n `41` status `ready` deltaP `48.9414` edge `0.5286` maxDD `-1.3521`
- `news_risk_high->equity_4h` score `4.5529` n `68` status `ready` deltaP `16.5261` edge `0.3456` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6182` n `68` status `ready` deltaP `15.9164` edge `0.0668` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0739` n `41` status `ready` deltaP `14.1768` edge `0.1278` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6552` n `68` status `ready` deltaP `9.9419` edge `0.0706` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.5379` n `41` status `ready` deltaP `18.4452` edge `0.0256` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5004` n `41` status `ready` deltaP `9.7342` edge `0.0367` maxDD `-1.3282`
- `market_context_high->crypto_alt_4h` score `0.4455` n `41` status `ready` deltaP `6.25` edge `0.1061` maxDD `-4.9184`
- `market_context_high->fx_1h` score `0.3558` n `41` status `ready` deltaP `12.772` edge `0.0024` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2588` n `68` status `ready` deltaP `13.8182` edge `0.0252` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1466` n `68` status `ready` deltaP `5.7747` edge `0.0279` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0967` n `68` status `ready` deltaP `6.4812` edge `0.0374` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0435` n `68` status `ready` deltaP `3.267` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0528` n `68` status `ready` deltaP `2.7651` edge `0.0071` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.0991` n `68` status `ready` deltaP `3.2142` edge `0.0062` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1743` n `68` status `ready` deltaP `2.9676` edge `0.0299` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.344` n `41` status `ready` deltaP `1.8183` edge `0.0065` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6856` n `68` status `ready` deltaP `2.6682` edge `-0.0277` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

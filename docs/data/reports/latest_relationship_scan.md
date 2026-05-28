# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T21:52:22.041743+00:00`
- Price records: `672`
- Market context records: `2182`
- Flow alert records: `8174`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.6647` n `132` status `ready` deltaP `35.9295` edge `0.9095` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.704` n `132` status `ready` deltaP `41.8237` edge `0.7495` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5229` n `132` status `ready` deltaP `21.8311` edge `0.3826` maxDD `-2.4317`
- `market_context_high->unknown_24h` score `3.8662` n `132` status `ready` deltaP `29.5455` edge `0.6067` maxDD `-32.8525`
- `news_risk_high->commodity_4h` score `3.8199` n `43` status `ready` deltaP `31.8526` edge `0.3445` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.5596` n `132` status `ready` deltaP `24.1778` edge `0.2449` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.1835` n `132` status `ready` deltaP `17.4152` edge `0.1969` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.8955` n `132` status `ready` deltaP `15.7594` edge `0.2226` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `2.8406` n `132` status `ready` deltaP `21.1016` edge `1.0517` maxDD `-60.2561`
- `market_context_high->index_4h` score `2.7975` n `132` status `ready` deltaP `22.9629` edge `0.1484` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.6192` n `132` status `ready` deltaP `10.9059` edge `0.2684` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1842` n `43` status `ready` deltaP `27.7368` edge `0.0155` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.6623` n `132` status `ready` deltaP `23.0271` edge `0.4696` maxDD `-33.1007`
- `market_context_high->metal_4h` score `1.5143` n `132` status `ready` deltaP `18.2003` edge `0.1436` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.4527` n `43` status `ready` deltaP `21.3445` edge `0.0257` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3593` n `43` status `ready` deltaP `14.9248` edge `0.0861` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.3313` n `43` status `ready` deltaP `-2.5312` edge `0.3083` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7206` n `43` status `ready` deltaP `10.3154` edge `0.0916` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4885` n `43` status `ready` deltaP `8.4389` edge `0.0101` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2968` n `132` status `ready` deltaP `9.041` edge `0.0433` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

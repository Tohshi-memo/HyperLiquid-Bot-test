# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T02:07:21.787918+00:00`
- Price records: `672`
- Market context records: `2201`
- Flow alert records: `8227`
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

- `market_context_high->crypto_alt_4h` score `12.6663` n `132` status `ready` deltaP `36.2343` edge `0.9076` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6762` n `132` status `ready` deltaP `41.6713` edge `0.7482` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4587` n `132` status `ready` deltaP `21.3738` edge `0.3803` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8119` n `43` status `ready` deltaP `31.7002` edge `0.3445` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3746` n `132` status `ready` deltaP `23.1107` edge `0.2366` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.3073` n `132` status `ready` deltaP `27.8094` edge `0.5717` maxDD `-32.8525`
- `market_context_high->crypto_major_1h` score `3.2434` n `132` status `ready` deltaP `17.7146` edge `0.1999` maxDD `-1.817`
- `market_context_high->index_4h` score `3.086` n `132` status `ready` deltaP `25.2494` edge `0.1572` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9327` n `132` status `ready` deltaP `15.9091` edge `0.2247` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.5052` n `132` status `ready` deltaP `10.9059` edge `0.2589` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1964` n `43` status `ready` deltaP `27.8892` edge `0.0155` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1764` n `132` status `ready` deltaP `18.8447` edge `0.9816` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4036` n `43` status `ready` deltaP `21.1948` edge `0.0226` maxDD `-1.7548`
- `market_context_high->metal_4h` score `1.3231` n `132` status `ready` deltaP `16.9808` edge `0.1358` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.2951` n `43` status `ready` deltaP `14.4675` edge `0.0838` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.2111` n `43` status `ready` deltaP `-3.5983` edge `0.3` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.744` n `43` status `ready` deltaP `10.6148` edge `0.0926` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4238` n `43` status `ready` deltaP `7.6904` edge `0.0097` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3364` n `132` status `ready` deltaP `9.3404` edge `0.0446` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.1924` n `43` status `ready` deltaP `4.7069` edge `0.0453` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

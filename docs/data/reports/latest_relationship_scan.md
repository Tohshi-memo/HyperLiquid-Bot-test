# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T02:22:21.636462+00:00`
- Price records: `672`
- Market context records: `2202`
- Flow alert records: `8230`
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

- `market_context_high->crypto_alt_4h` score `12.6711` n `132` status `ready` deltaP `36.2343` edge `0.908` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6834` n `132` status `ready` deltaP `41.6713` edge `0.7488` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4623` n `132` status `ready` deltaP `21.3738` edge `0.3806` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8127` n `43` status `ready` deltaP `31.7002` edge `0.3446` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3746` n `132` status `ready` deltaP `23.1107` edge `0.2366` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.255` n `132` status `ready` deltaP `27.6358` edge `0.5685` maxDD `-32.8525`
- `market_context_high->crypto_major_1h` score `3.2446` n `132` status `ready` deltaP `17.7146` edge `0.2` maxDD `-1.817`
- `market_context_high->index_4h` score `3.103` n `132` status `ready` deltaP `25.4019` edge `0.1576` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9183` n `132` status `ready` deltaP `15.7594` edge `0.2245` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.492` n `132` status `ready` deltaP `10.9059` edge `0.2578` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1976` n `43` status `ready` deltaP `27.8892` edge `0.0156` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1323` n `132` status `ready` deltaP `18.6711` edge `0.9771` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4251` n `43` status `ready` deltaP `21.3445` edge `0.0234` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.2987` n `43` status `ready` deltaP `14.4675` edge `0.0841` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.2965` n `132` status `ready` deltaP `16.8283` edge `0.1346` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.2111` n `43` status `ready` deltaP `-3.5983` edge `0.3` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.744` n `43` status `ready` deltaP `10.6148` edge `0.0926` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4357` n `43` status `ready` deltaP `7.8401` edge `0.0097` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3496` n `132` status `ready` deltaP `9.4901` edge `0.0447` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.201` n `43` status `ready` deltaP `4.8566` edge `0.0454` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

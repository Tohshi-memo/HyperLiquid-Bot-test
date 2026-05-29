# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T03:22:21.903043+00:00`
- Price records: `672`
- Market context records: `2206`
- Flow alert records: `8242`
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

- `market_context_high->crypto_alt_4h` score `12.7291` n `132` status `ready` deltaP `36.5392` edge `0.9108` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7282` n `132` status `ready` deltaP `41.9762` edge `0.7505` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4671` n `132` status `ready` deltaP `21.3738` edge `0.381` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8197` n `43` status `ready` deltaP `31.7002` edge `0.3455` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3818` n `132` status `ready` deltaP `23.1107` edge `0.2372` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2206` n `132` status `ready` deltaP `17.5649` edge `0.199` maxDD `-1.817`
- `market_context_high->index_4h` score `3.1674` n `132` status `ready` deltaP `26.0116` edge `0.1589` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `3.0477` n `132` status `ready` deltaP `27.1149` edge `0.5547` maxDD `-32.8525`
- `market_context_high->crypto_alt_1h` score `2.9195` n `132` status `ready` deltaP `15.7594` edge `0.2246` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.4061` n `132` status `ready` deltaP `10.7323` edge `0.2518` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.2` n `43` status `ready` deltaP `27.8892` edge `0.0158` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `1.9414` n `132` status `ready` deltaP `18.1502` edge `0.9561` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4335` n `43` status `ready` deltaP `21.3445` edge `0.0241` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3035` n `43` status `ready` deltaP `14.4675` edge `0.0845` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.2577` n `132` status `ready` deltaP `16.5235` edge `0.1334` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.2157` n `43` status `ready` deltaP `-3.5983` edge `0.3006` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7829` n `43` status `ready` deltaP `11.2136` edge `0.0936` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4873` n `43` status `ready` deltaP `8.4389` edge `0.01` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3292` n `132` status `ready` deltaP `9.3404` edge `0.044` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.1877` n `43` status `ready` deltaP `4.7069` edge `0.0447` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T06:52:24.057977+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10652`

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

- `risk_on_high->unknown_4h` score `19.2976` n `133` status `ready` deltaP `7.779` edge `1.6181` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.2976` n `133` status `ready` deltaP `7.779` edge `1.6181` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `8.1987` n `224` status `ready` deltaP `7.5675` edge `0.7058` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3571` n `37` status `ready` deltaP `25.1783` edge `0.4722` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.3328` n `37` status `ready` deltaP `25.0` edge `0.1944` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.8014` n `37` status `ready` deltaP `17.4852` edge `0.2415` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.153` n `37` status `ready` deltaP `21.5598` edge `0.0578` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8411` n `37` status `ready` deltaP `10.6666` edge `0.1024` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6398` n `37` status `ready` deltaP `13.6835` edge `0.0845` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.3381` n `37` status `ready` deltaP `7.3637` edge `0.0807` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1994` n `37` status `ready` deltaP `15.0227` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1592` n `37` status `ready` deltaP `13.817` edge `0.0238` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `0.9693` n `37` status `ready` deltaP `9.0266` edge `0.0471` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.794` n `37` status `ready` deltaP `7.1605` edge `0.0513` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.2227` n `37` status `ready` deltaP `12.317` edge `0.038` maxDD `-3.1244`
- `news_risk_high->crypto_major_24h` score `0.2124` n `37` status `ready` deltaP `12.7581` edge `0.2198` maxDD `-18.2098`
- `risk_on_high->metal_1h` score `0.0877` n `144` status `ready` deltaP `12.1465` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0877` n `144` status `ready` deltaP `12.1465` edge `0.0015` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.0018` n `37` status `ready` deltaP `6.1742` edge `0.0037` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1064` n `144` status `ready` deltaP `5.094` edge `-0.0029` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

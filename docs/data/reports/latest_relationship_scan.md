# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T04:22:18.902399+00:00`
- Price records: `672`
- Market context records: `2107`
- Flow alert records: `7960`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `11.0779` n `174` status `ready` deltaP `31.7493` edge `0.8218` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.7647` n `174` status `ready` deltaP `38.4234` edge `0.6939` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.8696` n `174` status `ready` deltaP `24.0679` edge `0.4036` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.2614` n `174` status `ready` deltaP `22.8851` edge `0.312` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.5686` n `174` status `ready` deltaP `19.0969` edge `0.1551` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.4347` n `173` status `ready` deltaP `11.9447` edge `0.2461` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.3293` n `174` status `ready` deltaP `16.1883` edge `0.1848` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `2.1515` n `173` status `ready` deltaP `23.3754` edge `0.5555` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `2.1271` n `174` status `ready` deltaP `12.7693` edge `0.2035` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.6846` n `173` status `ready` deltaP `23.1944` edge `0.4756` maxDD `-33.1875`
- `market_context_high->metal_4h` score `1.6221` n `174` status `ready` deltaP `17.0644` edge `0.2001` maxDD `-7.9614`
- `market_context_high->equity_1h` score `0.8711` n `174` status `ready` deltaP `10.8043` edge `0.0794` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `0.4275` n `173` status `ready` deltaP `21.1963` edge `0.7529` maxDD `-62.3533`
- `market_context_high->index_1h` score `0.1522` n `174` status `ready` deltaP `6.0035` edge `0.0317` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.0751` n `173` status `ready` deltaP `14.8619` edge `0.0306` maxDD `-2.811`
- `market_context_high->unknown_1h` score `-0.1279` n `174` status `ready` deltaP `4.8008` edge `0.0293` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.1658` n `174` status `ready` deltaP `6.8191` edge `0.039` maxDD `-4.8622`
- `market_context_high->fx_1h` score `-0.5943` n `174` status `ready` deltaP `-2.1492` edge `0.0009` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-0.6945` n `173` status `ready` deltaP `10.2216` edge `0.2641` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.0831` n `174` status `ready` deltaP `-7.1419` edge `-0.0031` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

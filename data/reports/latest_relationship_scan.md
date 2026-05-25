# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T08:22:16.848414+00:00`
- Price records: `672`
- Market context records: `1825`
- Flow alert records: `7151`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4474`

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

- `market_context_high->crypto_alt_4h` score `6.871` n `188` status `ready` deltaP `22.2528` edge `0.5387` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8277` n `178` status `ready` deltaP `27.4169` edge `0.6288` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.5002` n `30` status `ready` deltaP `29.2582` edge `0.4121` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.4488` n `188` status `ready` deltaP `26.0411` edge `0.4884` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.5369` n `188` status `ready` deltaP `16.9305` edge `0.4676` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6202` n `178` status `ready` deltaP `17.8683` edge `0.3054` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2123` n `30` status `ready` deltaP `24.4212` edge `0.1366` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0032` n `188` status `ready` deltaP `16.3077` edge `0.251` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.5938` n `178` status `ready` deltaP `14.0391` edge `0.6546` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.4121` n `178` status `ready` deltaP `16.5827` edge `0.5803` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.9034` n `30` status `ready` deltaP `21.6362` edge `-0.0012` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.7976` n `188` status `ready` deltaP `11.5302` edge `0.0985` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4841` n `196` status `ready` deltaP `6.6388` edge `0.0947` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3433` n `196` status `ready` deltaP `6.6724` edge `0.0955` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.2141` n `30` status `ready` deltaP `8.4553` edge `0.0434` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.0028` n `196` status `ready` deltaP `5.1815` edge `0.0446` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.0826` n `178` status `ready` deltaP `18.1648` edge `0.7306` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1622` n `178` status `ready` deltaP `11.6086` edge `0.014` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4216` n `30` status `ready` deltaP `16.7066` edge `-0.1182` maxDD `-2.1115`
- `market_context_high->unknown_1h` score `-0.4731` n `196` status `ready` deltaP `3.3393` edge `0.0335` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

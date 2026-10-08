# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T03:07:26.474710+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.6835` n `90` status `ready` deltaP `-4.0487` edge `3.3045` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7995` n `62` status `ready` deltaP `37.902` edge `0.6676` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.9068` n `62` status `ready` deltaP `22.1069` edge `0.5626` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.1844` n `62` status `ready` deltaP `15.4828` edge `0.4221` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.813` n `62` status `ready` deltaP `34.8877` edge `0.1685` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.3244` n `90` status `ready` deltaP `10.4836` edge `0.7819` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.9708` n `62` status `ready` deltaP `32.5453` edge `0.0568` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4688` n `62` status `ready` deltaP `10.256` edge `0.1729` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2947` n `90` status `ready` deltaP `15.9665` edge `0.1812` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1774` n `62` status `ready` deltaP `17.7223` edge `0.1231` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9496` n `62` status `ready` deltaP `24.5046` edge `0.0141` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.6798` n `90` status `ready` deltaP `13.0455` edge `0.0959` maxDD `-1.0977`
- `news_risk_high->unknown_4h` score `1.4631` n `62` status `ready` deltaP `-7.0237` edge `0.2933` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4533` n `62` status `ready` deltaP `21.0144` edge `0.0878` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2287` n `90` status `ready` deltaP `21.3644` edge `0.1636` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0979` n `62` status `ready` deltaP `2.9389` edge `0.1238` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0938` n `90` status `ready` deltaP `22.0396` edge `0.0189` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7176` n `90` status `ready` deltaP `12.0179` edge `0.0039` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1397` n `90` status `ready` deltaP `10.1843` edge `0.0389` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.1245` n `90` status `ready` deltaP `7.1964` edge `0.5618` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

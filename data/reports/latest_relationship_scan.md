# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T13:07:17.293633+00:00`
- Price records: `672`
- Market context records: `1844`
- Flow alert records: `7209`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4489`

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

- `market_context_high->crypto_alt_4h` score `6.7596` n `196` status `ready` deltaP `22.3152` edge `0.529` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.2539` n `178` status `ready` deltaP `24.6392` edge `0.5995` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.1857` n `196` status `ready` deltaP `25.6471` edge `0.4691` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.4957` n `196` status `ready` deltaP `17.9754` edge `0.4572` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.1976` n `178` status `ready` deltaP `16.3058` edge `0.2806` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.7075` n `178` status `ready` deltaP `14.56` edge `0.6606` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.5772` n `196` status `ready` deltaP `15.303` edge `0.2222` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.2878` n `178` status `ready` deltaP `13.2841` edge `0.5086` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.6815` n `196` status `ready` deltaP `11.3085` edge `0.0903` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3624` n `199` status `ready` deltaP `5.2975` edge `0.0935` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2618` n `178` status `ready` deltaP `19.3801` edge `0.7512` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.1862` n `199` status `ready` deltaP `5.308` edge `0.0915` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.0172` n `199` status `ready` deltaP `4.8371` edge `0.0457` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.0293` n `178` status `ready` deltaP `12.1294` edge `0.0216` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-0.4437` n `199` status `ready` deltaP `3.7365` edge `0.0333` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5374` n `199` status `ready` deltaP `5.982` edge `0.0248` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.5738` n `199` status `ready` deltaP `0.1437` edge `0.0144` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.574` n `196` status `ready` deltaP `12.7427` edge `0.1364` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.7547` n `199` status `ready` deltaP `-4.8491` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0546` n `196` status `ready` deltaP `-5.8922` edge `-0.0071` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

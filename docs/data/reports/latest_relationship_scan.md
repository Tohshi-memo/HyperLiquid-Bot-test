# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T21:22:26.745302+00:00`
- Price records: `672`
- Market context records: `6541`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `news_risk_high->crypto_alt_24h` score `13.6504` n `30` status `ready` deltaP `37.5274` edge `0.9021` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6513` n `30` status `ready` deltaP `55.286` edge `0.1857` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3799` n `144` status `ready` deltaP `11.8934` edge `0.7824` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.695` n `30` status `ready` deltaP `20.3524` edge `0.5442` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7369` n `36` status `ready` deltaP `39.3462` edge `0.0537` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.5921` n `30` status `ready` deltaP `26.7418` edge `0.0472` maxDD `-0.0911`
- `news_risk_high->fx_1h` score `2.1232` n `36` status `ready` deltaP `26.4138` edge `0.0189` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.9884` n `196` status `ready` deltaP `-6.4493` edge `0.2988` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.391` n `144` status `ready` deltaP `13.1307` edge `0.2152` maxDD `-5.2791`
- `news_risk_high->crypto_major_1h` score `0.6035` n `36` status `ready` deltaP `6.3872` edge `0.0885` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.6029` n `187` status `ready` deltaP `13.4962` edge `0.0279` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.3458` n `187` status `ready` deltaP `9.898` edge `0.1182` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `-0.083` n `36` status `ready` deltaP `-0.1497` edge `0.0413` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.2825` n `187` status `ready` deltaP `10.8851` edge `0.0611` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.3277` n `30` status `ready` deltaP `6.3662` edge `0.0027` maxDD `-2.3058`
- `market_context_high->crypto_major_4h` score `-0.3992` n `187` status `ready` deltaP `12.4169` edge `0.0951` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.429` n `196` status `ready` deltaP `-0.4002` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4606` n `196` status `ready` deltaP `1.5978` edge `-0.0014` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5232` n `196` status `ready` deltaP `6.483` edge `0.021` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5401` n `196` status `ready` deltaP `6.2172` edge `0.0159` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

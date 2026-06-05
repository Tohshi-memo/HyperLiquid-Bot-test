# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T10:22:25.506383+00:00`
- Price records: `672`
- Market context records: `2960`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.2735` n `122` status `ready` deltaP `12.5` edge `1.7478` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.7865` n `122` status `ready` deltaP `17.142` edge `0.6644` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.9387` n `122` status `ready` deltaP `17.9445` edge `0.7423` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `6.8529` n `122` status `ready` deltaP `26.8072` edge `0.5102` maxDD `-3.7602`
- `market_context_high->index_24h` score `3.2541` n `122` status `ready` deltaP `13.6726` edge `0.2781` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.2458` n `123` status `ready` deltaP `16.4126` edge `0.2043` maxDD `-1.1251`
- `market_context_high->crypto_alt_4h` score `2.7146` n `123` status `ready` deltaP `23.2724` edge `0.5272` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.7499` n `123` status `ready` deltaP `6.1992` edge `0.1265` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6914` n `123` status `ready` deltaP `13.567` edge `0.0816` maxDD `-2.3388`
- `market_context_high->equity_1h` score `0.3679` n `123` status `ready` deltaP `3.4468` edge `0.0534` maxDD `-1.6574`
- `market_context_high->index_1h` score `0.042` n `123` status `ready` deltaP `5.2639` edge `0.0197` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.2423` n `123` status `ready` deltaP `0.9639` edge `0.0041` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.3537` n `123` status `ready` deltaP `5.7982` edge `0.092` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.4553` n `123` status `ready` deltaP `5.5401` edge `0.0708` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.5183` n `123` status `ready` deltaP `-0.8118` edge `0.0015` maxDD `-3.3365`
- `market_context_high->crypto_major_4h` score `-0.5332` n `123` status `ready` deltaP `12.2967` edge `0.3622` maxDD `-33.6701`
- `market_context_high->unknown_1h` score `-0.6521` n `123` status `ready` deltaP `2.226` edge `0.0039` maxDD `-3.1801`
- `market_context_high->commodity_4h` score `-0.7673` n `123` status `ready` deltaP `5.8943` edge `0.0413` maxDD `-8.9839`
- `market_context_high->metal_1h` score `-0.8316` n `123` status `ready` deltaP `-2.1409` edge `-0.0036` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.8838` n `123` status `ready` deltaP `-0.7622` edge `0.0093` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

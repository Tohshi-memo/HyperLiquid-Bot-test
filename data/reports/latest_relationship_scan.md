# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T01:52:26.821826+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `1.0426` n `68` status `ready` deltaP `8.42` edge `0.1556` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7691` n `68` status `ready` deltaP `13.5402` edge `0.0216` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.337` n `68` status `ready` deltaP `9.4976` edge `0.1467` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0409` n `68` status `ready` deltaP `7.1064` edge `0.0032` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `-0.1368` n `68` status `ready` deltaP `3.533` edge `0.0035` maxDD `-0.2336`
- `news_risk_high->equity_1h` score `-0.1876` n `68` status `ready` deltaP `-2.0694` edge `0.0447` maxDD `-1.396`
- `news_risk_high->fx_24h` score `-0.1881` n `68` status `ready` deltaP `-3.7071` edge `0.0533` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.285` n `68` status `ready` deltaP `0.0705` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4861` n `68` status `ready` deltaP `-2.9676` edge `-0.0068` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2172` n `68` status `ready` deltaP `-3.7661` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.612` n `68` status `ready` deltaP `-6.232` edge `-0.0047` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-2.1756` n `68` status `ready` deltaP `-14.7323` edge `-0.0045` maxDD `-1.2868`
- `news_risk_high->crypto_major_1h` score `-2.3273` n `68` status `ready` deltaP `-9.3695` edge `-0.0376` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-2.5199` n `68` status `ready` deltaP `-5.9792` edge `-0.0526` maxDD `-5.4024`
- `news_risk_high->crypto_alt_4h` score `-2.7471` n `68` status `ready` deltaP `-7.2991` edge `-0.0415` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.5009` n `68` status `ready` deltaP `-2.3897` edge `-0.2433` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.6792` n `68` status `ready` deltaP `23.8868` edge `0.5277` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.6893` n `68` status `ready` deltaP `-32.7564` edge `-0.0126` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-10.4303` n `68` status `ready` deltaP `-30.4023` edge `-0.0986` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.3993` n `68` status `ready` deltaP `-28.9624` edge `-0.0732` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

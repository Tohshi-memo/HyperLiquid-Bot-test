# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T01:52:11.264855+00:00`
- Price records: `507`
- Market context records: `601`
- Flow alert records: `1700`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.6274` n `146` status `ready` deltaP `6.8577` edge `0.3447` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.7725` n `146` status `ready` deltaP `11.2455` edge `0.2728` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0278` n `146` status `ready` deltaP `10.7859` edge `0.0188` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3212` n `146` status `ready` deltaP `1.9395` edge `0.0037` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6336` n `146` status `ready` deltaP `1.2518` edge `0.0363` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6416` n `146` status `ready` deltaP `0.8387` edge `-0.0025` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.0996` n `146` status `ready` deltaP `5.7355` edge `0.0016` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.1492` n `146` status `ready` deltaP `-3.9652` edge `-0.009` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1925` n `146` status `ready` deltaP `-1.5662` edge `-0.0079` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7265` n `146` status `ready` deltaP `5.3146` edge `-0.007` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.8938` n `146` status `ready` deltaP `3.8934` edge `0.0732` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2043` n `146` status `ready` deltaP `0.3868` edge `-0.034` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.4955` n `146` status `ready` deltaP `-6.952` edge `0.0379` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.611` n `146` status `ready` deltaP `13.262` edge `0.0646` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.1876` n `146` status `ready` deltaP `-2.8986` edge `-0.0311` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3491` n `146` status `ready` deltaP `-4.9144` edge `-0.0504` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8169` n `146` status `ready` deltaP `-7.4372` edge `0.0816` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3184` n `146` status `ready` deltaP `-3.1739` edge `-0.0153` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.5371` n `146` status `ready` deltaP `-10.6526` edge `-0.0466` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-5.0143` n `146` status `ready` deltaP `0.9695` edge `-0.2365` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

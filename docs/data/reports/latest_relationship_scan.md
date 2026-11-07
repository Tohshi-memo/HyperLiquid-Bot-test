# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T10:52:27.256314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4001`

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

- `market_context_high->equity_1h` score `3.7503` n `31` status `ready` deltaP `10.8412` edge `0.2862` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.2565` n `62` status `ready` deltaP `11.6837` edge `0.1571` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6385` n `62` status `ready` deltaP `12.0131` edge `0.0209` maxDD `-0.4888`
- `market_context_high->crypto_major_1h` score `0.5451` n `31` status `ready` deltaP `10.1603` edge `0.0607` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.4994` n `31` status `ready` deltaP `7.6975` edge `0.0174` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.486` n `31` status `ready` deltaP `11.2082` edge `0.0691` maxDD `-3.1881`
- `market_context_high->index_1h` score `0.4393` n `31` status `ready` deltaP `2.6608` edge `0.0459` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.3345` n `62` status `ready` deltaP `9.9294` edge `0.1435` maxDD `-6.6786`
- `market_context_high->metal_1h` score `0.2901` n `31` status `ready` deltaP `7.316` edge `0.0212` maxDD `-0.6226`
- `news_risk_high->fx_24h` score `0.0669` n `62` status `ready` deltaP `-2.5706` edge `0.0669` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0629` n `62` status `ready` deltaP `7.4995` edge `0.0034` maxDD `-0.2931`
- `market_context_high->commodity_1h` score `-0.0563` n `31` status `ready` deltaP `6.1184` edge `0.0066` maxDD `-1.7019`
- `news_risk_high->equity_1h` score `-0.0854` n `62` status `ready` deltaP `-0.4491` edge `0.047` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1316` n `62` status `ready` deltaP `2.8588` edge `0.0026` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.1866` n `62` status `ready` deltaP `2.4243` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5392` n `62` status `ready` deltaP `-3.9743` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9475` n `62` status `ready` deltaP `1.4211` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1572` n `62` status `ready` deltaP `-1.695` edge `-0.0215` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2446` n `62` status `ready` deltaP `-2.857` edge `0.0199` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.6362` n `62` status `ready` deltaP `-11.6235` edge `-0.0029` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

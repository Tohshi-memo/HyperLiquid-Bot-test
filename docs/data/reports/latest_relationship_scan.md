# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T13:37:26.834365+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4099`

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

- `market_context_high->unknown_4h` score `265.7641` n `30` status `ready` deltaP `8.2521` edge `22.0978` maxDD `-0.1314`
- `market_context_high->fx_4h` score `3.4581` n `30` status `ready` deltaP `36.4735` edge `0.054` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.0759` n `37` status `ready` deltaP `8.5613` edge `0.2452` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.7087` n `30` status `ready` deltaP `22.246` edge `0.0411` maxDD `-2.4279`
- `news_risk_high->equity_4h` score `1.2035` n `60` status `ready` deltaP `10.9045` edge `0.1555` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7965` n `60` status `ready` deltaP `13.9126` edge `0.0214` maxDD `-0.4888`
- `market_context_high->crypto_major_1h` score `0.7387` n `37` status `ready` deltaP `9.6011` edge `0.0561` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.4697` n `37` status `ready` deltaP `7.6712` edge `0.0151` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.3805` n `37` status `ready` deltaP `10.4993` edge `0.0603` maxDD `-3.1881`
- `news_risk_high->index_24h` score `0.3542` n `60` status `ready` deltaP `10.0695` edge `0.1451` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.3462` n `60` status `ready` deltaP `-1.1806` edge `0.0719` maxDD `-0.1476`
- `market_context_high->index_1h` score `0.2973` n `37` status `ready` deltaP `1.9502` edge `0.0388` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1864` n `37` status `ready` deltaP `10.2161` edge `0.0104` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.1398` n `60` status `ready` deltaP `8.9321` edge `0.0037` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0033` n `60` status `ready` deltaP `0.7685` edge `0.0494` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.0805` n `60` status `ready` deltaP `3.8423` edge `0.0026` maxDD `-0.0826`
- `market_context_high->metal_1h` score `-0.0988` n `37` status `ready` deltaP `0.6029` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->fx_4h` score `-0.1446` n `60` status `ready` deltaP `3.1402` edge `0.0048` maxDD `-0.2082`
- `market_context_high->commodity_4h` score `-0.3869` n `30` status `ready` deltaP `-3.0284` edge `0.016` maxDD `-1.633`
- `news_risk_high->metal_1h` score `-0.5448` n `60` status `ready` deltaP `-4.0818` edge `-0.0069` maxDD `-0.5256`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

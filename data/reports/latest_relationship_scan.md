# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T17:07:31.626126+00:00`
- Price records: `672`
- Market context records: `5898`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10264`

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

- `news_risk_high->fx_4h` score `3.6047` n `30` status `ready` deltaP `37.4085` edge `0.0556` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0118` n `30` status `ready` deltaP `24.3812` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9346` n `30` status `ready` deltaP `11.3872` edge `0.0906` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8226` n `225` status `ready` deltaP `7.2412` edge `0.1303` maxDD `-4.1352`
- `news_risk_high->crypto_alt_1h` score `0.2271` n `30` status `ready` deltaP `5.02` edge `0.0418` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2372` n `225` status `ready` deltaP `4.7419` edge `0.0306` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.3122` n `225` status `ready` deltaP `3.3101` edge `0.005` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4538` n `30` status `ready` deltaP `1.0878` edge `-0.0288` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5611` n `225` status `ready` deltaP `-1.8224` edge `-0.0027` maxDD `-1.9006`
- `market_context_high->crypto_major_1h` score `-0.6131` n `225` status `ready` deltaP `3.165` edge `0.0324` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.6246` n `225` status `ready` deltaP `0.1943` edge `0.0034` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.714` n `225` status `ready` deltaP `2.1311` edge `0.0277` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.857` n `225` status `ready` deltaP `-3.1743` edge `-0.0014` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2518` n `30` status `ready` deltaP `-12.6946` edge `-0.0244` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6238` n `225` status `ready` deltaP `-2.7967` edge `-0.0182` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.6642` n `225` status `ready` deltaP `-2.9295` edge `-0.0306` maxDD `-5.725`
- `market_context_high->crypto_major_4h` score `-1.8738` n `225` status `ready` deltaP `8.3103` edge `0.1416` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.8813` n `30` status `ready` deltaP `-14.7967` edge `-0.055` maxDD `-2.3372`
- `market_context_high->index_4h` score `-2.0115` n `225` status `ready` deltaP `-1.3042` edge `0.0098` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.0277` n `218` status `ready` deltaP `2.284` edge `0.0066` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T06:22:29.382040+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `market_context_high->unknown_24h` score `37.3935` n `130` status `ready` deltaP `-18.025` edge `3.4817` maxDD `-9.6329`
- `market_context_high->commodity_24h` score `1.0295` n `130` status `ready` deltaP `13.3138` edge `0.1863` maxDD `-7.1122`
- `market_context_high->commodity_1h` score `0.6561` n `180` status `ready` deltaP `9.3114` edge `0.0269` maxDD `-0.7439`
- `market_context_high->commodity_4h` score `0.6358` n `169` status `ready` deltaP `10.3267` edge `0.0556` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.5254` n `130` status `ready` deltaP `17.4634` edge `0.0317` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.2055` n `180` status `ready` deltaP `2.4983` edge `-0.0005` maxDD `-0.4001`
- `market_context_high->fx_4h` score `-0.2673` n `169` status `ready` deltaP `3.3288` edge `0.004` maxDD `-0.504`
- `market_context_high->index_1h` score `-0.8428` n `180` status `ready` deltaP `-7.0758` edge `-0.0032` maxDD `-0.948`
- `market_context_high->metal_1h` score `-0.9862` n `180` status `ready` deltaP `-7.2488` edge `-0.0145` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.3294` n `169` status `ready` deltaP `-2.1831` edge `-0.0068` maxDD `-1.4875`
- `market_context_high->equity_1h` score `-1.4443` n `180` status `ready` deltaP `-6.8662` edge `-0.0117` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-2.5684` n `130` status `ready` deltaP `-0.0292` edge `-0.0814` maxDD `-2.9283`
- `market_context_high->crypto_alt_1h` score `-2.6009` n `180` status `ready` deltaP `-9.1084` edge `-0.0375` maxDD `-6.4812`
- `market_context_high->crypto_major_1h` score `-3.3902` n `180` status `ready` deltaP `-7.3952` edge `-0.0428` maxDD `-11.9002`
- `market_context_high->metal_4h` score `-3.6092` n `169` status `ready` deltaP `-10.977` edge `-0.0512` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.9369` n `169` status `ready` deltaP `-12.1072` edge `-0.1131` maxDD `-15.8728`
- `market_context_high->index_24h` score `-4.4206` n `130` status `ready` deltaP `-14.5728` edge `-0.0617` maxDD `-6.7627`
- `market_context_high->crypto_alt_4h` score `-6.8297` n `169` status `ready` deltaP `-13.7301` edge `-0.1428` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-7.2024` n `130` status `ready` deltaP `-16.074` edge `-0.2391` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-8.9126` n `130` status `ready` deltaP `-11.0088` edge `-0.1895` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

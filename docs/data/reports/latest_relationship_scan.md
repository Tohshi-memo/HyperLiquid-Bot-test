# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T08:22:30.182365+00:00`
- Price records: `672`
- Market context records: `7860`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `11.2333` n `129` status `ready` deltaP `28.8587` edge `0.8779` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.4222` n `130` status `ready` deltaP `5.0882` edge `0.3252` maxDD `-6.8098`
- `market_context_high->commodity_24h` score `1.4086` n `129` status `ready` deltaP `22.2649` edge `0.1273` maxDD `-7.0012`
- `market_context_high->metal_24h` score `1.2348` n `130` status `ready` deltaP `9.3627` edge `0.2369` maxDD `-2.3799`
- `market_context_high->crypto_major_4h` score `1.1639` n `130` status `ready` deltaP `14.3245` edge `0.1733` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0193` n `130` status `ready` deltaP `12.4574` edge `0.046` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8954` n `129` status `ready` deltaP `26.2581` edge `0.0485` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.8083` n `130` status `ready` deltaP `8.621` edge `0.1216` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.5423` n `130` status `ready` deltaP `9.292` edge `0.0426` maxDD `-1.0817`
- `market_context_high->equity_1h` score `0.4255` n `130` status `ready` deltaP `6.9415` edge `0.0942` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.4234` n `130` status `ready` deltaP `9.1938` edge `0.017` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2584` n `130` status `ready` deltaP `4.7236` edge `0.0333` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.1826` n `130` status `ready` deltaP `7.0524` edge `0.0141` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1632` n `130` status `ready` deltaP `11.0845` edge `0.051` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3059` n `130` status `ready` deltaP `-0.0554` edge `-0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8708` n `130` status `ready` deltaP `1.1354` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1172` n `129` status `ready` deltaP `-4.1025` edge `0.0938` maxDD `-2.1079`
- `market_context_high->metal_4h` score `-1.2816` n `130` status `ready` deltaP `2.8893` edge `0.0794` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4331` n `130` status `ready` deltaP `-3.2863` edge `0.001` maxDD `-1.6921`
- `market_context_high->crypto_alt_24h` score `-1.571` n `130` status `ready` deltaP `15.9032` edge `0.2221` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T14:52:25.960493+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9286`

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

- `market_context_high->equity_24h` score `6.6638` n `34` status `ready` deltaP `8.844` edge `0.7507` maxDD `-17.0141`
- `market_context_high->commodity_24h` score `1.9524` n `34` status `ready` deltaP `4.1463` edge `0.1938` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.9446` n `34` status `ready` deltaP `10.5392` edge `0.0971` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.6222` n `34` status `ready` deltaP `9.9877` edge `-0.0041` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3437` n `88` status `ready` deltaP `3.797` edge `0.0137` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5062` n `88` status `ready` deltaP `0.2926` edge `0.0014` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5264` n `88` status `ready` deltaP `3.7001` edge `0.0056` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.7808` n `88` status `ready` deltaP `-1.4689` edge `0.0203` maxDD `-4.182`
- `market_context_high->metal_4h` score `-0.9229` n `88` status `ready` deltaP `0.4712` edge `0.0169` maxDD `-4.0688`
- `market_context_high->index_1h` score `-0.9426` n `88` status `ready` deltaP `-6.7569` edge `0.0073` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.2953` n `88` status `ready` deltaP `-13.7588` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.4164` n `88` status `ready` deltaP `-6.7569` edge `0.0488` maxDD `-8.161`
- `market_context_high->crypto_alt_1h` score `-1.8664` n `88` status `ready` deltaP `1.0819` edge `-0.0486` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-2.0272` n `34` status `ready` deltaP `-3.2986` edge `-0.1826` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1091` n `88` status `ready` deltaP `-6.6103` edge `-0.0082` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.1058` n `88` status `ready` deltaP `-4.6611` edge `-0.1048` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.4198` n `88` status `ready` deltaP `0.3049` edge `-0.0708` maxDD `-25.2973`
- `market_context_high->crypto_major_24h` score `-6.3981` n `34` status `ready` deltaP `-6.5257` edge `-0.0266` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.6414` n `88` status `ready` deltaP `2.5499` edge `-0.2253` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.7784` n `34` status `ready` deltaP `-20.9049` edge `-0.2494` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

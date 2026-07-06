# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T18:52:26.184661+00:00`
- Price records: `672`
- Market context records: `5906`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11166`

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
- `news_risk_high->fx_1h` score `1.9878` n `30` status `ready` deltaP `24.0818` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9408` n `30` status `ready` deltaP `11.3872` edge `0.0914` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7683` n `220` status `ready` deltaP `7.2256` edge `0.1253` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.2169` n `30` status `ready` deltaP `5.02` edge `0.0405` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2106` n `220` status `ready` deltaP `4.9211` edge `0.0322` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3572` n `220` status `ready` deltaP `2.7599` edge `0.0029` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4811` n `30` status `ready` deltaP `0.6387` edge `-0.0293` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4978` n `220` status `ready` deltaP `-1.5406` edge `-0.002` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5279` n `220` status `ready` deltaP `3.963` edge `0.038` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6359` n `220` status `ready` deltaP `2.8988` edge `0.0326` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.6414` n `220` status `ready` deltaP `-0.1279` edge `0.0034` maxDD `-0.7819`
- `market_context_high->fx_1h` score `-0.8317` n `220` status `ready` deltaP `-2.8879` edge `-0.0012` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2074` n `30` status `ready` deltaP `-11.9461` edge `-0.0237` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.5941` n `220` status `ready` deltaP `-2.3752` edge `-0.0172` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.729` n `220` status `ready` deltaP `-3.6807` edge `-0.0339` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.9121` n `30` status `ready` deltaP `-15.254` edge `-0.0559` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-2.0327` n `220` status `ready` deltaP `8.0155` edge `0.1232` maxDD `-25.6458`
- `market_context_high->index_4h` score `-2.0421` n `220` status `ready` deltaP `-1.5521` edge `0.0089` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.132` n `213` status `ready` deltaP `0.8949` edge `0.0025` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

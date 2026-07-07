# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T05:07:26.470328+00:00`
- Price records: `672`
- Market context records: `5949`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `6.877` n `30` status `ready` deltaP `62.8472` edge `0.1541` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4668` n `30` status `ready` deltaP `39.2709` edge `0.2143` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.7761` n `30` status `ready` deltaP `39.0854` edge `0.0587` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0933` n `30` status `ready` deltaP `25.2794` edge `0.0198` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6239` n `221` status `ready` deltaP `10.5852` edge `0.1742` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.9276` n `30` status `ready` deltaP `11.2375` edge `0.0907` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2753` n `30` status `ready` deltaP `6.0679` edge `0.041` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.2085` n `30` status `ready` deltaP `6.9791` edge `0.0139` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.3468` n `230` status `ready` deltaP `4.9675` edge `0.0311` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.3892` n `30` status `ready` deltaP `2.2854` edge `-0.0285` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4008` n `230` status `ready` deltaP `2.4304` edge `-0.0005` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6449` n `230` status `ready` deltaP `0.5988` edge `0.0041` maxDD `-1.2616`
- `market_context_high->commodity_1h` score `-0.6974` n `230` status `ready` deltaP `-4.4689` edge `-0.0039` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.7852` n `230` status `ready` deltaP `-1.9669` edge `-0.0012` maxDD `-0.756`
- `market_context_high->equity_24h` score `-0.7905` n `213` status `ready` deltaP `19.2268` edge `0.2781` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0462` n `30` status `ready` deltaP `-9.4012` edge `-0.02` maxDD `-1.1161`
- `market_context_high->crypto_alt_1h` score `-1.0723` n `230` status `ready` deltaP `1.5751` edge `0.0176` maxDD `-8.9126`
- `market_context_high->crypto_major_1h` score `-1.1005` n `230` status `ready` deltaP `1.8172` edge `0.0193` maxDD `-9.4673`
- `market_context_high->metal_4h` score `-1.5834` n `221` status `ready` deltaP `-1.9465` edge `-0.0268` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.667` n `221` status `ready` deltaP `1.3974` edge `0.0205` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

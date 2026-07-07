# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T04:22:25.894344+00:00`
- Price records: `672`
- Market context records: `5946`
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

- `news_risk_high->fx_24h` score `6.8408` n `30` status `ready` deltaP `62.5` edge `0.1534` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.474` n `30` status `ready` deltaP `39.2709` edge `0.2149` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.7311` n `30` status `ready` deltaP `38.628` edge `0.058` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0933` n `30` status `ready` deltaP `25.2794` edge `0.0198` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5831` n `221` status `ready` deltaP `10.5852` edge `0.1708` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.9213` n `30` status `ready` deltaP `11.2375` edge `0.0899` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2644` n `30` status `ready` deltaP `5.9182` edge `0.0406` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1773` n `227` status `ready` deltaP `5.7374` edge `0.0352` maxDD `-4.3608`
- `news_risk_high->index_24h` score `-0.2217` n `30` status `ready` deltaP `6.9791` edge `0.0122` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3524` n `227` status `ready` deltaP `3.1371` edge `0.001` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.3861` n `30` status `ready` deltaP `2.2854` edge `-0.0281` maxDD `-1.2643`
- `market_context_high->index_1h` score `-0.5853` n `227` status `ready` deltaP `1.2596` edge `0.0049` maxDD `-1.0668`
- `market_context_high->commodity_1h` score `-0.6342` n `227` status `ready` deltaP `-3.8771` edge `-0.0039` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.8081` n `227` status `ready` deltaP `-2.2389` edge `-0.0013` maxDD `-0.756`
- `market_context_high->equity_24h` score `-0.9119` n `213` status `ready` deltaP `18.706` edge `0.266` maxDD `-31.2762`
- `market_context_high->crypto_alt_1h` score `-0.9169` n `227` status `ready` deltaP `2.1149` edge `0.0209` maxDD `-8.2036`
- `market_context_high->crypto_major_1h` score `-0.9447` n `227` status `ready` deltaP `2.5298` edge `0.0232` maxDD `-8.5616`
- `news_risk_high->index_1h` score `-1.047` n `30` status `ready` deltaP `-9.4012` edge `-0.0201` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.6252` n `221` status `ready` deltaP `-2.4038` edge `-0.0291` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.6766` n `221` status `ready` deltaP `1.3974` edge `0.0197` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

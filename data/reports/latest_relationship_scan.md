# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T03:52:34.043940+00:00`
- Price records: `672`
- Market context records: `5943`
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

- `news_risk_high->fx_24h` score `6.8046` n `30` status `ready` deltaP `62.1528` edge `0.1527` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.48` n `30` status `ready` deltaP `39.2709` edge `0.2154` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.7007` n `30` status `ready` deltaP `38.3232` edge `0.0575` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1052` n `30` status `ready` deltaP `25.4291` edge `0.0198` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5375` n `221` status `ready` deltaP `10.5852` edge `0.167` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8933` n `30` status `ready` deltaP `10.9381` edge `0.0883` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2395` n `30` status `ready` deltaP `5.6188` edge `0.0394` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1112` n `225` status `ready` deltaP `5.9628` edge `0.038` maxDD `-4.3608`
- `news_risk_high->index_24h` score `-0.2288` n `30` status `ready` deltaP `6.9791` edge `0.0113` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3328` n `225` status `ready` deltaP `3.4691` edge `0.0013` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.397` n `30` status `ready` deltaP `2.1357` edge `-0.0285` maxDD `-1.2643`
- `market_context_high->index_1h` score `-0.5504` n `225` status `ready` deltaP `1.4105` edge `0.0054` maxDD `-0.8293`
- `market_context_high->commodity_1h` score `-0.6108` n `225` status `ready` deltaP `-3.4737` edge `-0.0036` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.7947` n `225` status `ready` deltaP `-2.1264` edge `-0.0013` maxDD `-0.7267`
- `market_context_high->crypto_major_1h` score `-0.8236` n `225` status `ready` deltaP `2.7159` edge `0.0262` maxDD `-7.6584`
- `market_context_high->crypto_alt_1h` score `-0.8335` n `225` status `ready` deltaP `2.2854` edge `0.0229` maxDD `-7.5997`
- `market_context_high->equity_24h` score `-0.9861` n `213` status `ready` deltaP `18.3588` edge `0.2588` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0664` n `30` status `ready` deltaP `-9.7006` edge `-0.0206` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.6613` n `221` status `ready` deltaP `-2.7087` edge `-0.0317` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.6874` n `221` status `ready` deltaP `1.3974` edge `0.0188` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

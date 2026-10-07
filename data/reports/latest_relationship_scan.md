# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T13:22:52.683094+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_4h` score `36.2932` n `90` status `ready` deltaP `-5.8468` edge `3.1173` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.6195` n `62` status `ready` deltaP `36.4477` edge `0.6623` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.4304` n `62` status `ready` deltaP `24.0018` edge `0.5936` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.8494` n `62` status `ready` deltaP `27.7778` edge `0.1356` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.3675` n `62` status `ready` deltaP `8.6526` edge `0.2329` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.0739` n `62` status `ready` deltaP `33.9841` edge `0.0558` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4276` n `62` status `ready` deltaP `9.8754` edge `0.172` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.3367` n `62` status `ready` deltaP `19.7581` edge `0.1228` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.1147` n `90` status `ready` deltaP `14.5122` edge `0.1759` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0499` n `62` status `ready` deltaP `25.7727` edge `0.014` maxDD `-0.1997`
- `market_context_high->crypto_major_24h` score `1.8472` n `90` status `ready` deltaP `6.7361` edge `0.4893` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.4617` n `62` status `ready` deltaP `20.4858` edge `0.0924` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2785` n `62` status `ready` deltaP `3.9067` edge `0.1324` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.7932` n `90` status `ready` deltaP `18.7771` edge `0.0156` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7657` n `90` status `ready` deltaP `12.6946` edge `0.0034` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.6971` n `90` status `ready` deltaP `18.7152` edge `0.1131` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.2156` n `62` status `ready` deltaP `7.4995` edge `0.0098` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.1129` n `90` status `ready` deltaP `9.8037` edge `0.038` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.0918` n `62` status `ready` deltaP `24.4176` edge `0.0056` maxDD `-8.196`
- `market_context_high->commodity_1h` score `-0.0431` n `90` status `ready` deltaP `4.2315` edge `0.0058` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

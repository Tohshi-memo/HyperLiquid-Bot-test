# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T13:37:28.829335+00:00`
- Price records: `672`
- Market context records: `5776`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8674`

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

- `market_context_high->equity_24h` score `0.661` n `234` status `ready` deltaP `15.6651` edge `0.4882` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1445` n `291` status `ready` deltaP `7.7115` edge `0.1245` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2877` n `303` status `ready` deltaP `1.6348` edge `0.0007` maxDD `-0.5452`
- `market_context_high->equity_1h` score `-0.5771` n `303` status `ready` deltaP `3.8399` edge `0.027` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6047` n `303` status `ready` deltaP `2.6897` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7816` n `303` status `ready` deltaP `-2.1487` edge `-0.0054` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.852` n `303` status `ready` deltaP `3.6457` edge `0.0368` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-0.9283` n `234` status `ready` deltaP `14.7036` edge `0.0413` maxDD `-3.6674`
- `market_context_high->index_1h` score `-0.9504` n `303` status `ready` deltaP `0.5904` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-1.042` n `303` status `ready` deltaP `1.9377` edge `0.0337` maxDD `-6.6758`
- `market_context_high->fx_4h` score `-1.2809` n `291` status `ready` deltaP `2.2362` edge `0.0054` maxDD `-1.4288`
- `market_context_high->index_4h` score `-1.8466` n `291` status `ready` deltaP `0.637` edge `0.0106` maxDD `-3.165`
- `market_context_high->commodity_4h` score `-2.4413` n `291` status `ready` deltaP `-2.8256` edge `-0.0266` maxDD `-14.071`
- `market_context_high->metal_4h` score `-2.5344` n `291` status `ready` deltaP `-6.1169` edge `-0.0482` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.8639` n `291` status `ready` deltaP `7.7372` edge `0.147` maxDD `-25.6458`
- `market_context_high->index_24h` score `-2.8663` n `234` status `ready` deltaP `2.5641` edge `0.0299` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.4377` n `291` status `ready` deltaP `5.4066` edge `0.095` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-6.0341` n `234` status `ready` deltaP `3.9931` edge `-0.0546` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0432` n `234` status `ready` deltaP `-7.8659` edge `-0.2436` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.9271` n `234` status `ready` deltaP `-14.0358` edge `-0.0794` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

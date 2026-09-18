# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T13:52:33.973059+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8620`

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

- `market_context_high->unknown_4h` score `39.9646` n `149` status `ready` deltaP `-0.4634` edge `3.3568` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.8433` n `52` status `ready` deltaP `-7.704` edge `1.2275` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8433` n `52` status `ready` deltaP `-7.704` edge `1.2275` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.7708` n `52` status `ready` deltaP `49.3056` edge `0.4022` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.7708` n `52` status `ready` deltaP `49.3056` edge `0.4022` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4717` n `149` status `ready` deltaP `42.5942` edge `0.3912` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `3.9854` n `30` status `ready` deltaP `21.4236` edge `0.3272` maxDD `-9.3661`
- `news_risk_high->crypto_alt_4h` score `3.2903` n `95` status `ready` deltaP `21.6447` edge `0.4926` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8027` n `52` status `ready` deltaP `32.5399` edge `0.0516` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8027` n `52` status `ready` deltaP `32.5399` edge `0.0516` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7024` n `149` status `ready` deltaP `29.0422` edge `0.0734` maxDD `-0.345`
- `news_risk_high->index_24h` score `1.0831` n `30` status `ready` deltaP `9.4445` edge `0.0449` maxDD `-0.075`
- `market_context_high->commodity_1h` score `1.0618` n `149` status `ready` deltaP `15.7618` edge `0.0211` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.6945` n `52` status `ready` deltaP `16.3061` edge `-0.0466` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6945` n `52` status `ready` deltaP `16.3061` edge `-0.0466` maxDD `-0.0054`
- `news_risk_high->equity_4h` score `0.6487` n `95` status `ready` deltaP `12.2288` edge `0.0958` maxDD `-4.1995`
- `market_context_high->fx_24h` score `0.5596` n `149` status `ready` deltaP `13.5312` edge `-0.022` maxDD `-0.0593`
- `news_risk_high->crypto_major_4h` score `0.5472` n `95` status `ready` deltaP `13.7099` edge `0.3034` maxDD `-19.972`
- `risk_on_high->commodity_1h` score `0.4385` n `52` status `ready` deltaP `8.8439` edge `0.0128` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4385` n `52` status `ready` deltaP `8.8439` edge `0.0128` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

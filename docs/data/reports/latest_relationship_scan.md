# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T12:22:37.117281+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8366`

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

- `market_context_high->unknown_4h` score `40.0932` n `149` status `ready` deltaP `-0.311` edge `3.3665` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.9719` n `52` status `ready` deltaP `-7.5516` edge `1.2372` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.9719` n `52` status `ready` deltaP `-7.5516` edge `1.2372` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8672` n `52` status `ready` deltaP `50.0` edge `0.4056` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8672` n `52` status `ready` deltaP `50.0` edge `0.4056` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5681` n `149` status `ready` deltaP `43.2886` edge `0.3946` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.1672` n `93` status `ready` deltaP `21.017` edge `0.481` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8219` n `52` status `ready` deltaP `32.5399` edge `0.0532` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8219` n `52` status `ready` deltaP `32.5399` edge `0.0532` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7216` n `149` status `ready` deltaP `29.0422` edge `0.075` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.1049` n `149` status `ready` deltaP `16.0612` edge `0.0227` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.8319` n `93` status `ready` deltaP `12.8475` edge `0.1047` maxDD `-3.3619`
- `risk_on_high->fx_24h` score `0.7975` n `52` status `ready` deltaP `17.1741` edge `-0.0438` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.7975` n `52` status `ready` deltaP `17.1741` edge `-0.0438` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.6626` n `149` status `ready` deltaP `14.3992` edge `-0.0192` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4817` n `52` status `ready` deltaP `9.1433` edge `0.0144` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4817` n `52` status `ready` deltaP `9.1433` edge `0.0144` maxDD `-0.1507`
- `news_risk_high->crypto_major_4h` score `0.3616` n `93` status `ready` deltaP `12.8557` edge `0.2853` maxDD `-19.972`
- `news_risk_high->fx_4h` score `0.3292` n `93` status `ready` deltaP `9.2053` edge `0.0255` maxDD `-0.2398`
- `news_risk_high->equity_1h` score `0.3021` n `95` status `ready` deltaP `10.1402` edge `0.0233` maxDD `-1.8403`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

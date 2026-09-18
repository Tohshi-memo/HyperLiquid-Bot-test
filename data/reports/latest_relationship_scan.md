# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T05:37:28.578431+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8638`

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

- `market_context_high->unknown_4h` score `40.3552` n `149` status `ready` deltaP `-0.0061` edge `3.3863` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `14.2339` n `52` status `ready` deltaP `-7.2467` edge `1.257` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `14.2339` n `52` status `ready` deltaP `-7.2467` edge `1.257` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9272` n `52` status `ready` deltaP `50.0` edge `0.4106` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9272` n `52` status `ready` deltaP `50.0` edge `0.4106` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6281` n `149` status `ready` deltaP `43.2886` edge `0.3996` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.9075` n `52` status `ready` deltaP `32.8447` edge `0.0583` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9075` n `52` status `ready` deltaP `32.8447` edge `0.0583` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8072` n `149` status `ready` deltaP `29.347` edge `0.0801` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.3913` n `69` status `ready` deltaP `15.2969` edge `0.425` maxDD `-12.9654`
- `risk_on_high->fx_24h` score `1.3273` n `52` status `ready` deltaP `21.8616` edge `-0.0309` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.3273` n `52` status `ready` deltaP `21.8616` edge `-0.0309` maxDD `-0.0054`
- `market_context_high->commodity_1h` score `1.2224` n `149` status `ready` deltaP `17.1091` edge `0.0255` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.1924` n `149` status `ready` deltaP `19.0867` edge `-0.0063` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5991` n `52` status `ready` deltaP `10.1912` edge `0.0172` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5991` n `52` status `ready` deltaP `10.1912` edge `0.0172` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.4175` n `69` status `ready` deltaP `10.262` edge `0.0688` maxDD `-3.3619`
- `news_risk_high->equity_1h` score `0.1827` n `79` status `ready` deltaP `8.7584` edge `0.0172` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.1234` n `69` status `ready` deltaP `5.6867` edge `0.0226` maxDD `-0.2415`
- `market_context_high->fx_4h` score `0.0382` n `149` status `ready` deltaP `7.9043` edge `-0.0002` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

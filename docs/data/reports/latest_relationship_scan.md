# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T06:22:35.675886+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8410`

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

- `market_context_high->unknown_4h` score `39.9268` n `149` status `ready` deltaP `-0.0061` edge `3.3506` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.8055` n `52` status `ready` deltaP `-7.2467` edge `1.2213` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8055` n `52` status `ready` deltaP `-7.2467` edge `1.2213` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9032` n `52` status `ready` deltaP `50.0` edge `0.4086` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9032` n `52` status `ready` deltaP `50.0` edge `0.4086` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6041` n `149` status `ready` deltaP `43.2886` edge `0.3976` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8883` n `52` status `ready` deltaP `32.8447` edge `0.0567` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8883` n `52` status `ready` deltaP `32.8447` edge `0.0567` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.788` n `149` status `ready` deltaP `29.347` edge `0.0785` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.5875` n `69` status `ready` deltaP `16.2889` edge `0.4382` maxDD `-12.8718`
- `risk_on_high->fx_24h` score `1.2701` n `52` status `ready` deltaP `21.3408` edge `-0.0322` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.2701` n `52` status `ready` deltaP `21.3408` edge `-0.0322` maxDD `-0.0054`
- `market_context_high->commodity_1h` score `1.202` n `149` status `ready` deltaP `16.9594` edge `0.0248` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.1352` n `149` status `ready` deltaP `18.5659` edge `-0.0076` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5787` n `52` status `ready` deltaP `10.0415` edge `0.0165` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5787` n `52` status `ready` deltaP `10.0415` edge `0.0165` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.4151` n `69` status `ready` deltaP `10.262` edge `0.0685` maxDD `-3.3619`
- `news_risk_high->equity_1h` score `0.2356` n `81` status `ready` deltaP `9.8211` edge `0.0169` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.1853` n `69` status `ready` deltaP `6.6786` edge `0.0239` maxDD `-0.2398`
- `market_context_high->fx_4h` score `0.0105` n `149` status `ready` deltaP `7.447` edge `-0.0007` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T06:37:28.383603+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8218`

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

- `market_context_high->unknown_4h` score `39.8392` n `149` status `ready` deltaP `-0.0061` edge `3.3433` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7179` n `52` status `ready` deltaP `-7.2467` edge `1.214` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7179` n `52` status `ready` deltaP `-7.2467` edge `1.214` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8984` n `52` status `ready` deltaP `50.0` edge `0.4082` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8984` n `52` status `ready` deltaP `50.0` edge `0.4082` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5993` n `149` status `ready` deltaP `43.2886` edge `0.3972` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8859` n `52` status `ready` deltaP `32.8447` edge `0.0565` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8859` n `52` status `ready` deltaP `32.8447` edge `0.0565` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7856` n `149` status `ready` deltaP `29.347` edge `0.0783` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.6471` n `70` status `ready` deltaP `16.5506` edge `0.4441` maxDD `-12.8718`
- `risk_on_high->fx_24h` score `1.2502` n `52` status `ready` deltaP `21.1672` edge `-0.0327` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.2502` n `52` status `ready` deltaP `21.1672` edge `-0.0327` maxDD `-0.0054`
- `market_context_high->commodity_1h` score `1.2044` n `149` status `ready` deltaP `16.9594` edge `0.025` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.1153` n `149` status `ready` deltaP `18.3923` edge `-0.0081` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5811` n `52` status `ready` deltaP `10.0415` edge `0.0167` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5811` n `52` status `ready` deltaP `10.0415` edge `0.0167` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.5364` n `70` status `ready` deltaP `10.7796` edge `0.0806` maxDD `-3.3619`
- `news_risk_high->equity_1h` score `0.2856` n `82` status `ready` deltaP `10.333` edge `0.0199` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.2124` n `70` status `ready` deltaP `7.0644` edge `0.0248` maxDD `-0.2398`
- `market_context_high->fx_1h` score `0.0112` n `149` status `ready` deltaP `3.9033` edge `0.0012` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T14:52:44.719961+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8732`

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

- `market_context_high->unknown_24h` score `895.237` n `117` status `ready` deltaP `11.0847` edge `74.5672` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `11.2347` n `117` status `ready` deltaP `-0.3583` edge `0.9925` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.1919` n `62` status `ready` deltaP `32.9416` edge `0.5667` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.377` n `62` status `ready` deltaP `19.1238` edge `0.455` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.1513` n `62` status `ready` deltaP `9.6996` edge `0.2079` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.0784` n `62` status `ready` deltaP `21.6495` edge `0.1122` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.447` n `117` status `ready` deltaP `12.801` edge `0.215` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.4151` n `62` status `ready` deltaP `27.4292` edge `0.0446` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0235` n `62` status `ready` deltaP `7.7796` edge `0.1523` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8055` n `62` status `ready` deltaP `23.0781` edge `0.0116` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.5818` n `62` status `ready` deltaP `15.9471` edge `0.0853` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1561` n `62` status `ready` deltaP `16.9797` edge `0.0766` maxDD `-0.993`
- `market_context_high->commodity_4h` score `1.1009` n `117` status `ready` deltaP `15.382` edge `0.0592` maxDD `-1.6002`
- `market_context_high->fx_4h` score `0.9372` n `117` status `ready` deltaP `19.9604` edge `0.0207` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.8263` n `62` status `ready` deltaP `3.0085` edge `0.1007` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.8053` n `62` status `ready` deltaP `27.0092` edge `0.0798` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7659` n `117` status `ready` deltaP `12.992` edge `0.0056` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.6159` n `117` status `ready` deltaP `10.8578` edge `0.0186` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.2522` n `117` status `ready` deltaP `-1.7888` edge `0.2053` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.042` n `62` status `ready` deltaP `4.9546` edge `0.0053` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

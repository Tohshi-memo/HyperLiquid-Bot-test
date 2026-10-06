# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T15:22:33.636087+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8712`

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

- `market_context_high->unknown_24h` score `1001.1238` n `117` status `ready` deltaP `11.0847` edge `83.3911` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `19.6335` n `117` status `ready` deltaP `-0.3583` edge `1.6924` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.0727` n `62` status `ready` deltaP `32.6367` edge `0.5588` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.2626` n `62` status `ready` deltaP `18.8189` edge `0.4475` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.1141` n `62` status `ready` deltaP `9.6996` edge `0.2048` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.0748` n `62` status `ready` deltaP `21.6495` edge `0.1119` maxDD `0.0`
- `news_risk_high->index_4h` score `2.3871` n `62` status `ready` deltaP `27.1243` edge `0.0443` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.3278` n `117` status `ready` deltaP `12.4961` edge `0.2071` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.972` n `62` status `ready` deltaP `7.4802` edge `0.15` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8055` n `62` status `ready` deltaP `23.0781` edge `0.0116` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.5456` n `62` status `ready` deltaP `15.7947` edge `0.0833` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1466` n `62` status `ready` deltaP `16.8273` edge `0.0764` maxDD `-0.993`
- `market_context_high->commodity_4h` score `1.0973` n `117` status `ready` deltaP `15.382` edge `0.0589` maxDD `-1.6002`
- `market_context_high->fx_4h` score `0.9104` n `117` status `ready` deltaP `19.6555` edge `0.0205` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.8442` n `62` status `ready` deltaP `27.3529` edge `0.0825` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.7987` n `62` status `ready` deltaP `2.8588` edge `0.0994` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7527` n `117` status `ready` deltaP `12.8423` edge `0.0055` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.6447` n `117` status `ready` deltaP `11.1572` edge `0.019` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.1378` n `117` status `ready` deltaP `-2.0937` edge `0.1978` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0444` n `62` status `ready` deltaP `4.9546` edge `0.0051` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

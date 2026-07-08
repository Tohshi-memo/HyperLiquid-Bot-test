# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T03:07:27.929149+00:00`
- Price records: `672`
- Market context records: `6045`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11125`

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

- `news_risk_high->fx_24h` score `8.0024` n `30` status `ready` deltaP `71.875` edge `0.1877` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2211` n `30` status `ready` deltaP `43.6585` edge `0.0653` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3089` n `30` status `ready` deltaP `27.6746` edge `0.0218` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `2.298` n `30` status `ready` deltaP `24.8611` edge `0.0463` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.4939` n `206` status `ready` deltaP `8.6416` edge `0.1586` maxDD `-2.671`
- `news_risk_high->crypto_alt_24h` score `1.1638` n `30` status `ready` deltaP `25.625` edge `-0.0591` maxDD `-0.5131`
- `news_risk_high->crypto_major_1h` score `1.0048` n `30` status `ready` deltaP `11.2375` edge `0.1006` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3861` n `30` status `ready` deltaP `6.3673` edge `0.0532` maxDD `-1.6923`
- `market_context_high->equity_24h` score `0.3785` n `185` status `ready` deltaP `27.6802` edge `0.5359` maxDD `-40.0859`
- `news_risk_high->index_24h` score `0.1327` n `30` status `ready` deltaP `9.2361` edge `0.0426` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4376` n `206` status `ready` deltaP `3.1306` edge `0.0029` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4741` n `30` status `ready` deltaP `0.6387` edge `-0.0284` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5234` n `206` status `ready` deltaP `0.4578` edge `-0.001` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6763` n `206` status `ready` deltaP `-1.683` edge `-0.0005` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8129` n `206` status `ready` deltaP `4.7003` edge `0.0412` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8205` n `206` status `ready` deltaP `4.555` edge `0.0397` maxDD `-9.3536`
- `market_context_high->index_24h` score `-0.8674` n `185` status `ready` deltaP `4.0109` edge `0.071` maxDD `-5.6021`
- `market_context_high->index_4h` score `-0.9971` n `206` status `ready` deltaP `1.5007` edge `0.0155` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0454` n `30` status `ready` deltaP `-9.4012` edge `-0.0199` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.0631` n `206` status `ready` deltaP `4.0285` edge `0.0033` maxDD `-3.4996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

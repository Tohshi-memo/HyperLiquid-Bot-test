# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T18:07:23.638710+00:00`
- Price records: `672`
- Market context records: `3303`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.8225` n `32` status `ready` deltaP `29.7256` edge `1.2326` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8225` n `32` status `ready` deltaP `29.7256` edge `1.2326` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.272` n `120` status `ready` deltaP `19.6181` edge `2.6831` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.0463` n `120` status `ready` deltaP `31.7014` edge `0.8813` maxDD `-16.1026`
- `market_context_high->commodity_24h` score `8.7581` n `120` status `ready` deltaP `34.6528` edge `0.6278` maxDD `-6.3183`
- `market_context_high->equity_24h` score `7.9325` n `120` status `ready` deltaP `22.9514` edge `1.7056` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.4843` n `32` status `ready` deltaP `10.4421` edge `0.7385` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.4843` n `32` status `ready` deltaP `10.4421` edge `0.7385` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.611` n `32` status `ready` deltaP `14.1006` edge `0.4824` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.611` n `32` status `ready` deltaP `14.1006` edge `0.4824` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.1213` n `181` status `ready` deltaP `19.4987` edge `0.1426` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.0759` n `32` status `ready` deltaP `7.1669` edge `0.3253` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0759` n `32` status `ready` deltaP `7.1669` edge `0.3253` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `1.9268` n `120` status `ready` deltaP `20.3473` edge `2.1813` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.1128` n `32` status `ready` deltaP `1.1433` edge `0.1938` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.1128` n `32` status `ready` deltaP `1.1433` edge `0.1938` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.3079` n `32` status `ready` deltaP `6.6991` edge `0.0633` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3079` n `32` status `ready` deltaP `6.6991` edge `0.0633` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2485` n `32` status `ready` deltaP `0.5988` edge `0.1716` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2485` n `32` status `ready` deltaP `0.5988` edge `0.1716` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

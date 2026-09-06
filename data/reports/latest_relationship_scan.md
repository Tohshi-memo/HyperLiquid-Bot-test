# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T01:37:26.512459+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10963`

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

- `risk_on_high->unknown_4h` score `21.3615` n `140` status `ready` deltaP `-3.0923` edge `2.0013` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.3615` n `140` status `ready` deltaP `-3.0923` edge `2.0013` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.4843` n `235` status `ready` deltaP `1.1326` edge `0.9463` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `5.2869` n `37` status `ready` deltaP `23.6158` edge `0.3101` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9103` n `37` status `ready` deltaP `20.1389` edge `0.1916` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2827` n `37` status `ready` deltaP `16.2657` edge `0.2064` maxDD `-0.9693`
- `market_context_high->equity_24h` score `2.4884` n `155` status `ready` deltaP `14.1756` edge `0.4667` maxDD `-16.9737`
- `news_risk_high->metal_4h` score `2.3747` n `37` status `ready` deltaP `24.1513` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.562` n `37` status `ready` deltaP `12.7853` edge `0.084` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5222` n `37` status `ready` deltaP `7.1605` edge `0.0992` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3436` n `37` status `ready` deltaP `16.0625` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1742` n `37` status `ready` deltaP `14.7233` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.0983` n `37` status `ready` deltaP `5.717` edge `0.0717` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `1.097` n `37` status `ready` deltaP `21.8656` edge `0.0472` maxDD `-3.1244`
- `risk_on_high->crypto_major_24h` score `1.0663` n `78` status `ready` deltaP `10.577` edge `0.7988` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.0663` n `78` status `ready` deltaP `10.577` edge `0.7988` maxDD `-47.9416`
- `news_risk_high->crypto_alt_1h` score `0.7738` n `37` status `ready` deltaP `8.2781` edge `0.0358` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `-0.0132` n `37` status `ready` deltaP `2.7398` edge `0.0135` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `-0.0449` n `37` status `ready` deltaP `5.4257` edge `0.0027` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T02:37:26.993872+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10991`

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

- `risk_on_high->unknown_4h` score `19.9186` n `144` status `ready` deltaP `-3.0996` edge `1.8811` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `19.9186` n `144` status `ready` deltaP `-3.0996` edge `1.8811` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `7.781` n `239` status `ready` deltaP `0.9363` edge `0.889` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `4.9062` n `37` status `ready` deltaP `22.9214` edge `0.283` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9331` n `37` status `ready` deltaP `20.1389` edge `0.1935` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2937` n `37` status `ready` deltaP `16.4181` edge `0.2063` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.4259` n `37` status `ready` deltaP `24.7611` edge `0.0592` maxDD `-0.7692`
- `market_context_high->equity_24h` score `2.2202` n `159` status `ready` deltaP `14.0331` edge `0.4453` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.5739` n `37` status `ready` deltaP `12.935` edge `0.084` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5344` n `37` status `ready` deltaP `7.313` edge `0.0992` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3568` n `37` status `ready` deltaP `16.2122` edge `0.0243` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1994` n `37` status `ready` deltaP `15.0227` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1115` n `37` status `ready` deltaP `5.8667` edge `0.0718` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `1.1006` n `37` status `ready` deltaP `21.8656` edge `0.0475` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8074` n `37` status `ready` deltaP `8.5775` edge `0.0366` maxDD `-0.7867`
- `risk_on_high->crypto_major_24h` score `0.7767` n `78` status `ready` deltaP `9.8825` edge `0.7663` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `0.7767` n `78` status `ready` deltaP `9.8825` edge `0.7663` maxDD `-47.9416`
- `news_risk_high->crypto_alt_4h` score `-0.03` n `37` status `ready` deltaP `2.7398` edge `0.0121` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `-0.0371` n `37` status `ready` deltaP `5.5754` edge `0.0027` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.092` n `145` status `ready` deltaP `5.3861` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

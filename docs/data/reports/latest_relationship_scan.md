# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T01:52:26.760810+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.5976` n `107` status `ready` deltaP `23.2691` edge `0.5398` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.5976` n `107` status `ready` deltaP `23.2691` edge `0.5398` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.1068` n `157` status `ready` deltaP `19.7093` edge `0.447` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0638` n `107` status `ready` deltaP `5.0185` edge `0.1962` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0638` n `107` status `ready` deltaP `5.0185` edge `0.1962` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.8443` n `157` status `ready` deltaP `3.8875` edge `0.1908` maxDD `-2.042`
- `risk_on_high->commodity_24h` score `1.6728` n `100` status `ready` deltaP `13.5903` edge `0.1476` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.6728` n `100` status `ready` deltaP `13.5903` edge `0.1476` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.1577` n `61` status `ready` deltaP `2.1228` edge `0.117` maxDD `-1.1072`
- `risk_on_high->crypto_alt_24h` score `0.8865` n `100` status `ready` deltaP `13.5625` edge `0.7136` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.8865` n `100` status `ready` deltaP `13.5625` edge `0.7136` maxDD `-42.8959`
- `risk_on_high->fx_24h` score `0.3353` n `100` status `ready` deltaP `38.6806` edge `0.0233` maxDD `-4.0544`
- `risk_on_and_context->fx_24h` score `0.3353` n `100` status `ready` deltaP `38.6806` edge `0.0233` maxDD `-4.0544`
- `news_risk_high->commodity_4h` score `0.1775` n `61` status `ready` deltaP `6.2725` edge `0.0226` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1487` n `61` status `ready` deltaP `10.6533` edge `0.0007` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.1168` n `157` status `ready` deltaP `8.716` edge `0.0166` maxDD `-1.5315`
- `risk_on_high->commodity_1h` score `-0.0095` n `107` status `ready` deltaP `5.4718` edge `0.0145` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0095` n `107` status `ready` deltaP `5.4718` edge `0.0145` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0719` n `107` status `ready` deltaP `5.399` edge `-0.0007` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0719` n `107` status `ready` deltaP `5.399` edge `-0.0007` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

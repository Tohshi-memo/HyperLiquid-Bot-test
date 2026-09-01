# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T00:37:24.390477+00:00`
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

- `risk_on_high->unknown_4h` score `7.6756` n `107` status `ready` deltaP `23.2691` edge `0.5462` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.6756` n `107` status `ready` deltaP `23.2691` edge `0.5462` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.1284` n `159` status `ready` deltaP `19.9657` edge `0.447` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.0313` n `107` status `ready` deltaP `4.8688` edge `0.1945` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.0313` n `107` status `ready` deltaP `4.8688` edge `0.1945` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `1.8075` n `159` status `ready` deltaP `4.2105` edge `0.1856` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.6508` n `95` status `ready` deltaP `13.3004` edge `0.1477` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.6508` n `95` status `ready` deltaP `13.3004` edge `0.1477` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.1257` n `61` status `ready` deltaP `1.9731` edge `0.1153` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `0.6235` n `95` status `ready` deltaP `40.7072` edge `0.0232` maxDD `-3.8386`
- `risk_on_and_context->fx_24h` score `0.6235` n `95` status `ready` deltaP `40.7072` edge `0.0232` maxDD `-3.8386`
- `risk_on_high->crypto_alt_24h` score `0.4407` n `95` status `ready` deltaP `12.4306` edge `0.664` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.4407` n `95` status `ready` deltaP `12.4306` edge `0.664` maxDD `-42.8959`
- `news_risk_high->commodity_4h` score `0.1799` n `61` status `ready` deltaP `6.2725` edge `0.0229` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1609` n `61` status `ready` deltaP `10.8057` edge `0.0007` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.148` n `159` status `ready` deltaP `9.031` edge `0.0171` maxDD `-1.5315`
- `risk_on_high->commodity_1h` score `-0.0189` n `107` status `ready` deltaP `5.3221` edge `0.0143` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0189` n `107` status `ready` deltaP `5.3221` edge `0.0143` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0633` n `107` status `ready` deltaP `5.5487` edge `-0.0006` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0633` n `107` status `ready` deltaP `5.5487` edge `-0.0006` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

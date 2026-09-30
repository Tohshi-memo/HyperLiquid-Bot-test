# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T08:07:34.255387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7466`

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

- `news_risk_high->unknown_24h` score `914.4748` n `135` status `ready` deltaP `1.9097` edge `76.1935` maxDD `0.0`
- `market_context_high->unknown_1h` score `611.6348` n `38` status `ready` deltaP `9.7305` edge `50.9047` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.0121` n `135` status `ready` deltaP `28.5532` edge `1.3316` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.9658` n `135` status `ready` deltaP `27.5116` edge `0.7153` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.5861` n `135` status `ready` deltaP `23.9931` edge `0.7876` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.745` n `135` status `ready` deltaP `33.7037` edge `0.1352` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.3772` n `135` status `ready` deltaP `25.8796` edge `0.2363` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.8746` n `135` status `ready` deltaP `29.1711` edge `0.2052` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.7987` n `135` status `ready` deltaP `10.8074` edge `0.3438` maxDD `-15.9436`
- `market_context_high->crypto_alt_1h` score `1.634` n `38` status `ready` deltaP `9.9275` edge `0.1363` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `1.5786` n `38` status `ready` deltaP `9.0057` edge `0.1325` maxDD `-3.546`
- `news_risk_high->crypto_alt_1h` score `1.0958` n `135` status `ready` deltaP `9.4012` edge `0.1197` maxDD `-4.2849`
- `market_context_high->equity_1h` score `1.0463` n `38` status `ready` deltaP `15.041` edge `0.0764` maxDD `-2.4027`
- `news_risk_high->equity_1h` score `0.8888` n `135` status `ready` deltaP `9.2515` edge `0.0747` maxDD `-1.6514`
- `market_context_high->metal_1h` score `0.6037` n `38` status `ready` deltaP `11.0384` edge `0.0259` maxDD `-0.4338`
- `market_context_high->fx_1h` score `0.529` n `38` status `ready` deltaP `12.6851` edge `0.0055` maxDD `-0.113`
- `news_risk_high->index_1h` score `0.479` n `135` status `ready` deltaP `8.6682` edge `0.0109` maxDD `-0.302`
- `market_context_high->index_1h` score `0.4503` n `38` status `ready` deltaP `8.0444` edge `0.0176` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.1746` n `135` status `ready` deltaP `6.4916` edge `0.0275` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.6067` n `135` status `ready` deltaP `1.8906` edge `0.0651` maxDD `-7.2607`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

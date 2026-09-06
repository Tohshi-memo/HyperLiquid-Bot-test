# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T15:07:24.572155+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9975`

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

- `risk_on_high->unknown_24h` score `116.8109` n `109` status `ready` deltaP `23.885` edge `9.586` maxDD `-0.2126`
- `risk_on_and_context->unknown_24h` score `116.8109` n `109` status `ready` deltaP `23.885` edge `9.586` maxDD `-0.2126`
- `risk_on_high->crypto_major_24h` score `10.7724` n `109` status `ready` deltaP `23.6908` edge `1.1712` maxDD `-27.5153`
- `risk_on_and_context->crypto_major_24h` score `10.7724` n `109` status `ready` deltaP `23.6908` edge `1.1712` maxDD `-27.5153`
- `market_context_high->equity_24h` score `3.0996` n `196` status `ready` deltaP `16.0218` edge `0.3572` maxDD `-9.4569`
- `risk_on_high->crypto_alt_24h` score `2.304` n `109` status `ready` deltaP `11.96` edge `0.5172` maxDD `-24.3945`
- `risk_on_and_context->crypto_alt_24h` score `2.304` n `109` status `ready` deltaP `11.96` edge `0.5172` maxDD `-24.3945`
- `market_context_high->crypto_alt_24h` score `0.9291` n `196` status `ready` deltaP `14.4876` edge `0.4111` maxDD `-25.754`
- `risk_on_high->equity_24h` score `0.5879` n `109` status `ready` deltaP `7.47` edge `0.2049` maxDD `-9.4569`
- `risk_on_and_context->equity_24h` score `0.5879` n `109` status `ready` deltaP `7.47` edge `0.2049` maxDD `-9.4569`
- `risk_on_high->index_1h` score `-0.0449` n `134` status `ready` deltaP `6.2629` edge `-0.0028` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0449` n `134` status `ready` deltaP `6.2629` edge `-0.0028` maxDD `-0.5764`
- `risk_on_high->crypto_alt_1h` score `-0.1106` n `134` status `ready` deltaP `3.4163` edge `0.0697` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1106` n `134` status `ready` deltaP `3.4163` edge `0.0697` maxDD `-5.4685`
- `risk_on_high->metal_1h` score `-0.2184` n `134` status `ready` deltaP `6.7253` edge `-0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.2184` n `134` status `ready` deltaP `6.7253` edge `-0.0016` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.3936` n `134` status `ready` deltaP `7.2907` edge `-0.0116` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.3936` n `134` status `ready` deltaP `7.2907` edge `-0.0116` maxDD `-2.6638`
- `market_context_high->index_24h` score `-0.4554` n `196` status `ready` deltaP `13.5452` edge `0.0754` maxDD `-5.6252`
- `risk_on_high->commodity_1h` score `-0.5032` n `134` status `ready` deltaP `1.1731` edge `0.0006` maxDD `-1.0281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

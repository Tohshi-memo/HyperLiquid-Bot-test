# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T16:22:27.651567+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10109`

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

- `risk_on_high->unknown_24h` score `131.0887` n `108` status `ready` deltaP `23.8426` edge `10.7761` maxDD `-0.2126`
- `risk_on_and_context->unknown_24h` score `131.0887` n `108` status `ready` deltaP `23.8426` edge `10.7761` maxDD `-0.2126`
- `risk_on_high->crypto_major_24h` score `13.6127` n `108` status `ready` deltaP `27.2569` edge `1.2651` maxDD `-19.6602`
- `risk_on_and_context->crypto_major_24h` score `13.6127` n `108` status `ready` deltaP `27.2569` edge `1.2651` maxDD `-19.6602`
- `risk_on_high->crypto_alt_24h` score `4.9325` n `108` status `ready` deltaP `15.5093` edge `0.6181` maxDD `-18.5032`
- `risk_on_and_context->crypto_alt_24h` score `4.9325` n `108` status `ready` deltaP `15.5093` edge `0.6181` maxDD `-18.5032`
- `market_context_high->equity_24h` score `4.0496` n `196` status `ready` deltaP `17.7048` edge `0.3701` maxDD `-6.7198`
- `market_context_high->crypto_alt_24h` score `2.7207` n `196` status `ready` deltaP `16.1707` edge `0.4547` maxDD `-19.8626`
- `risk_on_high->equity_24h` score `1.9335` n `108` status `ready` deltaP `11.0533` edge `0.2381` maxDD `-6.7198`
- `risk_on_and_context->equity_24h` score `1.9335` n `108` status `ready` deltaP `11.0533` edge `0.2381` maxDD `-6.7198`
- `market_context_high->index_24h` score `0.1393` n `196` status `ready` deltaP `15.2282` edge `0.0795` maxDD `-4.5531`
- `risk_on_high->index_1h` score `-0.1164` n `130` status `ready` deltaP `4.977` edge `-0.0034` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1164` n `130` status `ready` deltaP `4.977` edge `-0.0034` maxDD `-0.5764`
- `risk_on_high->index_24h` score `-0.2738` n `108` status `ready` deltaP `10.0695` edge `0.0481` maxDD `-4.0437`
- `risk_on_and_context->index_24h` score `-0.2738` n `108` status `ready` deltaP `10.0695` edge `0.0481` maxDD `-4.0437`
- `risk_on_high->crypto_alt_1h` score `-0.328` n `130` status `ready` deltaP `2.3031` edge `0.059` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.328` n `130` status `ready` deltaP `2.3031` edge `0.059` maxDD `-5.4685`
- `risk_on_high->metal_1h` score `-0.3286` n `130` status `ready` deltaP `4.8319` edge `-0.0031` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.3286` n `130` status `ready` deltaP `4.8319` edge `-0.0031` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.4645` n `130` status `ready` deltaP `6.3612` edge `-0.0145` maxDD `-2.6638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

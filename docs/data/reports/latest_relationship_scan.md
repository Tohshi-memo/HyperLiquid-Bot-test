# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T09:52:29.965411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `news_risk_high->unknown_24h` score `574.9348` n `135` status `ready` deltaP `1.9097` edge `47.8985` maxDD `0.0`
- `market_context_high->unknown_1h` score `477.0209` n `45` status `ready` deltaP `7.658` edge `39.7056` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `398.6673` n `33` status `ready` deltaP `8.2317` edge `33.1674` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.2358` n `135` status `ready` deltaP `27.6852` edge `1.2727` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.4366` n `135` status `ready` deltaP `26.2963` edge `0.6793` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.1445` n `135` status `ready` deltaP `23.9931` edge `0.7508` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.5637` n `135` status `ready` deltaP `32.4884` edge `0.1282` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.1659` n `135` status `ready` deltaP `24.6643` edge `0.2268` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.7441` n `135` status `ready` deltaP `28.409` edge `0.1994` maxDD `-9.143`
- `market_context_high->fx_4h` score `2.7045` n `33` status `ready` deltaP `31.1299` edge `0.0309` maxDD `-0.0449`
- `market_context_high->crypto_alt_1h` score `2.3747` n `45` status `ready` deltaP `13.2468` edge `0.1759` maxDD `-3.6387`
- `market_context_high->crypto_major_4h` score `1.9588` n `33` status `ready` deltaP `4.1067` edge `0.2062` maxDD `-3.294`
- `market_context_high->crypto_major_1h` score `1.8662` n `45` status `ready` deltaP `11.0712` edge `0.1427` maxDD `-3.546`
- `news_risk_high->crypto_alt_4h` score `1.5527` n `135` status `ready` deltaP `9.8927` edge `0.3294` maxDD `-15.9436`
- `market_context_high->fx_1h` score `1.1066` n `45` status `ready` deltaP `16.4138` edge `0.0092` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `0.9879` n `135` status `ready` deltaP `8.8024` edge `0.1147` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.908` n `135` status `ready` deltaP `9.4012` edge `0.0753` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.4826` n `135` status `ready` deltaP `8.6682` edge `0.0112` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.3769` n `45` status `ready` deltaP `7.179` edge `0.0555` maxDD `-2.4027`
- `market_context_high->metal_4h` score `-0.0749` n `33` status `ready` deltaP `13.5209` edge `-0.0254` maxDD `-2.614`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

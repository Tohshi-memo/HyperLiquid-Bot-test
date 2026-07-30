# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T11:22:29.129357+00:00`
- Price records: `672`
- Market context records: `8404`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6252.6812` n `52` status `ready` deltaP `38.6619` edge `520.8411` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.1248` n `52` status `ready` deltaP `25.6098` edge `0.4827` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.82` n `52` status `ready` deltaP `20.6817` edge `0.128` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5405` n `52` status `ready` deltaP `21.189` edge `0.0895` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.7723` n `52` status `ready` deltaP `7.8447` edge `0.2443` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6879` n `52` status `ready` deltaP `12.9088` edge `0.098` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6182` n `52` status `ready` deltaP `11.4118` edge `0.0985` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3592` n `52` status `ready` deltaP `16.4165` edge `0.204` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.5051` n `52` status `ready` deltaP `5.652` edge `0.0512` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2277` n `52` status `ready` deltaP `4.445` edge `0.0182` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0899` n `52` status `ready` deltaP `5.4929` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2923` n `52` status `ready` deltaP `1.6007` edge `0.0053` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4841` n `52` status `ready` deltaP `4.1979` edge `0.0057` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9872` n `52` status `ready` deltaP `-6.9208` edge `-0.0409` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7577` n `52` status `ready` deltaP `-27.7244` edge `-0.0628` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.088` n `52` status `ready` deltaP `-31.5838` edge `-0.1864` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.5594` n `52` status `ready` deltaP `-27.2748` edge `-0.2007` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.3299` n `52` status `ready` deltaP `-25.2938` edge `-0.3086` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.3368` n `52` status `ready` deltaP `-11.2179` edge `-0.3593` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.5551` n `52` status `ready` deltaP `-23.2105` edge `-0.9373` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

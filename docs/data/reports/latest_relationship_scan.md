# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T02:37:26.162548+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11041`

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

- `market_context_high->unknown_1h` score `85.1288` n `47` status `ready` deltaP `9.3675` edge `7.0387` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.0305` n `47` status `ready` deltaP `30.4226` edge `3.839` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.4404` n `47` status `ready` deltaP `24.782` edge `2.4928` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.029` n `47` status `ready` deltaP `34.7628` edge `1.9729` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2652` n `47` status `ready` deltaP `38.9295` edge `0.4422` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `4.6426` n `116` status `ready` deltaP `-0.1703` edge `0.4099` maxDD `-0.7504`
- `market_context_high->metal_24h` score `4.5351` n `47` status `ready` deltaP `38.1834` edge `0.1472` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3333` n `61` status `ready` deltaP `31.0195` edge `0.1058` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9607` n `47` status `ready` deltaP `33.8739` edge `0.0363` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5091` n `47` status `ready` deltaP `17.1445` edge `0.1366` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.1055` n `116` status `ready` deltaP `11.5941` edge `0.1491` maxDD `-1.7416`
- `news_risk_high->crypto_major_1h` score `1.6277` n `116` status `ready` deltaP `13.6899` edge `0.1003` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.2198` n `116` status `ready` deltaP `16.3741` edge `0.021` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9188` n `47` status `ready` deltaP `14.161` edge `0.01` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8827` n `47` status `ready` deltaP `11.0173` edge `0.0404` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.565` n `47` status `ready` deltaP `7.5538` edge `0.0635` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.2997` n `47` status `ready` deltaP `8.1634` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->equity_1h` score `0.1234` n `116` status `ready` deltaP `4.5427` edge `0.038` maxDD `-2.6402`
- `news_risk_high->fx_4h` score `0.089` n `104` status `ready` deltaP `9.3574` edge `0.0169` maxDD `-0.763`
- `market_context_high->metal_1h` score `-0.0443` n `47` status `ready` deltaP `2.3793` edge `0.0101` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

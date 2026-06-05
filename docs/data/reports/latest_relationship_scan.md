# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T14:37:31.823945+00:00`
- Price records: `672`
- Market context records: `2978`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6956`

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

- `market_context_high->commodity_24h` score `10.8979` n `105` status `ready` deltaP `39.7718` edge `0.6611` maxDD `-0.7805`
- `market_context_high->crypto_alt_24h` score `10.185` n `105` status `ready` deltaP `7.3562` edge `1.6484` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `10.0178` n `105` status `ready` deltaP `15.9276` edge `0.7751` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.8341` n `105` status `ready` deltaP `16.0467` edge `0.6629` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.0676` n `105` status `ready` deltaP `16.0416` edge `0.3301` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.8457` n `106` status `ready` deltaP `15.4769` edge `0.1729` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.0974` n `106` status `ready` deltaP `20.2974` edge `0.1183` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `1.7124` n `106` status `ready` deltaP `13.7425` edge `0.1158` maxDD `-2.8438`
- `market_context_high->equity_1h` score `1.1817` n `106` status `ready` deltaP `8.5668` edge `0.0747` maxDD `-1.0004`
- `market_context_high->index_1h` score `0.7913` n `106` status `ready` deltaP `9.9735` edge `0.0386` maxDD `-0.7983`
- `market_context_high->crypto_alt_4h` score `0.4714` n `106` status `ready` deltaP `21.7154` edge `0.3718` maxDD `-30.8239`
- `market_context_high->crypto_alt_1h` score `-0.018` n `106` status `ready` deltaP `9.2843` edge `0.0993` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.1718` n `106` status `ready` deltaP `9.4481` edge `0.0686` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.2044` n `106` status `ready` deltaP `-0.0593` edge `0.014` maxDD `-1.5182`
- `market_context_high->fx_1h` score `-0.444` n `106` status `ready` deltaP `-1.3021` edge `0.0024` maxDD `-0.1244`
- `market_context_high->fx_4h` score `-0.9999` n `106` status `ready` deltaP `-7.5184` edge `-0.0002` maxDD `-0.5631`
- `market_context_high->unknown_4h` score `-1.0511` n `106` status `ready` deltaP `-0.4286` edge `0.0206` maxDD `-3.7602`
- `market_context_high->metal_1h` score `-1.3357` n `106` status `ready` deltaP `-3.1607` edge `-0.0015` maxDD `-3.4325`
- `market_context_high->fx_24h` score `-1.37` n `105` status `ready` deltaP `-8.9484` edge `-0.0288` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.3837` n `106` status `ready` deltaP `2.4715` edge `-0.0587` maxDD `-3.1801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

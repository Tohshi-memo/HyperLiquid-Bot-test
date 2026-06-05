# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T05:52:22.896028+00:00`
- Price records: `672`
- Market context records: `2941`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6940`

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

- `market_context_high->crypto_alt_24h` score `16.4074` n `140` status `ready` deltaP `15.8036` edge `1.6536` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.8734` n `140` status `ready` deltaP `18.3283` edge `0.7343` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.9823` n `140` status `ready` deltaP `16.3096` edge `0.5196` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.8042` n `140` status `ready` deltaP `13.869` edge `0.2393` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `2.2` n `140` status `ready` deltaP `16.374` edge `0.368` maxDD `-11.8393`
- `market_context_high->equity_4h` score `0.8219` n `141` status `ready` deltaP `8.183` edge `0.1519` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.7156` n `141` status `ready` deltaP `14.6384` edge `0.0783` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.2109` n `141` status `ready` deltaP `4.3516` edge `0.0939` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `0.0808` n `141` status `ready` deltaP `16.2353` edge `0.3588` maxDD `-30.8239`
- `market_context_high->index_1h` score `-0.0054` n `141` status `ready` deltaP `4.5314` edge `0.0185` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.4321` n `141` status `ready` deltaP `0.568` edge `0.0435` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4813` n `141` status `ready` deltaP `5.5793` edge `0.0771` maxDD `-10.747`
- `market_context_high->unknown_1h` score `-0.5439` n `141` status `ready` deltaP `2.6638` edge `0.01` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-0.5551` n `141` status `ready` deltaP `-0.7326` edge `0.003` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.6217` n `141` status `ready` deltaP `5.7364` edge `0.069` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.6524` n `141` status `ready` deltaP `-1.1105` edge `-0.0009` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6705` n `141` status `ready` deltaP `-0.0478` edge `0.0031` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.9343` n `141` status `ready` deltaP `-1.0174` edge `0.0068` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2575` n `141` status `ready` deltaP `1.8001` edge `0.0188` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3514` n `140` status `ready` deltaP `-2.0436` edge `-0.0118` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

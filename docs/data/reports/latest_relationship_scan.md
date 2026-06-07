# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T23:37:23.081812+00:00`
- Price records: `672`
- Market context records: `3227`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.0692` n `102` status `ready` deltaP `19.0563` edge `2.6666` maxDD `-70.5257`
- `market_context_high->commodity_24h` score `13.8778` n `102` status `ready` deltaP `49.5609` edge `0.8689` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.7624` n `102` status `ready` deltaP `32.547` edge `0.852` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.5676` n `102` status `ready` deltaP `19.1278` edge `1.5561` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.012` n `128` status `ready` deltaP `20.3696` edge `0.161` maxDD `-1.9973`
- `market_context_high->crypto_major_24h` score `1.8917` n `102` status `ready` deltaP `22.2631` edge `2.195` maxDD `-154.072`
- `market_context_high->commodity_1h` score `0.1048` n `140` status `ready` deltaP `5.4149` edge `0.0219` maxDD `-1.9413`
- `market_context_high->unknown_4h` score `-0.656` n `128` status `ready` deltaP `8.8605` edge `0.0834` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.789` n `140` status `ready` deltaP `3.9948` edge `0.0985` maxDD `-15.1032`
- `market_context_high->crypto_alt_1h` score `-0.7946` n `140` status `ready` deltaP `3.8238` edge `0.0981` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.9461` n `140` status `ready` deltaP `2.8101` edge `0.0087` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.9491` n `140` status `ready` deltaP `3.7553` edge `0.0102` maxDD `-8.8863`
- `market_context_high->fx_24h` score `-1.2453` n `102` status `ready` deltaP `-3.3598` edge `-0.0181` maxDD `-1.8657`
- `market_context_high->index_4h` score `-1.4383` n `128` status `ready` deltaP `9.6609` edge `0.0421` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.8918` n `140` status `ready` deltaP `-12.3396` edge `-0.0059` maxDD `-0.8923`
- `market_context_high->fx_4h` score `-2.2122` n `128` status `ready` deltaP `-12.2523` edge `-0.0124` maxDD `-1.5551`
- `market_context_high->metal_1h` score `-2.3331` n `140` status `ready` deltaP `-3.9863` edge `-0.0184` maxDD `-8.2892`
- `market_context_high->unknown_1h` score `-2.8832` n `140` status `ready` deltaP `1.5227` edge `-0.1319` maxDD `-17.8311`
- `market_context_high->equity_4h` score `-3.4611` n `128` status `ready` deltaP `10.8804` edge `0.0143` maxDD `-36.7784`
- `market_context_high->metal_4h` score `-4.2009` n `128` status `ready` deltaP `-11.9475` edge `-0.0348` maxDD `-24.9302`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

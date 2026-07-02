# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T05:52:29.940970+00:00`
- Price records: `672`
- Market context records: `5425`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `market_context_high->crypto_major_24h` score `4.7331` n `186` status `ready` deltaP `20.4973` edge `0.7118` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.5199` n `186` status `ready` deltaP `11.4248` edge `0.6541` maxDD `-21.6219`
- `market_context_high->crypto_major_4h` score `3.9094` n `197` status `ready` deltaP `16.9091` edge `0.4423` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0796` n `197` status `ready` deltaP `12.2872` edge `0.3388` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.5991` n `197` status `ready` deltaP `12.3831` edge `0.2979` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4759` n `197` status `ready` deltaP `8.2776` edge `0.081` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1327` n `197` status `ready` deltaP `6.6446` edge `0.0161` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0376` n `186` status `ready` deltaP `8.8598` edge `0.0336` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.2158` n `197` status `ready` deltaP `1.6011` edge `0.0675` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2337` n `197` status `ready` deltaP `3.2805` edge `0.0832` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.402` n `197` status `ready` deltaP `2.7334` edge `0.0158` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5905` n `197` status `ready` deltaP `-0.0198` edge `-0.0002` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.9504` n `197` status `ready` deltaP `6.3483` edge `0.0394` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.1356` n `186` status `ready` deltaP `15.7762` edge `0.0988` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1529` n `197` status `ready` deltaP `0.6515` edge `0.0021` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.5148` n `197` status `ready` deltaP `-3.6574` edge `-0.0074` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.7345` n `197` status `ready` deltaP `-9.0341` edge `-0.0379` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3997` n `197` status `ready` deltaP `-8.0127` edge `-0.0494` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.8087` n `186` status `ready` deltaP `11.2735` edge `0.3105` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.299` n `186` status `ready` deltaP `-5.4603` edge `-0.1616` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

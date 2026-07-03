# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T18:07:27.805555+00:00`
- Price records: `672`
- Market context records: `5582`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11423`

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

- `market_context_high->equity_24h` score `4.0603` n `174` status `ready` deltaP `15.0084` edge `0.7462` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1656` n `197` status `ready` deltaP `11.4716` edge `0.2499` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.9162` n `174` status `ready` deltaP `18.1394` edge `0.0528` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.5874` n `197` status `ready` deltaP `6.9503` edge `0.1667` maxDD `-9.46`
- `market_context_high->crypto_major_24h` score `0.5759` n `174` status `ready` deltaP `13.2783` edge `0.4135` maxDD `-29.6555`
- `market_context_high->equity_4h` score `0.5518` n `197` status `ready` deltaP `5.6774` edge `0.172` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.1916` n `209` status `ready` deltaP `5.9136` edge `0.0367` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.195` n `209` status `ready` deltaP `3.7941` edge `0.0078` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3186` n `209` status `ready` deltaP `0.7764` edge `0.0008` maxDD `-0.4122`
- `market_context_high->fx_4h` score `-0.3764` n `197` status `ready` deltaP `4.9686` edge `0.0089` maxDD `-0.8712`
- `market_context_high->metal_1h` score `-0.5243` n `209` status `ready` deltaP `-0.0602` edge `0.0007` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.612` n `209` status `ready` deltaP `0.9233` edge `0.039` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7368` n `209` status `ready` deltaP `2.7519` edge `0.0448` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.2145` n `209` status `ready` deltaP `-2.3938` edge `-0.0087` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5407` n `197` status `ready` deltaP `2.5845` edge `0.0153` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.1145` n `174` status `ready` deltaP `12.3444` edge `0.0453` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0258` n `197` status `ready` deltaP `-13.2994` edge `-0.0609` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2955` n `197` status `ready` deltaP `-5.9854` edge `-0.0505` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.9545` n `174` status `ready` deltaP `-8.3273` edge `-0.2282` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.5025` n `174` status `ready` deltaP `3.0651` edge `0.0574` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

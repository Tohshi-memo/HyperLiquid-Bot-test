# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T18:37:30.496001+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `risk_on_high->unknown_4h` score `30.5812` n `133` status `ready` deltaP `12.5046` edge `2.5269` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `30.5812` n `133` status `ready` deltaP `12.5046` edge `2.5269` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `23.8162` n `167` status `ready` deltaP `14.1029` edge `1.9602` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `16.4141` n `133` status `ready` deltaP `1.1919` edge `1.4176` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `16.4141` n `133` status `ready` deltaP `1.1919` edge `1.4176` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.9342` n `167` status `ready` deltaP `1.6467` edge `1.0466` maxDD `-2.0446`
- `market_context_high->equity_24h` score `2.0974` n `127` status `ready` deltaP `18.9072` edge `0.4833` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `1.7594` n `67` status `ready` deltaP `18.4831` edge `0.3958` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `1.6145` n `107` status `ready` deltaP `14.1534` edge `0.4547` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.6145` n `107` status `ready` deltaP `14.1534` edge `0.4547` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `1.1516` n `67` status `ready` deltaP `14.9798` edge `0.4861` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `0.848` n `67` status `ready` deltaP `6.5791` edge `0.3116` maxDD `-15.4056`
- `news_risk_high->commodity_4h` score `0.4284` n `67` status `ready` deltaP `7.7767` edge `0.039` maxDD `-0.8733`
- `news_risk_high->fx_4h` score `0.0629` n `67` status `ready` deltaP `9.9563` edge `0.0045` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.0595` n `133` status `ready` deltaP `11.6643` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0595` n `133` status `ready` deltaP `11.6643` edge `0.0011` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0858` n `67` status `ready` deltaP `4.176` edge `-0.0035` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.113` n `67` status `ready` deltaP `5.0563` edge `0.0015` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.124` n `133` status `ready` deltaP `4.5912` edge `-0.002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.124` n `133` status `ready` deltaP `4.5912` edge `-0.002` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

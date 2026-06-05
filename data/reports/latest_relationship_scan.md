# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T11:37:22.206638+00:00`
- Price records: `672`
- Market context records: `2965`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.082` n `117` status `ready` deltaP `11.2313` edge `1.7403` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `9.1632` n `117` status `ready` deltaP `16.7201` edge `0.6986` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `8.0` n `117` status `ready` deltaP `30.2751` edge `0.5493` maxDD `-2.7572`
- `market_context_high->equity_24h` score `7.6099` n `117` status `ready` deltaP `16.8937` edge `0.7219` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.4671` n `117` status `ready` deltaP `14.4899` edge `0.2904` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.3615` n `118` status `ready` deltaP `16.7347` edge `0.2075` maxDD `-0.7819`
- `market_context_high->crypto_alt_4h` score `2.8423` n `118` status `ready` deltaP `24.0285` edge `0.5328` maxDD `-30.8239`
- `market_context_high->index_4h` score `1.4046` n `118` status `ready` deltaP `15.4919` edge `0.0926` maxDD `-1.9733`
- `market_context_high->equity_1h` score `0.7696` n `118` status `ready` deltaP `5.6277` edge `0.0601` maxDD `-1.012`
- `market_context_high->unknown_4h` score `0.356` n `118` status `ready` deltaP `4.5602` edge `0.1046` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0849` n `118` status `ready` deltaP `5.8307` edge `0.0201` maxDD `-1.1802`
- `market_context_high->crypto_alt_1h` score `0.072` n `118` status `ready` deltaP `8.0255` edge `0.116` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.1181` n `118` status `ready` deltaP `7.6296` edge `0.0876` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.2308` n `118` status `ready` deltaP `1.0936` edge `0.0042` maxDD `-0.1244`
- `market_context_high->commodity_4h` score `-0.4505` n `118` status `ready` deltaP `6.852` edge `0.0484` maxDD `-7.8132`
- `market_context_high->commodity_1h` score `-0.5979` n `118` status `ready` deltaP `-1.6974` edge `-0.0028` maxDD `-3.3365`
- `market_context_high->crypto_major_4h` score `-0.6544` n `118` status `ready` deltaP `11.8412` edge `0.3497` maxDD `-33.6701`
- `market_context_high->unknown_1h` score `-0.7189` n `118` status `ready` deltaP `2.1415` edge `-0.0011` maxDD `-3.1801`
- `market_context_high->metal_1h` score `-0.7189` n `118` status `ready` deltaP `-0.8449` edge `0.0022` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-1.0804` n `118` status `ready` deltaP `-2.8292` edge `0.0067` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

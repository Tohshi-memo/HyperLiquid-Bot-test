# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T03:07:26.903825+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6595`

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

- `market_context_high->equity_24h` score `11.0621` n `32` status `ready` deltaP `18.2292` edge `1.0376` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.9253` n `32` status `ready` deltaP `9.7222` edge `0.2377` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.5306` n `32` status `ready` deltaP `18.4028` edge `0.1198` maxDD `-2.3671`
- `market_context_high->equity_1h` score `1.1471` n `68` status `ready` deltaP `5.9088` edge `0.1759` maxDD `-5.5762`
- `market_context_high->metal_1h` score `1.0567` n `68` status `ready` deltaP `12.6365` edge `0.0366` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.6319` n `32` status `ready` deltaP `10.2431` edge `-0.0068` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.4252` n `56` status `ready` deltaP `7.4912` edge `0.0571` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.1463` n `56` status `ready` deltaP `0.6751` edge `0.0549` maxDD `-1.1102`
- `market_context_high->commodity_1h` score `0.0348` n `68` status `ready` deltaP `6.5516` edge `0.018` maxDD `-1.7019`
- `market_context_high->index_4h` score `-0.1102` n `56` status `ready` deltaP `10.1045` edge `0.0163` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.1914` n `68` status `ready` deltaP `2.9676` edge `0.0226` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.3769` n `68` status `ready` deltaP `12.4427` edge `0.058` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.9171` n `68` status `ready` deltaP `-11.0954` edge `-0.0042` maxDD `-0.486`
- `market_context_high->fx_4h` score `-1.0899` n `56` status `ready` deltaP `-3.5932` edge `-0.0014` maxDD `-1.1502`
- `market_context_high->metal_24h` score `-1.4965` n `32` status `ready` deltaP `1.0417` edge `-0.1435` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.6929` n `68` status `ready` deltaP `3.4431` edge `-0.0301` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-4.5206` n `56` status `ready` deltaP `5.1394` edge `-0.033` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.7074` n `32` status `ready` deltaP `-4.8611` edge `0.0044` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-7.6178` n `56` status `ready` deltaP `5.6185` edge `-0.2054` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-8.8126` n `32` status `ready` deltaP `-18.75` edge `-0.1515` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

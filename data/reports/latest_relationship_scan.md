# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T05:52:21.424266+00:00`
- Price records: `672`
- Market context records: `2014`
- Flow alert records: `7688`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9107`

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

- `market_context_high->crypto_major_4h` score `8.9429` n `209` status `ready` deltaP `31.0261` edge `0.5914` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4534` n `209` status `ready` deltaP `24.9628` edge `0.6525` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.8466` n `209` status `ready` deltaP `19.1745` edge `0.4343` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.8582` n `209` status `ready` deltaP `16.4007` edge `0.2383` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5122` n `209` status `ready` deltaP `12.4094` edge `0.1419` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.2712` n `209` status `ready` deltaP `11.9843` edge `0.0944` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2203` n `209` status `ready` deltaP `10.0142` edge `0.1463` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.8559` n `188` status `ready` deltaP `15.9101` edge `0.4973` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.544` n `188` status `ready` deltaP `13.5347` edge `0.1977` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.4241` n `188` status `ready` deltaP `14.7734` edge `0.4267` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.1494` n `209` status `ready` deltaP `6.4479` edge `0.0483` maxDD `-2.6402`
- `market_context_high->fx_24h` score `0.0124` n `188` status `ready` deltaP `14.0156` edge `0.026` maxDD `-2.1393`
- `market_context_high->index_24h` score `-0.0209` n `188` status `ready` deltaP `3.0749` edge `0.1006` maxDD `-4.1604`
- `market_context_high->unknown_1h` score `-0.0225` n `209` status `ready` deltaP `3.5534` edge `0.0464` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.3965` n `209` status `ready` deltaP `1.6045` edge `0.0153` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.8107` n `209` status `ready` deltaP `-0.838` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0208` n `209` status `ready` deltaP `-6.1843` edge `-0.0015` maxDD `-1.0513`
- `market_context_high->metal_1h` score `-1.0501` n `209` status `ready` deltaP `2.8694` edge `0.0121` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.5437` n `209` status `ready` deltaP `7.2639` edge `0.0852` maxDD `-11.9812`
- `market_context_high->crypto_major_24h` score `-1.7151` n `188` status `ready` deltaP `16.4639` edge `0.6059` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

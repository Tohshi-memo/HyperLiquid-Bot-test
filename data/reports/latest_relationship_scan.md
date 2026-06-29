# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T08:52:35.002647+00:00`
- Price records: `672`
- Market context records: `5128`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `29.1637` n `63` status `ready` deltaP `28.7947` edge `2.2726` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.7202` n `127` status `ready` deltaP `10.07` edge `0.7237` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.2864` n `118` status `ready` deltaP `19.8326` edge `0.5772` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.957` n `118` status `ready` deltaP `14.1148` edge `0.4789` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.4708` n `118` status `ready` deltaP `11.8773` edge `0.4393` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.3527` n `63` status `ready` deltaP `20.2381` edge `0.1479` maxDD `-5.418`
- `market_context_high->equity_1h` score `0.7769` n `127` status `ready` deltaP `8.3785` edge `0.0682` maxDD `-2.745`
- `market_context_high->crypto_alt_1h` score `0.6995` n `127` status `ready` deltaP `4.8517` edge `0.1221` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.6333` n `118` status `ready` deltaP `7.7615` edge `0.1649` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.6277` n `127` status `ready` deltaP `7.208` edge `0.1288` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.1455` n `127` status `ready` deltaP `7.0972` edge `0.0228` maxDD `-1.4501`
- `market_context_high->index_1h` score `0.0516` n `127` status `ready` deltaP `5.9055` edge `0.0153` maxDD `-1.0296`
- `market_context_high->metal_24h` score `-0.5017` n `63` status `ready` deltaP `0.9424` edge `0.1773` maxDD `-14.4989`
- `market_context_high->commodity_1h` score `-0.5474` n `127` status `ready` deltaP `1.1033` edge `-0.0006` maxDD `-2.155`
- `market_context_high->index_4h` score `-0.5518` n `118` status `ready` deltaP `4.7927` edge `0.0338` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.636` n `127` status `ready` deltaP `-2.3457` edge `-0.0018` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.6565` n `118` status `ready` deltaP `0.9095` edge `0.0508` maxDD `-4.6157`
- `market_context_high->fx_4h` score `-0.9834` n `118` status `ready` deltaP `-2.8473` edge `0.0002` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.3318` n `63` status `ready` deltaP `-1.3145` edge `-0.0083` maxDD `-1.1804`
- `market_context_high->crypto_alt_24h` score `-2.1126` n `63` status `ready` deltaP `12.9712` edge `0.4479` maxDD `-58.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

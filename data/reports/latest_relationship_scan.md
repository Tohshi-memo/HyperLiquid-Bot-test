# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T11:52:28.950062+00:00`
- Price records: `672`
- Market context records: `5141`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `26.4843` n `67` status `ready` deltaP `31.3925` edge `2.032` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `6.8588` n `124` status `ready` deltaP `19.1827` edge `0.5459` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.4355` n `136` status `ready` deltaP `9.5456` edge `0.5368` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `4.8653` n `124` status `ready` deltaP `14.6637` edge `0.4676` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.5018` n `124` status `ready` deltaP `12.5492` edge `0.4374` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.9717` n `124` status `ready` deltaP `9.7856` edge `0.1796` maxDD `-7.4425`
- `market_context_high->commodity_24h` score `0.9581` n `67` status `ready` deltaP `16.5423` edge `0.1248` maxDD `-4.6462`
- `market_context_high->crypto_alt_1h` score `0.6878` n `136` status `ready` deltaP `5.0502` edge `0.1198` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6345` n `136` status `ready` deltaP `7.4586` edge `0.1277` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.6165` n `136` status `ready` deltaP `6.9435` edge `0.0644` maxDD `-2.745`
- `market_context_high->crypto_alt_24h` score `0.3622` n `67` status `ready` deltaP `16.7548` edge `0.5799` maxDD `-46.2794`
- `market_context_high->index_1h` score `-0.0056` n `136` status `ready` deltaP `5.31` edge `0.0145` maxDD `-1.0296`
- `market_context_high->crypto_major_24h` score `-0.075` n `67` status `ready` deltaP `15.0549` edge `0.5773` maxDD `-48.0465`
- `market_context_high->metal_1h` score `-0.0853` n `136` status `ready` deltaP `4.6407` edge `0.0147` maxDD `-1.8592`
- `market_context_high->metal_24h` score `-0.1766` n `67` status `ready` deltaP `-1.3319` edge `0.1783` maxDD `-10.0641`
- `market_context_high->index_4h` score `-0.3398` n `124` status `ready` deltaP `6.9483` edge `0.0371` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.4816` n `67` status `ready` deltaP `4.1122` edge `0.0007` maxDD `-0.8549`
- `market_context_high->commodity_1h` score `-0.5456` n `136` status `ready` deltaP `1.0479` edge `0.0` maxDD `-2.155`
- `market_context_high->fx_1h` score `-0.6015` n `136` status `ready` deltaP `-1.7436` edge `-0.0014` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.873` n `124` status `ready` deltaP `0.9736` edge `0.0415` maxDD `-6.1264`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

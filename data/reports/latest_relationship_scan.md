# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T14:37:30.934919+00:00`
- Price records: `672`
- Market context records: `5256`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `25.4605` n `145` status `ready` deltaP `29.5331` edge `1.9438` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `10.6954` n `145` status `ready` deltaP `29.3774` edge `1.0616` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `3.9161` n `160` status `ready` deltaP `13.3232` edge `0.4016` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.6419` n `160` status `ready` deltaP `13.5061` edge `0.4427` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.2524` n `145` status `ready` deltaP `19.3523` edge `0.7049` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.6489` n `160` status `ready` deltaP `16.1738` edge `0.1318` maxDD `-5.5109`
- `market_context_high->crypto_alt_24h` score `1.3696` n `145` status `ready` deltaP `16.1242` edge `0.5577` maxDD `-33.7517`
- `market_context_high->crypto_alt_1h` score `0.6561` n `167` status `ready` deltaP `5.2395` edge `0.1159` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.5126` n `160` status `ready` deltaP `8.247` edge `0.1516` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.5036` n `167` status `ready` deltaP `6.5868` edge `0.1226` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.5024` n `145` status `ready` deltaP `12.615` edge `0.0473` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.1622` n `145` status `ready` deltaP `20.6681` edge `0.0465` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1186` n `167` status `ready` deltaP `6.7365` edge `0.0615` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0724` n `167` status `ready` deltaP `4.9401` edge `0.0114` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1026` n `167` status `ready` deltaP `4.9401` edge `0.0177` maxDD `-2.0682`
- `market_context_high->unknown_1h` score `-0.1975` n `167` status `ready` deltaP `8.2336` edge `-0.0072` maxDD `-2.7986`
- `market_context_high->fx_1h` score `-0.3109` n `167` status `ready` deltaP `0.8982` edge `-0.0006` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.7252` n `160` status `ready` deltaP `4.7256` edge `0.0198` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.8065` n `160` status `ready` deltaP `-0.0915` edge `0.0006` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-1.2728` n `167` status `ready` deltaP `-2.3952` edge `-0.006` maxDD `-2.728`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

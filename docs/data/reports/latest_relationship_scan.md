# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T07:52:30.398919+00:00`
- Price records: `672`
- Market context records: `5228`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5600`

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

- `market_context_high->unknown_24h` score `21.4373` n `119` status `ready` deltaP `32.4026` edge `1.5894` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.5407` n `119` status `ready` deltaP `32.0189` edge `1.2811` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `7.981` n `119` status `ready` deltaP `25.1226` edge `0.8363` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `3.9419` n `155` status `ready` deltaP `12.9318` edge `0.4022` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9054` n `155` status `ready` deltaP `14.0696` edge `0.4609` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.1118` n `155` status `ready` deltaP `16.8302` edge `0.166` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8454` n `155` status `ready` deltaP `8.2393` edge `0.163` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5543` n `119` status `ready` deltaP `13.3388` edge `0.0468` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.4133` n `155` status `ready` deltaP `6.553` edge `0.1153` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.4077` n `155` status `ready` deltaP `4.3539` edge `0.1011` maxDD `-5.0257`
- `market_context_high->equity_24h` score `0.1026` n `119` status `ready` deltaP `16.7907` edge `0.4641` maxDD `-40.0306`
- `market_context_high->equity_4h` score `-0.0257` n `155` status `ready` deltaP `5.5684` edge `0.1246` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.2228` n `155` status `ready` deltaP `3.2132` edge `0.0092` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.2451` n `155` status `ready` deltaP `4.9208` edge `0.0433` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2589` n `155` status `ready` deltaP `3.0887` edge `0.0082` maxDD `-1.0296`
- `market_context_high->index_24h` score `-0.2844` n `119` status `ready` deltaP `15.2894` edge `0.0251` maxDD `-7.413`
- `market_context_high->fx_1h` score `-0.3024` n `155` status `ready` deltaP `1.0605` edge `-0.0006` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.618` n `155` status `ready` deltaP `0.4259` edge `-0.0012` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.6738` n `155` status `ready` deltaP `1.9669` edge `0.0039` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.9275` n `155` status `ready` deltaP `2.857` edge `0.0154` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

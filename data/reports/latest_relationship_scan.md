# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T00:08:04.412035+00:00`
- Price records: `672`
- Market context records: `5196`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5644`

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

- `market_context_high->unknown_24h` score `18.9004` n `91` status `ready` deltaP `33.4516` edge `1.371` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.3864` n `91` status `ready` deltaP `28.6096` edge `1.3743` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.8851` n `91` status `ready` deltaP `29.1285` edge `1.0516` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.4407` n `155` status `ready` deltaP `19.7266` edge `0.4241` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.5199` n `155` status `ready` deltaP `13.5415` edge `0.4463` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4032` n `155` status `ready` deltaP `13.9172` edge `0.5034` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.576` n `155` status `ready` deltaP `9.1375` edge `0.2179` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.8896` n `155` status `ready` deltaP `8.1599` edge `0.1836` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5696` n `155` status `ready` deltaP `4.6533` edge `0.1126` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5524` n `155` status `ready` deltaP `6.7027` edge `0.1259` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.3816` n `91` status `ready` deltaP `12.5153` edge `0.0379` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.147` n `155` status `ready` deltaP `6.8669` edge `0.063` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0624` n `155` status `ready` deltaP `4.8851` edge `0.0126` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0919` n `155` status `ready` deltaP `4.5605` edge `0.017` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2495` n `155` status `ready` deltaP `1.9587` edge `0.0002` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.5274` n `155` status `ready` deltaP `4.406` edge `0.0064` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.5402` n `155` status `ready` deltaP `5.4485` edge `0.0304` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.5969` n `155` status `ready` deltaP `0.7253` edge `-0.0005` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.893` n `91` status `ready` deltaP `9.6307` edge `-0.0152` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3418` n `155` status `ready` deltaP `-0.1023` edge `0.029` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T02:22:25.999127+00:00`
- Price records: `672`
- Market context records: `5206`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `16.4541` n `100` status `ready` deltaP `33.8472` edge `1.1645` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.8916` n `100` status `ready` deltaP `30.4097` edge `1.4044` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.685` n `100` status `ready` deltaP `30.6319` edge `1.0249` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.2537` n `155` status `ready` deltaP `18.9644` edge `0.4136` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.6283` n `155` status `ready` deltaP `13.8464` edge `0.4533` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4718` n `155` status `ready` deltaP `14.0696` edge `0.5081` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.5437` n `155` status `ready` deltaP `8.6884` edge `0.2182` maxDD `-2.7986`
- `market_context_high->crypto_major_1h` score `0.646` n `155` status `ready` deltaP `7.0021` edge `0.1317` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.6388` n `155` status `ready` deltaP `8.1599` edge `0.1627` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.6368` n `155` status `ready` deltaP `4.803` edge `0.1172` maxDD `-5.0257`
- `market_context_high->fx_24h` score `0.5413` n `100` status `ready` deltaP `13.3264` edge `0.0458` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.0379` n `155` status `ready` deltaP `6.2681` edge `0.0579` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.0919` n `155` status `ready` deltaP `4.5605` edge `0.017` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.108` n `155` status `ready` deltaP `4.436` edge `0.0118` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.276` n `155` status `ready` deltaP `1.5096` edge `-0.0002` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.5858` n `155` status `ready` deltaP `5.4485` edge `0.0266` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5931` n `155` status `ready` deltaP `3.3389` edge `0.0051` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6063` n `155` status `ready` deltaP `0.5756` edge `-0.0007` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.6954` n `100` status `ready` deltaP `11.8264` edge `-0.0045` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3597` n `155` status `ready` deltaP `-0.1023` edge `0.0267` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

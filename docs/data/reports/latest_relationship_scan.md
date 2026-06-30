# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T01:07:27.925324+00:00`
- Price records: `672`
- Market context records: `5200`
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

- `market_context_high->unknown_24h` score `17.75` n `95` status `ready` deltaP `33.6367` edge `1.2739` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.7327` n `95` status `ready` deltaP `29.4883` edge `1.3973` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.9215` n `95` status `ready` deltaP `29.8684` edge `1.0497` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.3299` n `155` status `ready` deltaP `19.4217` edge `0.4169` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.6163` n `155` status `ready` deltaP `13.8464` edge `0.4523` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.461` n `155` status `ready` deltaP `14.0696` edge `0.5072` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.4909` n `155` status `ready` deltaP `8.6884` edge `0.2138` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.7924` n `155` status `ready` deltaP `8.1599` edge `0.1755` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.6236` n `155` status `ready` deltaP `4.803` edge `0.1161` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6088` n `155` status `ready` deltaP `6.8524` edge `0.1296` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.4677` n `95` status `ready` deltaP `12.9312` edge `0.0423` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.1398` n `155` status `ready` deltaP `6.8669` edge `0.0624` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0481` n `155` status `ready` deltaP `5.0348` edge `0.0128` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0802` n `155` status `ready` deltaP `4.7102` edge `0.0175` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2845` n `155` status `ready` deltaP `1.3599` edge `-0.0003` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.5558` n `155` status `ready` deltaP `5.4485` edge `0.0291` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5654` n `155` status `ready` deltaP `3.7962` edge `0.0056` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5891` n `155` status `ready` deltaP `0.875` edge `-0.0005` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.8026` n `95` status `ready` deltaP `10.6944` edge `-0.0107` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3582` n `155` status `ready` deltaP `-0.1023` edge `0.0269` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

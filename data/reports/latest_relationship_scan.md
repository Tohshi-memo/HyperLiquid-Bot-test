# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T12:52:27.722898+00:00`
- Price records: `672`
- Market context records: `5249`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7568`

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

- `market_context_high->unknown_24h` score `24.9057` n `138` status `ready` deltaP `30.6083` edge `1.8904` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `11.9387` n `138` status `ready` deltaP `31.8085` edge `1.149` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `4.5935` n `138` status `ready` deltaP `18.8179` edge `0.6502` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.4655` n `155` status `ready` deltaP `15.0659` edge `0.4316` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.165` n `155` status `ready` deltaP `15.2892` edge `0.4744` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.4596` n `138` status `ready` deltaP `18.7576` edge `0.6428` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `2.2046` n `155` status `ready` deltaP `17.1351` edge `0.1717` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `0.9505` n `160` status `ready` deltaP `8.634` edge `0.0858` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5456` n `138` status `ready` deltaP `12.9906` edge `0.0484` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4873` n `160` status `ready` deltaP `4.7193` edge `0.1053` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.4776` n `155` status `ready` deltaP `7.855` edge `0.1513` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.4442` n `160` status `ready` deltaP `6.4895` edge `0.1183` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.0284` n `138` status `ready` deltaP `19.686` edge `0.0359` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0335` n `160` status `ready` deltaP `6.5307` edge `0.0502` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.0979` n `160` status `ready` deltaP `4.8952` edge `0.014` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1429` n `160` status `ready` deltaP `4.4798` edge `0.0086` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3403` n `160` status `ready` deltaP `0.378` edge `-0.0009` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.7971` n `155` status `ready` deltaP `-0.0148` edge `0.0013` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8241` n `155` status `ready` deltaP `3.9241` edge `0.0169` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-1.1654` n `160` status `ready` deltaP `-1.6729` edge `-0.0051` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

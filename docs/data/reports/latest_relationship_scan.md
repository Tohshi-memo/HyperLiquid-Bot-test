# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T11:52:28.224105+00:00`
- Price records: `672`
- Market context records: `5245`
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

- `market_context_high->unknown_24h` score `24.7089` n `135` status `ready` deltaP `31.2384` edge `1.8698` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.5209` n `135` status `ready` deltaP `33.0555` edge `1.1892` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `5.3331` n `135` status `ready` deltaP `19.3634` edge `0.6957` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.3245` n `155` status `ready` deltaP `14.6086` edge `0.4229` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0894` n `155` status `ready` deltaP `15.2892` edge `0.4681` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.207` n `155` status `ready` deltaP `17.1351` edge `0.1719` maxDD `-5.5109`
- `market_context_high->equity_24h` score `2.1305` n `135` status `ready` deltaP `18.4838` edge `0.6172` maxDD `-40.0306`
- `market_context_high->unknown_1h` score `0.935` n `160` status `ready` deltaP `8.4843` edge `0.0855` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5787` n `135` status `ready` deltaP `13.2986` edge `0.0491` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.3913` n `160` status `ready` deltaP `4.4199` edge `0.0993` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3626` n `160` status `ready` deltaP `6.3398` edge `0.1125` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.3436` n `155` status `ready` deltaP `7.2452` edge `0.1442` maxDD `-7.4425`
- `market_context_high->index_24h` score `-0.0221` n `135` status `ready` deltaP `19.0741` edge `0.0335` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0874` n `160` status `ready` deltaP `6.2313` edge `0.0477` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1337` n `160` status `ready` deltaP `4.4461` edge `0.0124` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1524` n `160` status `ready` deltaP `4.3301` edge `0.0088` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3473` n `160` status `ready` deltaP `0.2283` edge `-0.0008` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.7955` n `155` status `ready` deltaP `-0.0148` edge `0.0015` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8265` n `155` status `ready` deltaP `3.9241` edge `0.0167` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-1.0983` n `160` status `ready` deltaP `-1.0741` edge `-0.0035` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T17:53:27.134262+00:00`
- Price records: `672`
- Market context records: `1140`
- Flow alert records: `5185`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `19.7799` n `151` status `ready` deltaP `42.8049` edge `1.4401` maxDD `-5.5043`
- `market_context_high->crypto_alt_24h` score `9.5264` n `151` status `ready` deltaP `19.1616` edge `0.828` maxDD `-12.2838`
- `market_context_high->equity_24h` score `7.6606` n `151` status `ready` deltaP `18.6408` edge `0.5827` maxDD `-4.8203`
- `market_context_high->index_24h` score `5.9908` n `151` status `ready` deltaP `17.2519` edge `0.4259` maxDD `-2.668`
- `market_context_high->metal_24h` score `5.6584` n `151` status `ready` deltaP `-1.7477` edge `0.6499` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.2656` n `168` status `ready` deltaP `11.4039` edge `0.1791` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0453` n `168` status `ready` deltaP `8.747` edge `0.0971` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5229` n `168` status `ready` deltaP `7.7951` edge `0.0233` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4419` n `168` status `ready` deltaP `3.4787` edge `0.0514` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.2892` n `168` status `ready` deltaP `9.5238` edge `0.1657` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1136` n `168` status `ready` deltaP `8.0161` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0802` n `168` status `ready` deltaP `6.9825` edge `0.0367` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2316` n `168` status `ready` deltaP `6.8007` edge `-0.0036` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.243` n `168` status `ready` deltaP `2.9441` edge `0.0444` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7358` n `168` status `ready` deltaP `0.6315` edge `0.0011` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.8104` n `168` status `ready` deltaP `-2.6732` edge `-0.0053` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.8443` n `168` status `ready` deltaP `6.7582` edge `0.1432` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.3363` n `168` status `ready` deltaP `7.1574` edge `-0.047` maxDD `-9.2991`
- `market_context_high->unknown_24h` score `-3.1246` n `151` status `ready` deltaP `3.5068` edge `-0.0108` maxDD `-10.1706`
- `market_context_high->commodity_4h` score `-3.3147` n `168` status `ready` deltaP `-12.6452` edge `-0.0239` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

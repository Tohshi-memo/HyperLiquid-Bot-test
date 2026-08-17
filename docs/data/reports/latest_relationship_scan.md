# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T02:07:27.114567+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `11.6465` n `73` status `ready` deltaP `-41.5668` edge `2.0386` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `4.1965` n `73` status `ready` deltaP `34.199` edge `0.1566` maxDD `-0.4576`
- `market_context_high->index_24h` score `1.1746` n `73` status `ready` deltaP `19.3089` edge `-0.0266` maxDD `-0.0064`
- `market_context_high->commodity_4h` score `1.1003` n `103` status `ready` deltaP `12.6657` edge `0.0544` maxDD `-0.7718`
- `market_context_high->crypto_major_24h` score `0.6403` n `73` status `ready` deltaP `0.5113` edge `0.2161` maxDD `-7.9586`
- `market_context_high->metal_4h` score `-0.2282` n `103` status `ready` deltaP `16.0357` edge `0.0148` maxDD `-4.5909`
- `market_context_high->commodity_1h` score `-0.336` n `108` status `ready` deltaP `-1.1699` edge `0.0093` maxDD `-0.8998`
- `market_context_high->metal_1h` score `-0.3979` n `108` status `ready` deltaP `5.1619` edge `0.004` maxDD `-1.7257`
- `market_context_high->equity_24h` score `-0.566` n `73` status `ready` deltaP `12.5167` edge `-0.0361` maxDD `-5.2274`
- `market_context_high->fx_4h` score `-0.5991` n `103` status `ready` deltaP `-1.5362` edge `-0.0061` maxDD `-0.504`
- `market_context_high->index_1h` score `-0.7378` n `108` status `ready` deltaP `-5.988` edge `-0.0025` maxDD `-0.5064`
- `market_context_high->fx_1h` score `-0.7732` n `108` status `ready` deltaP `-3.7037` edge `-0.0027` maxDD `-0.2968`
- `market_context_high->equity_1h` score `-1.376` n `108` status `ready` deltaP `-8.5329` edge `-0.0364` maxDD `-3.3165`
- `market_context_high->crypto_major_4h` score `-1.4347` n `103` status `ready` deltaP `1.7612` edge `-0.0105` maxDD `-4.6638`
- `market_context_high->index_4h` score `-1.9747` n `103` status `ready` deltaP `-11.7097` edge `-0.0056` maxDD `-0.8045`
- `market_context_high->crypto_alt_1h` score `-2.0837` n `108` status `ready` deltaP `-6.7809` edge `-0.0246` maxDD `-4.6399`
- `market_context_high->crypto_major_1h` score `-2.1187` n `108` status `ready` deltaP `-6.7809` edge `-0.0303` maxDD `-4.0845`
- `market_context_high->fx_24h` score `-2.9696` n `73` status `ready` deltaP `-27.521` edge `-0.0365` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-3.1192` n `73` status `ready` deltaP `-19.8606` edge `-0.0163` maxDD `-7.0954`
- `market_context_high->equity_4h` score `-5.6385` n `103` status `ready` deltaP `-20.3351` edge `-0.1509` maxDD `-8.3394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

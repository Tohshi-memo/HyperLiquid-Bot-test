# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T02:22:27.735591+00:00`
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

- `market_context_high->commodity_24h` score `4.1187` n `72` status `ready` deltaP `34.2014` edge `0.1501` maxDD `-0.4576`
- `market_context_high->unknown_24h` score `2.3648` n `72` status `ready` deltaP `-42.5347` edge `0.8551` maxDD `-7.8016`
- `market_context_high->index_24h` score `1.2849` n `72` status `ready` deltaP `20.4861` edge `-0.0253` maxDD `-0.0026`
- `market_context_high->commodity_4h` score `1.1579` n `102` status `ready` deltaP `13.1606` edge `0.0559` maxDD `-0.7718`
- `market_context_high->crypto_major_24h` score `0.8151` n `72` status `ready` deltaP `1.0417` edge `0.2225` maxDD `-7.588`
- `market_context_high->equity_24h` score `0.0224` n `72` status `ready` deltaP `13.5417` edge `-0.0124` maxDD `-4.0806`
- `market_context_high->metal_4h` score `-0.2813` n `102` status `ready` deltaP `15.7312` edge `0.0124` maxDD `-4.5909`
- `market_context_high->commodity_1h` score `-0.284` n `108` status `ready` deltaP `-0.3936` edge `0.0108` maxDD `-0.8998`
- `market_context_high->metal_1h` score `-0.4804` n `108` status `ready` deltaP `4.3857` edge `0.0023` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.6162` n `102` status `ready` deltaP `-1.8502` edge `-0.0062` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.7732` n `108` status `ready` deltaP `-3.7037` edge `-0.0027` maxDD `-0.2968`
- `market_context_high->index_1h` score `-1.1326` n `108` status `ready` deltaP `-5.988` edge `-0.0023` maxDD `-0.5064`
- `market_context_high->equity_1h` score `-1.327` n `108` status `ready` deltaP `-7.7567` edge `-0.0353` maxDD `-3.3165`
- `market_context_high->crypto_major_4h` score `-1.5195` n `102` status `ready` deltaP `1.2853` edge `-0.0144` maxDD `-4.6638`
- `market_context_high->index_4h` score `-2.0135` n `102` status `ready` deltaP `-12.1951` edge `-0.0056` maxDD `-0.8045`
- `market_context_high->crypto_alt_1h` score `-2.0733` n `108` status `ready` deltaP `-6.7809` edge `-0.0243` maxDD `-4.595`
- `market_context_high->crypto_major_1h` score `-2.1271` n `108` status `ready` deltaP `-6.7809` edge `-0.031` maxDD `-4.0845`
- `market_context_high->fx_24h` score `-3.021` n `72` status `ready` deltaP `-28.2986` edge `-0.0379` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-4.9779` n `72` status `ready` deltaP `-20.6597` edge `-0.0259` maxDD `-7.0954`
- `market_context_high->equity_4h` score `-5.5999` n `102` status `ready` deltaP `-20.0592` edge `-0.1509` maxDD `-8.2292`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

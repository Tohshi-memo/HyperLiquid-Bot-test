# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T09:52:25.672055+00:00`
- Price records: `672`
- Market context records: `6075`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11112`

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

- `news_risk_high->fx_24h` score `8.1618` n `30` status `ready` deltaP `72.7431` edge `0.1952` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3695` n `30` status `ready` deltaP `45.1829` edge `0.0675` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `4.2292` n `30` status `ready` deltaP `30.3125` edge `0.1651` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.4458` n `32` status `ready` deltaP `29.3413` edge `0.0221` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6589` n `206` status `ready` deltaP `9.0989` edge `0.1693` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1972` n `32` status `ready` deltaP `13.8286` edge `0.108` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.0566` n `30` status `ready` deltaP `20.1736` edge `-0.0259` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.654` n `32` status `ready` deltaP `9.2253` edge `0.0685` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.093` n `30` status `ready` deltaP `9.2361` edge `0.0375` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.362` n `206` status `ready` deltaP `3.7294` edge `0.0086` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.521` n `206` status `ready` deltaP `0.4578` edge `-0.0008` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.7583` n `32` status `ready` deltaP `-2.0958` edge `-0.0335` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7628` n `206` status `ready` deltaP `4.7047` edge `0.0461` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.7895` n `206` status `ready` deltaP `4.9997` edge `0.0422` maxDD `-9.807`
- `market_context_high->commodity_1h` score `-0.8057` n `206` status `ready` deltaP `-2.4315` edge `-0.0063` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.8173` n `206` status `ready` deltaP `4.7907` edge `0.0187` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.8238` n `206` status `ready` deltaP `1.8284` edge `0.032` maxDD `-4.3608`
- `market_context_high->index_4h` score `-0.8943` n `206` status `ready` deltaP `2.2629` edge `0.0236` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-0.9574` n `32` status `ready` deltaP `-7.5786` edge `-0.0159` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.19` n `206` status `ready` deltaP `-2.0871` edge `0.0046` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

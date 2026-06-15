# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T16:52:38.414985+00:00`
- Price records: `672`
- Market context records: `4009`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10412`

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

- `risk_on_high->unknown_4h` score `147.1459` n `40` status `ready` deltaP `-3.9916` edge `12.4704` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `147.1459` n `40` status `ready` deltaP `-3.9916` edge `12.4704` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.8987` n `135` status `ready` deltaP `-3.0516` edge `4.4981` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.7047` n `146` status `ready` deltaP `2.892` edge `2.7484` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `8.0432` n `40` status `ready` deltaP `40.5546` edge `0.3999` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.0432` n `40` status `ready` deltaP `40.5546` edge `0.3999` maxDD `0.0`
- `market_context_high->index_24h` score `3.9068` n `135` status `ready` deltaP `26.7681` edge `0.1956` maxDD `-3.2125`
- `risk_on_high->equity_4h` score `3.735` n `40` status `ready` deltaP `37.226` edge `0.0678` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.735` n `40` status `ready` deltaP `37.226` edge `0.0678` maxDD `-0.0446`
- `market_context_high->metal_24h` score `3.1071` n `135` status `ready` deltaP `14.9445` edge `0.2782` maxDD `-6.5125`
- `risk_on_high->index_24h` score `2.0572` n `40` status `ready` deltaP `28.2496` edge `-0.0169` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.0572` n `40` status `ready` deltaP `28.2496` edge `-0.0169` maxDD `0.0`
- `market_context_high->equity_4h` score `1.9228` n `146` status `ready` deltaP `19.863` edge `0.1559` maxDD `-6.9137`
- `market_context_high->equity_24h` score `1.75` n `135` status `ready` deltaP `16.8509` edge `0.3333` maxDD `-14.318`
- `market_context_high->equity_1h` score `1.3057` n `148` status `ready` deltaP `9.1161` edge `0.104` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.2033` n `40` status `ready` deltaP `19.6842` edge `0.0356` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.2033` n `40` status `ready` deltaP `19.6842` edge `0.0356` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.1047` n `148` status `ready` deltaP `12.3803` edge `0.057` maxDD `-1.7983`
- `risk_on_high->commodity_24h` score `1.0244` n `40` status `ready` deltaP `4.2028` edge `0.2855` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0244` n `40` status `ready` deltaP `4.2028` edge `0.2855` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

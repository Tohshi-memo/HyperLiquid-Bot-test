# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T11:22:26.957421+00:00`
- Price records: `672`
- Market context records: `5976`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.2574` n `30` status `ready` deltaP `66.4931` edge `0.1615` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.8806` n `30` status `ready` deltaP `35.7986` edge `0.1886` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9634` n `30` status `ready` deltaP `41.0671` edge `0.0611` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1627` n `30` status `ready` deltaP `26.0279` edge `0.0206` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.36` n `236` status `ready` deltaP `8.6813` edge `0.1649` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8123` n `30` status `ready` deltaP `10.0399` edge `0.0839` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1397` n `30` status `ready` deltaP `5.02` edge `0.0306` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0039` n `30` status `ready` deltaP `8.8889` edge `0.0284` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3907` n `30` status `ready` deltaP `1.8363` edge `-0.0257` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4404` n `242` status `ready` deltaP `3.5817` edge `0.0325` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4989` n `242` status `ready` deltaP `2.222` edge `0.0011` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5067` n `242` status `ready` deltaP `-1.5811` edge `0.0013` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.6775` n `242` status `ready` deltaP `-0.6112` edge `-0.0007` maxDD `-0.8015`
- `market_context_high->index_1h` score `-0.7067` n `242` status `ready` deltaP `-0.5629` edge `0.0045` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-0.9155` n `213` status `ready` deltaP `21.2197` edge `0.3107` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0882` n `30` status `ready` deltaP `-10.1497` edge `-0.0204` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1163` n `236` status `ready` deltaP `0.9173` edge `0.0195` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.1247` n `242` status `ready` deltaP `2.0785` edge `0.0187` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1668` n `242` status `ready` deltaP `1.6591` edge `0.0146` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4071` n `236` status `ready` deltaP `-0.8346` edge `-0.0035` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

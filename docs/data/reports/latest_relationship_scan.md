# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T12:52:31.437220+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9102`

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

- `market_context_high->unknown_4h` score `31.7629` n `58` status `ready` deltaP `1.23` edge `2.6537` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `20.4601` n `101` status `ready` deltaP `7.9706` edge `2.3377` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `14.6413` n `101` status `ready` deltaP `8.3557` edge `1.6525` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.346` n `101` status `ready` deltaP `16.48` edge `0.2899` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.0701` n `101` status `ready` deltaP `19.8337` edge `0.2494` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.3697` n `101` status `ready` deltaP `14.7344` edge `0.1458` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7619` n `101` status `ready` deltaP `16.5308` edge `0.0889` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.3158` n `101` status `ready` deltaP `23.8913` edge `0.14` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7228` n `58` status `ready` deltaP `5.4099` edge `0.0495` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6046` n `58` status `ready` deltaP `9.3795` edge `0.0134` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.4855` n `101` status `ready` deltaP `13.4004` edge `0.0113` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3977` n `58` status `ready` deltaP `9.3744` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3525` n `101` status `ready` deltaP `10.1651` edge `0.0252` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2799` n `101` status `ready` deltaP `14.6598` edge `0.031` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2498` n `58` status `ready` deltaP `13.5618` edge `0.0053` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2075` n `58` status `ready` deltaP `4.9505` edge `0.0151` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1513` n `101` status `ready` deltaP `3.741` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3521` n `101` status `ready` deltaP `1.0227` edge `0.0044` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.4069` n `58` status `ready` deltaP `1.9712` edge `-0.0029` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4796` n `101` status `ready` deltaP `8.7355` edge `-0.0353` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

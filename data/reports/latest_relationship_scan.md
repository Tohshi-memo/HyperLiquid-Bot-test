# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T06:52:34.553687+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9154`

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

- `market_context_high->unknown_4h` score `32.5489` n `58` status `ready` deltaP `1.23` edge `2.7192` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `23.7898` n `99` status `ready` deltaP `11.5373` edge `2.5914` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `18.4702` n `99` status `ready` deltaP `12.0423` edge `1.947` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.4023` n `101` status `ready` deltaP `19.5288` edge `0.3576` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.0095` n `101` status `ready` deltaP `21.5105` edge `0.3165` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7318` n `101` status `ready` deltaP `16.2314` edge `0.166` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1228` n `101` status `ready` deltaP `18.1775` edge `0.108` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1853` n `99` status `ready` deltaP `23.4217` edge `0.1264` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0033` n `58` status `ready` deltaP `7.5057` edge `0.0589` maxDD `-0.36`
- `market_context_high->index_1h` score `0.7999` n `58` status `ready` deltaP `11.625` edge `0.0147` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6161` n `101` status `ready` deltaP `14.598` edge `0.0142` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.3816` n `101` status `ready` deltaP `15.422` edge `0.0344` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.3801` n `58` status `ready` deltaP `15.5435` edge `0.0088` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.3381` n `58` status `ready` deltaP `6.1481` edge `0.018` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3331` n `58` status `ready` deltaP `8.6259` edge `0.0059` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1809` n `101` status `ready` deltaP `8.3358` edge `0.0231` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.0716` n `101` status `ready` deltaP `3.1185` edge `0.0138` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1621` n `58` status `ready` deltaP `-1.6415` edge `0.0693` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.216` n `101` status `ready` deltaP `2.9925` edge `0.0064` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.3396` n `99` status `ready` deltaP `10.2273` edge `-0.0273` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

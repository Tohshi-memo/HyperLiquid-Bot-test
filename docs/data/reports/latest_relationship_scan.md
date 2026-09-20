# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T18:52:36.746030+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9806`

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

- `news_risk_high->crypto_major_24h` score `23.5981` n `98` status `ready` deltaP `10.8809` edge `2.5798` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3698` n `98` status `ready` deltaP `15.2671` edge `2.0838` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `15.9157` n `41` status `ready` deltaP `-0.9147` edge `1.3474` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.2818` n `101` status `ready` deltaP `22.2727` edge `0.4126` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.3183` n `41` status `ready` deltaP `37.3476` edge `0.1242` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `4.1161` n `101` status `ready` deltaP `21.358` edge `0.3264` maxDD `-8.0625`
- `market_context_high->commodity_24h` score `3.0656` n `30` status `ready` deltaP `15.9723` edge `0.2015` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `2.9141` n `101` status `ready` deltaP `16.6805` edge `0.1782` maxDD `-2.058`
- `market_context_high->fx_24h` score `2.194` n `30` status `ready` deltaP `21.3195` edge `0.0449` maxDD `-0.0027`
- `news_risk_high->crypto_major_1h` score `2.1935` n `101` status `ready` deltaP `18.6266` edge `0.1109` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.0808` n `41` status `ready` deltaP `27.2866` edge `0.013` maxDD `-0.0543`
- `news_risk_high->commodity_24h` score `1.051` n `98` status `ready` deltaP `22.775` edge `0.1135` maxDD `-3.4467`
- `market_context_high->fx_1h` score `1.0334` n `52` status `ready` deltaP `14.4404` edge `0.0073` maxDD `-0.063`
- `market_context_high->commodity_1h` score `1.0314` n `52` status `ready` deltaP `11.8148` edge `0.0347` maxDD `-0.2012`
- `news_risk_high->metal_1h` score `0.6425` n `101` status `ready` deltaP `14.7477` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6312` n `101` status `ready` deltaP `17.2512` edge `0.043` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.5554` n `98` status `ready` deltaP `16.3974` edge `0.0779` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.2786` n `52` status `ready` deltaP `7.0935` edge `0.0066` maxDD `-0.4538`
- `news_risk_high->equity_1h` score `0.2448` n `101` status `ready` deltaP `5.5137` edge `0.0242` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.1495` n `98` status `ready` deltaP `14.9837` edge `0.0037` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

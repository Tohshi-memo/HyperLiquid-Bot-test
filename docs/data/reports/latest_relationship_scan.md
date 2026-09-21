# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T06:22:26.211738+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9198`

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

- `market_context_high->unknown_4h` score `33.1669` n `58` status `ready` deltaP `1.23` edge `2.7707` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `24.0016` n `98` status `ready` deltaP `11.5753` edge `2.6088` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `18.6102` n `98` status `ready` deltaP `12.1421` edge `1.958` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.4938` n `101` status `ready` deltaP `19.8337` edge `0.3632` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.0155` n `101` status `ready` deltaP `21.5105` edge `0.317` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7618` n `101` status `ready` deltaP `16.3811` edge `0.1675` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1204` n `101` status `ready` deltaP `18.1775` edge `0.1078` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2417` n `98` status `ready` deltaP `23.8166` edge `0.131` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0428` n `58` status `ready` deltaP `7.8051` edge `0.0602` maxDD `-0.36`
- `market_context_high->index_1h` score `0.8274` n `58` status `ready` deltaP `11.9244` edge `0.015` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6329` n `101` status `ready` deltaP `14.7477` edge `0.0146` maxDD `-0.8144`
- `market_context_high->index_4h` score `0.3991` n `58` status `ready` deltaP `15.8484` edge `0.0092` maxDD `-1.0949`
- `news_risk_high->metal_4h` score `0.3912` n `101` status `ready` deltaP `15.422` edge `0.0352` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3549` n `58` status `ready` deltaP `6.2978` edge `0.0184` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3319` n `58` status `ready` deltaP `8.6259` edge `0.0058` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1797` n `101` status `ready` deltaP `8.3358` edge `0.023` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.032` n `101` status `ready` deltaP `3.4179` edge `0.0151` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1645` n `58` status `ready` deltaP `-1.6415` edge `0.0691` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.2172` n `101` status `ready` deltaP `2.9925` edge `0.0063` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.3287` n `98` status `ready` deltaP `10.1226` edge `-0.0252` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

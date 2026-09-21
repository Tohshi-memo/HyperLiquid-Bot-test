# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T08:07:32.148743+00:00`
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

- `market_context_high->unknown_4h` score `33.2029` n `58` status `ready` deltaP `1.23` edge `2.7737` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `23.2356` n `101` status `ready` deltaP `11.2692` edge `2.547` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `18.0107` n `101` status `ready` deltaP `11.6543` edge `1.9113` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.2585` n `101` status `ready` deltaP `18.7666` edge `0.3507` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.9333` n `101` status `ready` deltaP `21.0532` edge `0.3132` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7054` n `101` status `ready` deltaP `16.0817` edge `0.1648` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0988` n `101` status `ready` deltaP `18.0278` edge `0.107` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.0986` n `101` status `ready` deltaP `22.8496` edge `0.1191` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.9026` n `58` status `ready` deltaP `6.7572` edge `0.0555` maxDD `-0.36`
- `market_context_high->index_1h` score `0.7352` n `58` status `ready` deltaP `10.8765` edge `0.0143` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5718` n `101` status `ready` deltaP `14.1489` edge `0.0135` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.3502` n `101` status `ready` deltaP `15.2695` edge `0.0328` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.3335` n `58` status `ready` deltaP `14.7813` edge `0.0079` maxDD `-1.0949`
- `market_context_high->fx_1h` score `0.3211` n `58` status `ready` deltaP `8.4762` edge `0.0059` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.2938` n `58` status `ready` deltaP `5.699` edge `0.0173` maxDD `-0.1314`
- `news_risk_high->fx_4h` score `0.2199` n `101` status `ready` deltaP `8.7931` edge `0.0233` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.1723` n `101` status `ready` deltaP `2.37` edge `0.0104` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1861` n `58` status `ready` deltaP `-1.7912` edge `0.0683` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.228` n `101` status `ready` deltaP `2.8428` edge `0.0064` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.4087` n `101` status `ready` deltaP `9.6036` edge `-0.032` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

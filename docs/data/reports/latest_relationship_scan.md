# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T08:07:31.339426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_4h` score `40.9051` n `91` status `ready` deltaP `-6.188` edge `3.5039` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.5733` n `91` status `ready` deltaP `34.8239` edge `0.6085` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.8772` n `91` status `ready` deltaP `19.3098` edge `1.3242` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6031` n `91` status `ready` deltaP `10.0578` edge `0.7497` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.3424` n `91` status `ready` deltaP `15.7247` edge `0.2003` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2356` n `91` status `ready` deltaP `6.3977` edge `0.0012` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1797` n `91` status `ready` deltaP `9.5447` edge `0.0483` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.0928` n `91` status `ready` deltaP `8.8264` edge `0.0081` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.3098` n `91` status `ready` deltaP `3.5978` edge `0.0014` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3206` n `91` status `ready` deltaP `8.9036` edge `0.0905` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.3746` n `91` status `ready` deltaP `6.3706` edge `0.058` maxDD `-3.5466`
- `market_context_high->commodity_1h` score `-0.4273` n `91` status `ready` deltaP `-0.046` edge `0.0023` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.7725` n `91` status `ready` deltaP `-2.5562` edge `-0.012` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9227` n `91` status `ready` deltaP `-4.4383` edge `-0.0047` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9403` n `91` status `ready` deltaP `-5.0088` edge `0.0136` maxDD `-1.0609`
- `market_context_high->unknown_1h` score `-1.0301` n `91` status `ready` deltaP `-4.0682` edge `-0.0172` maxDD `-0.9885`
- `market_context_high->crypto_alt_1h` score `-1.1244` n `91` status `ready` deltaP `-1.7947` edge `0.0321` maxDD `-4.7735`
- `market_context_high->crypto_alt_4h` score `-1.1827` n `91` status `ready` deltaP `-8.4763` edge `0.0982` maxDD `-8.7986`
- `market_context_high->index_1h` score `-1.2248` n `91` status `ready` deltaP `-10.1879` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2882` n `91` status `ready` deltaP `-10.8651` edge `0.0005` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

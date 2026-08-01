# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T14:22:31.766480+00:00`
- Price records: `672`
- Market context records: `8630`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5191.4334` n `60` status `ready` deltaP `34.2345` edge `432.4333` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.175` n `48` status `ready` deltaP `53.7118` edge `1.1129` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.2785` n `60` status `ready` deltaP `21.9309` edge `0.4367` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.54` n `60` status `ready` deltaP `22.0833` edge `0.0835` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7011` n `60` status `ready` deltaP `15.0799` edge `0.0889` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.2227` n `60` status `ready` deltaP `7.7439` edge `0.1827` maxDD `-3.5385`
- `market_context_high->commodity_24h` score `0.9467` n `48` status `ready` deltaP `23.3355` edge `0.1811` maxDD `-11.5569`
- `market_context_high->crypto_alt_4h` score `0.693` n `56` status `ready` deltaP `10.1481` edge `0.1169` maxDD `-5.323`
- `news_risk_high->crypto_alt_4h` score `0.4572` n `60` status `ready` deltaP `11.2195` edge `0.123` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4335` n `60` status `ready` deltaP `8.1836` edge `0.0537` maxDD `-1.8813`
- `news_risk_high->fx_4h` score `0.329` n `60` status `ready` deltaP `14.7561` edge `0.0248` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `0.3279` n `60` status `ready` deltaP `6.2176` edge `0.0518` maxDD `-2.0972`
- `market_context_high->fx_24h` score `0.2574` n `48` status `ready` deltaP `12.3881` edge `0.0442` maxDD `-2.1692`
- `news_risk_high->metal_4h` score `0.1289` n `60` status `ready` deltaP `4.3699` edge `0.035` maxDD `-0.8085`
- `market_context_high->commodity_1h` score `0.1235` n `56` status `ready` deltaP `7.0038` edge `0.0177` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `0.1024` n `60` status `ready` deltaP `5.4491` edge `0.0049` maxDD `-0.2475`
- `market_context_high->fx_4h` score `0.0978` n `56` status `ready` deltaP `11.5418` edge `0.0152` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `0.0811` n `60` status `ready` deltaP `5.7884` edge `0.0085` maxDD `-0.5599`
- `news_risk_high->index_1h` score `0.0095` n `60` status `ready` deltaP `3.523` edge `0.0094` maxDD `-0.5338`
- `market_context_high->fx_1h` score `-0.2755` n `56` status `ready` deltaP `4.0205` edge `0.0005` maxDD `-0.6874`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T12:22:28.958561+00:00`
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

- `market_context_high->unknown_4h` score `31.7377` n `58` status `ready` deltaP `1.23` edge `2.6516` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `20.759` n `101` status `ready` deltaP `8.3178` edge `2.3603` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `15.0062` n `101` status `ready` deltaP `8.7029` edge `1.6806` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.3808` n `101` status `ready` deltaP `16.48` edge `0.2928` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.0845` n `101` status `ready` deltaP `19.8337` edge `0.2506` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.3924` n `101` status `ready` deltaP `14.8841` edge `0.1467` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7619` n `101` status `ready` deltaP `16.5308` edge `0.0889` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.3018` n `101` status `ready` deltaP `23.8913` edge `0.1382` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7156` n `58` status `ready` deltaP `5.4099` edge `0.0489` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6034` n `58` status `ready` deltaP `9.3795` edge `0.0133` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5118` n `101` status `ready` deltaP `13.6998` edge `0.0115` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3846` n `58` status `ready` deltaP `9.2247` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3792` n `101` status `ready` deltaP `10.47` edge `0.0254` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2787` n `101` status `ready` deltaP `14.6598` edge `0.0309` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2467` n `58` status `ready` deltaP `13.5618` edge `0.0049` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2339` n `58` status `ready` deltaP `5.2499` edge `0.0153` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1645` n `101` status `ready` deltaP `3.5913` edge `0.0067` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3593` n `101` status `ready` deltaP `1.0227` edge `0.0038` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.3894` n `58` status `ready` deltaP `2.2761` edge `-0.0027` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.478` n `101` status `ready` deltaP `8.7355` edge `-0.0351` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

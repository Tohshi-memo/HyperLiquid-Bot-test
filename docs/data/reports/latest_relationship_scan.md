# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T22:37:31.650347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `48.7577` n `50` status `ready` deltaP `11.5717` edge `3.986` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.2215` n `50` status `ready` deltaP `36.5872` edge `0.902` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.4697` n `50` status `ready` deltaP `26.4695` edge `0.8726` maxDD `-0.1274`
- `news_risk_high->equity_24h` score `7.323` n `50` status `ready` deltaP `32.0138` edge `0.4906` maxDD `-4.8351`
- `news_risk_high->index_24h` score `3.8896` n `50` status `ready` deltaP `38.7772` edge `0.0808` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.5928` n `50` status `ready` deltaP `42.3049` edge `0.0264` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3244` n `137` status `ready` deltaP `25.1702` edge `0.1499` maxDD `-0.5871`
- `news_risk_high->unknown_1h` score `2.7469` n `50` status `ready` deltaP `15.7784` edge `0.1593` maxDD `-0.8463`
- `news_risk_high->metal_24h` score `2.5` n `50` status `ready` deltaP `34.6149` edge `-0.0182` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.4328` n `50` status `ready` deltaP `19.4451` edge `0.0665` maxDD `-2.1389`
- `market_context_high->unknown_1h` score `1.3803` n `137` status `ready` deltaP `13.1507` edge `0.0723` maxDD `-1.5954`
- `news_risk_high->fx_1h` score `1.3467` n `50` status `ready` deltaP `18.4072` edge `0.0065` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2776` n `50` status `ready` deltaP `17.2635` edge `0.0193` maxDD `-0.2338`
- `news_risk_high->commodity_1h` score `0.5074` n `50` status `ready` deltaP `14.1497` edge `0.002` maxDD `-0.5024`
- `market_context_high->unknown_24h` score `0.2732` n `133` status `ready` deltaP `5.5567` edge `0.0588` maxDD `-3.1794`
- `news_risk_high->index_1h` score `0.103` n `50` status `ready` deltaP `6.9102` edge `0.0011` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0976` n `50` status `ready` deltaP `6.4756` edge `0.0047` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0882` n `50` status `ready` deltaP `5.2515` edge `-0.0011` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0295` n `50` status `ready` deltaP `8.378` edge `-0.0052` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4037` n `137` status `ready` deltaP `3.3415` edge `-0.0008` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

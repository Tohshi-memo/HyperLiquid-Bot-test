# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T21:53:17.610176+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11577`

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

- `risk_on_high->unknown_4h` score `27.6011` n `133` status `ready` deltaP `11.1326` edge `2.2877` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `27.6011` n `133` status `ready` deltaP `11.1326` edge `2.2877` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `20.836` n `167` status `ready` deltaP `12.7309` edge `1.721` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `15.2633` n `133` status `ready` deltaP `0.5931` edge `1.3257` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `15.2633` n `133` status `ready` deltaP `0.5931` edge `1.3257` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.7835` n `167` status `ready` deltaP `1.0479` edge `0.9547` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.9064` n `127` status `ready` deltaP `16.6502` edge `0.3991` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `0.4235` n `107` status `ready` deltaP `11.8964` edge `0.3705` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.4235` n `107` status `ready` deltaP `11.8964` edge `0.3705` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.3785` n `67` status `ready` deltaP `6.862` edge `0.0387` maxDD `-0.8733`
- `news_risk_high->crypto_alt_24h` score `0.2311` n `67` status `ready` deltaP `16.2261` edge `0.2149` maxDD `-19.4761`
- `risk_on_high->metal_1h` score `0.0875` n `133` status `ready` deltaP `12.1134` edge `0.0017` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0875` n `133` status `ready` deltaP `12.1134` edge `0.0017` maxDD `-1.699`
- `news_risk_high->equity_24h` score `0.0739` n `67` status `ready` deltaP `4.3221` edge `0.2274` maxDD `-15.4056`
- `news_risk_high->fx_4h` score `-0.0187` n `67` status `ready` deltaP `9.0417` edge `0.0038` maxDD `-1.2507`
- `news_risk_high->index_1h` score `-0.0344` n `67` status `ready` deltaP `5.0742` edge `-0.0029` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0726` n `133` status `ready` deltaP `5.4894` edge `-0.0014` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0726` n `133` status `ready` deltaP `5.4894` edge `-0.0014` maxDD `-0.5605`
- `risk_on_high->fx_24h` score `-0.1369` n `107` status `ready` deltaP `25.7075` edge `0.0808` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.1369` n `107` status `ready` deltaP `25.7075` edge `0.0808` maxDD `-4.2453`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

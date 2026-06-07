# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T06:52:23.332872+00:00`
- Price records: `672`
- Market context records: `3154`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7978`

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

- `market_context_high->commodity_24h` score `14.1262` n `111` status `ready` deltaP `47.7618` edge `0.9016` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.262` n `111` status `ready` deltaP `14.4097` edge `2.4736` maxDD `-71.142`
- `market_context_high->unknown_24h` score `12.0115` n `111` status `ready` deltaP `22.5835` edge `0.8992` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.7229` n `111` status `ready` deltaP `31.7192` edge `0.9059` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.117` n `111` status `ready` deltaP `13.4478` edge `1.408` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8776` n `144` status `ready` deltaP `18.8855` edge `0.1597` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1603` n `144` status `ready` deltaP `4.2623` edge `0.0272` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.1786` n `111` status `ready` deltaP `7.3715` edge `0.0004` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.5138` n `144` status `ready` deltaP `3.676` edge `0.0159` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.5852` n `144` status `ready` deltaP `6.0587` edge `0.1238` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.8892` n `144` status `ready` deltaP `2.8318` edge `0.0157` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.0079` n `144` status `ready` deltaP `2.9649` edge `0.0773` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1275` n `144` status `ready` deltaP `-10.6495` edge `-0.0053` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.1747` n `144` status `ready` deltaP `11.67` edge `0.0625` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.3929` n `144` status `ready` deltaP `6.8767` edge `0.0603` maxDD `-14.7778`
- `market_context_high->fx_4h` score `-1.4638` n `144` status `ready` deltaP `-13.6179` edge `-0.0084` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.0839` n `144` status `ready` deltaP `-4.3039` edge `-0.0056` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.8574` n `144` status `ready` deltaP `13.4146` edge `0.0748` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.9096` n `144` status `ready` deltaP `19.1565` edge `0.4343` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1305` n `144` status `ready` deltaP `1.8546` edge `-0.0706` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T09:22:27.856745+00:00`
- Price records: `672`
- Market context records: `8606`
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

- `news_risk_high->unknown_24h` score `4751.4339` n `64` status `ready` deltaP `34.6512` edge `395.7639` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.9632` n `34` status `ready` deltaP `50.2804` edge `1.2848` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.8097` n `64` status `ready` deltaP `20.2863` edge `0.4086` maxDD `-3.4427`
- `market_context_high->crypto_major_24h` score `4.2333` n `34` status `ready` deltaP `14.9659` edge `0.7032` maxDD `-16.8197`
- `market_context_high->fx_24h` score `3.7696` n `34` status `ready` deltaP `38.5157` edge `0.0912` maxDD `-0.3737`
- `news_risk_high->index_4h` score `2.2721` n `64` status `ready` deltaP `19.4849` edge `0.0785` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7346` n `64` status `ready` deltaP `16.1879` edge `0.0843` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.6083` n `62` status `ready` deltaP `11.9139` edge `0.1503` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.1156` n `64` status `ready` deltaP `7.8886` edge `0.168` maxDD `-3.5385`
- `market_context_high->metal_24h` score `0.785` n `34` status `ready` deltaP `8.0335` edge `0.0856` maxDD `-1.8995`
- `market_context_high->index_24h` score `0.5146` n `34` status `ready` deltaP `19.2986` edge `0.0346` maxDD `-3.7831`
- `news_risk_high->crypto_alt_4h` score `0.4544` n `64` status `ready` deltaP `11.5107` edge `0.1207` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.3924` n `64` status `ready` deltaP `7.5883` edge `0.0524` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3548` n `64` status `ready` deltaP `6.9904` edge `0.0501` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1095` n `64` status `ready` deltaP `5.6591` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0509` n `64` status `ready` deltaP `11.6843` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0382` n `64` status `ready` deltaP `4.1503` edge `0.0089` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.0257` n `64` status `ready` deltaP `2.8658` edge `0.0318` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.1174` n `62` status `ready` deltaP `8.5089` edge `0.0131` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1284` n `64` status `ready` deltaP `3.3352` edge `0.0074` maxDD `-0.5599`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

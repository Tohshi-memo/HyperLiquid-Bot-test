# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T21:52:28.596270+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1490.9646` n `98` status `ready` deltaP `3.4722` edge `124.2239` maxDD `0.0`
- `news_risk_high->equity_24h` score `48.1047` n `30` status `ready` deltaP `64.0278` edge `3.6525` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.4688` n `30` status `ready` deltaP `55.6402` edge `1.3348` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.5381` n `98` status `ready` deltaP `46.712` edge `2.0077` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.6639` n `98` status `ready` deltaP `32.9472` edge `1.8727` maxDD `-13.3222`
- `news_risk_high->crypto_major_24h` score `13.902` n `30` status `ready` deltaP `22.2222` edge `1.7485` maxDD `-6.8139`
- `news_risk_high->index_24h` score `8.1191` n `30` status `ready` deltaP `55.5208` edge `0.3368` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.5257` n `30` status `ready` deltaP `54.8611` edge `0.2614` maxDD `0.0`
- `news_risk_high->metal_4h` score `7.1152` n `30` status `ready` deltaP `55.9655` edge `0.2243` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.4276` n `30` status `ready` deltaP `26.0279` edge `0.3006` maxDD `-0.4122`
- `news_risk_high->crypto_alt_24h` score `4.4785` n `30` status `ready` deltaP `-0.5902` edge `0.8277` maxDD `-29.0448`
- `news_risk_high->crypto_major_4h` score `4.3958` n `30` status `ready` deltaP `17.9268` edge `0.2895` maxDD `-1.7491`
- `news_risk_high->crypto_alt_4h` score `4.3827` n `30` status `ready` deltaP `28.0793` edge `0.4514` maxDD `-4.137`
- `news_risk_high->index_4h` score `4.1982` n `30` status `ready` deltaP `34.4004` edge `0.143` maxDD `-0.1319`
- `news_risk_high->commodity_4h` score `2.8226` n `30` status `ready` deltaP `29.563` edge `0.0544` maxDD `-0.3018`
- `news_risk_high->metal_1h` score `2.4955` n `30` status `ready` deltaP `26.0279` edge `0.0562` maxDD `-0.0743`
- `news_risk_high->crypto_major_1h` score `2.0295` n `30` status `ready` deltaP `14.98` edge `0.1044` maxDD `-1.4777`
- `news_risk_high->index_1h` score `1.6896` n `30` status `ready` deltaP `19.8104` edge `0.0305` maxDD `-0.0751`
- `news_risk_high->crypto_alt_1h` score `1.6599` n `30` status `ready` deltaP `19.3613` edge `0.1364` maxDD `-2.5469`
- `market_context_high->metal_1h` score `-0.4766` n `98` status `ready` deltaP `-0.3666` edge `0.0015` maxDD `-2.1461`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

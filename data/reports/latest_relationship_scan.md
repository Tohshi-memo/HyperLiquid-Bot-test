# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T10:52:30.403033+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8380`

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

- `market_context_high->unknown_4h` score `39.5868` n `149` status `ready` deltaP `-0.311` edge `3.3243` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.4655` n `52` status `ready` deltaP `-7.5516` edge `1.195` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.4655` n `52` status `ready` deltaP `-7.5516` edge `1.195` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8708` n `52` status `ready` deltaP `50.0` edge `0.4059` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8708` n `52` status `ready` deltaP `50.0` edge `0.4059` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5717` n `149` status `ready` deltaP `43.2886` edge `0.3949` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.1669` n `87` status `ready` deltaP `20.4566` edge `0.4847` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8183` n `52` status `ready` deltaP `32.5399` edge `0.0529` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8183` n `52` status `ready` deltaP `32.5399` edge `0.0529` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.718` n `149` status `ready` deltaP `29.0422` edge `0.0747` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.2676` n `87` status `ready` deltaP `16.4564` edge `0.1365` maxDD `-3.3619`
- `market_context_high->commodity_1h` score `1.1169` n `149` status `ready` deltaP `16.2109` edge `0.0227` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.9145` n `52` status `ready` deltaP `18.2158` edge `-0.041` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.9145` n `52` status `ready` deltaP `18.2158` edge `-0.041` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.7796` n `149` status `ready` deltaP `15.4409` edge `-0.0164` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4936` n `52` status `ready` deltaP `9.293` edge `0.0144` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4936` n `52` status `ready` deltaP `9.293` edge `0.0144` maxDD `-0.1507`
- `news_risk_high->fx_4h` score `0.3607` n `87` status `ready` deltaP `9.7368` edge `0.026` maxDD `-0.2398`
- `news_risk_high->equity_1h` score `0.2756` n `95` status `ready` deltaP `9.8408` edge `0.0219` maxDD `-1.8403`
- `news_risk_high->crypto_major_4h` score `0.0213` n `87` status `ready` deltaP `10.5568` edge `0.257` maxDD `-19.972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

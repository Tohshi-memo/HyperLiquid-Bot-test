# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T11:37:32.610224+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8366`

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

- `market_context_high->unknown_4h` score `39.8232` n `149` status `ready` deltaP `-0.311` edge `3.344` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7019` n `52` status `ready` deltaP `-7.5516` edge `1.2147` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7019` n `52` status `ready` deltaP `-7.5516` edge `1.2147` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8895` n `52` status `ready` deltaP `50.1736` edge `0.4063` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8895` n `52` status `ready` deltaP `50.1736` edge `0.4063` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5903` n `149` status `ready` deltaP `43.4622` edge `0.3953` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.1234` n `90` status `ready` deltaP `20.2643` edge `0.4804` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8219` n `52` status `ready` deltaP `32.5399` edge `0.0532` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8219` n `52` status `ready` deltaP `32.5399` edge `0.0532` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7216` n `149` status `ready` deltaP `29.0422` edge `0.075` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.1181` n `149` status `ready` deltaP `16.2109` edge `0.0228` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `1.0623` n `90` status `ready` deltaP `14.5766` edge `0.1227` maxDD `-3.3619`
- `risk_on_high->fx_24h` score `0.8548` n `52` status `ready` deltaP `17.695` edge `-0.0425` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.8548` n `52` status `ready` deltaP `17.695` edge `-0.0425` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.7199` n `149` status `ready` deltaP `14.9201` edge `-0.0179` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4948` n `52` status `ready` deltaP `9.293` edge `0.0145` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4948` n `52` status `ready` deltaP `9.293` edge `0.0145` maxDD `-0.1507`
- `news_risk_high->fx_4h` score `0.3998` n `90` status `ready` deltaP `10.3523` edge `0.0269` maxDD `-0.2398`
- `news_risk_high->equity_1h` score `0.2748` n `95` status `ready` deltaP `9.8408` edge `0.0218` maxDD `-1.8403`
- `news_risk_high->crypto_major_4h` score `0.2032` n `90` status `ready` deltaP `11.7446` edge `0.2724` maxDD `-19.972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T14:52:27.933105+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8438`

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

- `market_context_high->unknown_4h` score `39.8986` n `149` status `ready` deltaP `-0.4634` edge `3.3513` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7773` n `52` status `ready` deltaP `-7.704` edge `1.222` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7773` n `52` status `ready` deltaP `-7.704` edge `1.222` maxDD `-0.4694`
- `news_risk_high->crypto_alt_24h` score `11.1297` n `34` status `ready` deltaP `24.3873` edge `0.9028` maxDD `-9.3661`
- `risk_on_high->commodity_24h` score `8.7227` n `52` status `ready` deltaP `48.9583` edge `0.4005` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.7227` n `52` status `ready` deltaP `48.9583` edge `0.4005` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4235` n `149` status `ready` deltaP `42.2469` edge `0.3895` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.2832` n `95` status `ready` deltaP `21.4923` edge `0.4927` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.7823` n `52` status `ready` deltaP `32.5399` edge `0.0499` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7823` n `52` status `ready` deltaP `32.5399` edge `0.0499` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.682` n `149` status `ready` deltaP `29.0422` edge `0.0717` maxDD `-0.345`
- `news_risk_high->crypto_major_24h` score `1.904` n `34` status `ready` deltaP `-11.7749` edge `0.5221` maxDD `-13.2931`
- `market_context_high->commodity_1h` score `1.0798` n `149` status `ready` deltaP `15.9115` edge `0.0216` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.6981` n `95` status `ready` deltaP `12.5337` edge `0.1001` maxDD `-4.1995`
- `risk_on_high->fx_24h` score `0.6765` n `52` status `ready` deltaP `16.3061` edge `-0.0481` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6765` n `52` status `ready` deltaP `16.3061` edge `-0.0481` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.5416` n `149` status `ready` deltaP `13.5312` edge `-0.0235` maxDD `-0.0593`
- `news_risk_high->crypto_major_4h` score `0.4612` n `95` status `ready` deltaP `13.5574` edge `0.2934` maxDD `-19.972`
- `risk_on_high->commodity_1h` score `0.4565` n `52` status `ready` deltaP `8.9936` edge `0.0133` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4565` n `52` status `ready` deltaP `8.9936` edge `0.0133` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

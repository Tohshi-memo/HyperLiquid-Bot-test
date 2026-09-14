# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T21:52:26.349817+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10608`

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

- `news_risk_high->unknown_4h` score `397.0148` n `78` status `ready` deltaP `-22.4554` edge `33.3236` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.6547` n `78` status `ready` deltaP `18.9236` edge `1.9284` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.761` n `78` status `ready` deltaP `45.8601` edge `1.5468` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.3233` n `78` status `ready` deltaP `32.9594` edge `1.2876` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.9168` n `78` status `ready` deltaP `42.5614` edge `1.054` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7339` n `78` status `ready` deltaP `61.9391` edge `0.3325` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4409` n `78` status `ready` deltaP `37.7938` edge `0.3302` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `6.1829` n `127` status `ready` deltaP `36.1111` edge `0.2745` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.7893` n `52` status `ready` deltaP `36.1111` edge `0.2417` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7893` n `52` status `ready` deltaP `36.1111` edge `0.2417` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.4159` n `52` status `ready` deltaP `49.6394` edge `0.0413` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.4159` n `52` status `ready` deltaP `49.6394` edge `0.0413` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.0666` n `127` status `ready` deltaP `46.8381` edge `0.0482` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1105` n `52` status `ready` deltaP `27.0521` edge `0.0305` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1105` n `52` status `ready` deltaP `27.0521` edge `0.0305` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.9108` n `137` status `ready` deltaP `22.462` edge `0.0513` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7275` n `137` status `ready` deltaP `12.2132` edge `0.0169` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.655` n `78` status `ready` deltaP `16.2015` edge `0.0388` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2121` n `52` status `ready` deltaP `6.5984` edge `0.0089` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2121` n `52` status `ready` deltaP `6.5984` edge `0.0089` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

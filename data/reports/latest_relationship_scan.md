# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T18:37:25.466707+00:00`
- Price records: `672`
- Market context records: `2167`
- Flow alert records: `8134`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.9673` n `135` status `ready` deltaP `36.6215` edge `0.9301` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8804` n `135` status `ready` deltaP `42.1997` edge `0.7617` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5041` n `135` status `ready` deltaP `22.6784` edge `0.3824` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `3.895` n `43` status `ready` deltaP `32.1575` edge `0.3521` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.7537` n `135` status `ready` deltaP `24.8193` edge `0.2568` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.3382` n `135` status `ready` deltaP `17.8643` edge `0.2068` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.1421` n `135` status `ready` deltaP `16.517` edge `0.2381` maxDD `-4.9097`
- `market_context_high->index_4h` score `2.7964` n `135` status `ready` deltaP `22.859` edge `0.149` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.7953` n `135` status `ready` deltaP `11.5625` edge `0.2787` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.7178` n `135` status `ready` deltaP `27.6042` edge `0.5745` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `2.5145` n `135` status `ready` deltaP `20.6134` edge `1.0302` maxDD `-61.2872`
- `news_risk_high->fx_4h` score `2.0892` n `43` status `ready` deltaP `26.6697` edge `0.0147` maxDD `-0.1382`
- `market_context_high->equity_24h` score `2.0195` n `135` status `ready` deltaP `23.9005` edge `0.4988` maxDD `-33.1875`
- `market_context_high->metal_4h` score `1.5588` n `135` status `ready` deltaP `18.0815` edge `0.1481` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.5357` n `43` status `ready` deltaP `15.8395` edge `0.0947` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.3815` n `43` status `ready` deltaP `-2.2264` edge `0.3127` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.3196` n `43` status `ready` deltaP `21.1948` edge `0.0156` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.8033` n `43` status `ready` deltaP `10.7645` edge `0.0992` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.5191` n `135` status `ready` deltaP `10.0643` edge `0.055` maxDD `-2.6402`
- `news_risk_high->fx_1h` score `0.4621` n `43` status `ready` deltaP `8.1395` edge `0.0099` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

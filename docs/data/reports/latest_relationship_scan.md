# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T07:07:28.509489+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `46.623` n `51` status `ready` deltaP `11.6319` edge `3.8077` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.7306` n `53` status `ready` deltaP `22.6933` edge `0.8362` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `8.3452` n `51` status `ready` deltaP `31.25` edge `0.4871` maxDD `0.0`
- `news_risk_high->equity_24h` score `7.0929` n `51` status `ready` deltaP `29.9939` edge `0.4842` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0544` n `51` status `ready` deltaP `40.2676` edge `0.0846` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.7767` n `53` status `ready` deltaP `33.4388` edge `0.0219` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7411` n `53` status `ready` deltaP `15.4135` edge `0.1612` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.4558` n `134` status `ready` deltaP `20.891` edge `0.1062` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7751` n `53` status `ready` deltaP `19.7365` edge `0.0934` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.4337` n `51` status `ready` deltaP `29.1156` edge `-0.0704` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0698` n `53` status `ready` deltaP `15.0209` edge `0.006` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0594` n `136` status `ready` deltaP `11.4873` edge `0.0566` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `0.4614` n `53` status `ready` deltaP `13.0748` edge `0.0084` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4523` n `53` status `ready` deltaP `10.9762` edge `-0.0042` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.0561` n `53` status `ready` deltaP `5.7467` edge `0.0061` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0729` n `53` status `ready` deltaP `3.8499` edge `0.0003` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4434` n `136` status `ready` deltaP `2.5625` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4882` n `53` status `ready` deltaP `-0.9123` edge `-0.012` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7213` n `53` status `ready` deltaP `2.9855` edge `-0.0269` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0466` n `53` status `ready` deltaP `-2.1255` edge `0.0033` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T16:07:46.845852+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `44.1136` n `51` status `ready` deltaP `4.3403` edge `3.6472` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.54` n `53` status `ready` deltaP `24.0652` edge `0.8945` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.4148` n `51` status `ready` deltaP `32.5981` edge `0.577` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.2746` n `51` status `ready` deltaP `42.5245` edge `0.0879` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1586` n `53` status `ready` deltaP `16.162` edge `0.191` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0136` n `53` status `ready` deltaP `35.7254` edge `0.0264` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.5814` n `133` status `ready` deltaP `22.2068` edge `0.1079` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.9115` n `53` status `ready` deltaP `21.2609` edge `0.0946` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1992` n `53` status `ready` deltaP `16.5179` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5229` n `53` status `ready` deltaP `14.4221` edge `0.0073` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3996` n `53` status `ready` deltaP `10.5271` edge `-0.0056` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2572` n `53` status `ready` deltaP `8.1857` edge `0.0066` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.141` n `133` status `ready` deltaP `11.7216` edge `-0.0215` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0394` n `53` status `ready` deltaP `4.4487` edge `0.0006` maxDD `-0.1583`
- `news_risk_high->metal_24h` score `-0.2814` n `51` status `ready` deltaP `23.9073` edge `-0.1786` maxDD `-0.0053`
- `news_risk_high->metal_4h` score `-0.3912` n `53` status `ready` deltaP `5.8818` edge `-0.0187` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4117` n `133` status `ready` deltaP `3.0976` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4259` n `53` status `ready` deltaP `-0.3135` edge `-0.0108` maxDD `-0.1413`
- `news_risk_high->crypto_alt_24h` score `-0.8305` n `51` status `ready` deltaP `20.8333` edge `-0.2081` maxDD `0.0`
- `market_context_high->metal_4h` score `-0.8916` n `133` status `ready` deltaP `4.8746` edge `-0.0431` maxDD `-2.4293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

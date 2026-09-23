# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T05:52:31.922909+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9818`

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

- `market_context_high->unknown_4h` score `46.8833` n `46` status `ready` deltaP `7.9268` edge `3.8541` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.3547` n `46` status `ready` deltaP `13.5341` edge `2.3716` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6645` n `46` status `ready` deltaP `12.1453` edge `1.3178` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.456` n `46` status `ready` deltaP `10.5903` edge `0.9674` maxDD `0.0`
- `market_context_high->index_24h` score `5.6512` n `46` status `ready` deltaP `20.8258` edge `0.3408` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.6611` n `96` status `ready` deltaP `-9.2014` edge `1.1356` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.461` n `96` status `ready` deltaP `34.8958` edge `0.257` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.6206` n `100` status `ready` deltaP `13.0976` edge `0.1888` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1611` n `46` status `ready` deltaP `25.2982` edge `0.0248` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.0206` n `100` status `ready` deltaP `8.0671` edge `0.2144` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.8326` n `103` status `ready` deltaP `10.6127` edge `0.131` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4185` n `103` status `ready` deltaP `12.8583` edge `0.076` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3894` n `100` status `ready` deltaP `20.622` edge `0.0419` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.9838` n `96` status `ready` deltaP `25.3472` edge `0.1161` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.8077` n `46` status `ready` deltaP `6.9123` edge `0.0455` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7567` n `46` status `ready` deltaP `5.8524` edge `0.0547` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6938` n `46` status `ready` deltaP `10.8045` edge `0.0111` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.4194` n `103` status `ready` deltaP `12.8074` edge `0.0089` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2939` n `103` status `ready` deltaP `8.7059` edge `0.0108` maxDD `-0.2147`
- `market_context_high->metal_24h` score `0.2172` n `46` status `ready` deltaP `16.0176` edge `-0.0653` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

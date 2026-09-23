# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T23:37:32.880563+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9834`

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

- `market_context_high->unknown_1h` score `72.1518` n `47` status `ready` deltaP `10.2657` edge `5.9513` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `35.0157` n `46` status `ready` deltaP `21.8675` edge `2.7878` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.3107` n `46` status `ready` deltaP `19.2633` edge `1.5742` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `18.7448` n `46` status `ready` deltaP `16.8403` edge `1.4498` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `9.3596` n `97` status `ready` deltaP `-1.6198` edge `1.4766` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.84` n `46` status `ready` deltaP `28.2911` edge `0.3901` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.8708` n `103` status `ready` deltaP `14.3841` edge `0.4098` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `4.8541` n `97` status `ready` deltaP `-3.7783` edge `0.9178` maxDD `-32.7147`
- `news_risk_high->crypto_major_4h` score `4.603` n `103` status `ready` deltaP `17.4328` edge `0.3251` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.5761` n `103` status `ready` deltaP `13.4571` edge `0.174` maxDD `-1.5895`
- `news_risk_high->commodity_24h` score `2.4992` n `97` status `ready` deltaP `24.5633` edge `0.1624` maxDD `-2.431`
- `market_context_high->index_4h` score `2.4442` n `47` status `ready` deltaP `28.8434` edge `0.0268` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0193` n `103` status `ready` deltaP `15.7026` edge `0.1071` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.6748` n `46` status `ready` deltaP `22.2676` edge `0.0145` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.571` n `103` status `ready` deltaP `23.0716` edge `0.0407` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.3369` n `47` status `ready` deltaP `10.742` edge `0.0816` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1086` n `97` status `ready` deltaP `27.6221` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7678` n `47` status `ready` deltaP `12.5143` edge `0.0084` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.7506` n `97` status `ready` deltaP `18.3455` edge `0.0657` maxDD `-3.0086`
- `news_risk_high->metal_1h` score `0.6254` n `103` status `ready` deltaP `15.2026` edge `0.0101` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

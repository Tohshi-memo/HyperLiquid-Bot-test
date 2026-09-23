# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T19:22:31.610957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9883`

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

- `market_context_high->unknown_1h` score `82.9915` n `47` status `ready` deltaP `9.8166` edge `6.8576` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `32.874` n `46` status `ready` deltaP `18.9161` edge `2.629` maxDD `-0.5817`
- `market_context_high->equity_24h` score `18.6934` n `46` status `ready` deltaP `16.3119` edge `1.4591` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.7055` n `46` status `ready` deltaP `13.8889` edge `1.2162` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.1805` n `96` status `ready` deltaP `-3.8194` edge `1.393` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.3231` n `46` status `ready` deltaP `25.3397` edge `0.3667` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.4078` n `103` status `ready` deltaP `16.8231` edge `0.3129` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.0876` n `103` status `ready` deltaP `11.945` edge `0.3608` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `2.9223` n `96` status `ready` deltaP `27.2569` edge `0.1797` maxDD `-2.431`
- `news_risk_high->crypto_alt_24h` score `2.8146` n `96` status `ready` deltaP `-5.9028` edge `0.762` maxDD `-32.7147`
- `news_risk_high->crypto_alt_1h` score `2.3795` n `103` status `ready` deltaP `12.5589` edge `0.1636` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.3023` n `47` status `ready` deltaP `27.6239` edge `0.0231` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0373` n `103` status `ready` deltaP `15.8523` edge `0.1076` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4064` n `103` status `ready` deltaP `21.0899` edge `0.0402` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2308` n `96` status `ready` deltaP `29.1667` edge `0.1223` maxDD `-1.7159`
- `market_context_high->metal_24h` score `0.9431` n `46` status `ready` deltaP `19.3162` edge `-0.0268` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.879` n `47` status `ready` deltaP `8.303` edge `0.0597` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6564` n `47` status `ready` deltaP `11.3167` edge `0.0071` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.5787` n `103` status `ready` deltaP `14.7535` edge `0.0092` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.444` n `96` status `ready` deltaP `16.1459` edge `0.0337` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

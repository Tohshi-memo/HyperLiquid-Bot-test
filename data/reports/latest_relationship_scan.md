# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T15:22:32.862557+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9888`

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

- `market_context_high->unknown_1h` score `80.42` n `47` status `ready` deltaP `9.2178` edge `6.6473` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `30.7066` n `46` status `ready` deltaP `16.1383` edge `2.4669` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.42` n `46` status `ready` deltaP `13.5341` edge `1.3715` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.9969` n `46` status `ready` deltaP `11.1111` edge `1.009` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `6.013` n `96` status `ready` deltaP `-6.5972` edge `1.2309` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.8921` n `46` status `ready` deltaP `22.5619` edge `0.3493` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `3.4863` n `103` status `ready` deltaP `14.9938` edge `0.2483` maxDD `-2.619`
- `news_risk_high->commodity_24h` score `3.2685` n `96` status `ready` deltaP `29.5139` edge `0.1935` maxDD `-2.431`
- `news_risk_high->crypto_alt_4h` score `2.7505` n `103` status `ready` deltaP `9.8109` edge `0.2636` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.5164` n `46` status `ready` deltaP `29.1092` edge `0.029` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `2.1324` n `103` status `ready` deltaP `11.8104` edge `0.148` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.819` n `103` status `ready` deltaP `14.8044` edge `0.0964` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.3627` n `46` status `ready` deltaP `9.6633` edge `0.0798` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2117` n `103` status `ready` deltaP `18.9557` edge `0.0382` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1673` n `96` status `ready` deltaP `28.125` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.6948` n `47` status `ready` deltaP `11.6161` edge `0.0083` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6674` n `103` status `ready` deltaP `15.3523` edge `0.0126` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.4128` n `47` status `ready` deltaP `7.2748` edge `0.0263` maxDD `-1.5655`
- `market_context_high->metal_24h` score `0.3944` n `46` status `ready` deltaP `16.5384` edge `-0.054` maxDD `-0.2042`
- `news_risk_high->metal_4h` score `0.2459` n `103` status `ready` deltaP `12.8981` edge `0.0413` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

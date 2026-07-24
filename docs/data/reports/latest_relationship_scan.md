# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T15:52:26.558589+00:00`
- Price records: `672`
- Market context records: `7789`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `7.6103` n `132` status `ready` deltaP `28.1068` edge `0.581` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.5209` n `133` status `ready` deltaP `14.3131` edge `0.2404` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.0371` n `133` status `ready` deltaP `14.194` edge `0.1636` maxDD `-6.7444`
- `market_context_high->equity_4h` score `1.001` n `133` status `ready` deltaP `3.4984` edge `0.2963` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `0.995` n `133` status `ready` deltaP `12.8585` edge `0.0413` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8375` n `133` status `ready` deltaP `8.6569` edge `0.1238` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8037` n `132` status `ready` deltaP `25.1848` edge `0.0439` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6206` n `133` status `ready` deltaP `7.7457` edge `0.086` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3266` n `133` status `ready` deltaP `8.194` edge `0.0156` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.2754` n `133` status `ready` deltaP `7.0808` edge `0.0351` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1688` n `133` status `ready` deltaP `4.2783` edge `0.0288` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0283` n `133` status `ready` deltaP `4.8963` edge `0.0109` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1529` n `133` status `ready` deltaP `11.6288` edge `0.0487` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3606` n `133` status `ready` deltaP `1.2746` edge `0.0002` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.5013` n `132` status `ready` deltaP `11.2607` edge `0.0415` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9381` n `133` status `ready` deltaP `0.5189` edge `0.0187` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3342` n `133` status `ready` deltaP `-1.5624` edge `0.0022` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5269` n `133` status `ready` deltaP `0.5283` edge `0.0747` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.7046` n `132` status `ready` deltaP `-10.0913` edge `0.059` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.4084` n `133` status `ready` deltaP `14.6643` edge `0.123` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

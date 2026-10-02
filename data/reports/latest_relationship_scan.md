# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T07:37:34.175874+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5056`

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

- `market_context_high->unknown_1h` score `340.7867` n `50` status `ready` deltaP `9.8263` edge `28.3383` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.3981` n `50` status `ready` deltaP `8.8415` edge `23.8909` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.6681` n `62` status `ready` deltaP `39.3089` edge `0.8979` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0447` n `50` status `ready` deltaP `36.1667` edge `0.8209` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `9.2128` n `62` status `ready` deltaP `36.6768` edge `0.5717` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.8725` n `50` status `ready` deltaP `16.5347` edge `0.8001` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.8893` n `50` status `ready` deltaP `17.5427` edge `0.5275` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8977` n `50` status `ready` deltaP `15.5793` edge `0.4336` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.8421` n `91` status `ready` deltaP `14.8101` edge `0.3558` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.049` n `50` status `ready` deltaP `14.3542` edge `0.4814` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9117` n `50` status `ready` deltaP `32.689` edge `0.0382` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8965` n `50` status `ready` deltaP `13.9042` edge `0.215` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.85` n `50` status `ready` deltaP `13.8503` edge `0.1902` maxDD `-2.2692`
- `market_context_high->fx_1h` score `1.4627` n `50` status `ready` deltaP `20.491` edge `0.0117` maxDD `-0.113`
- `news_risk_high->equity_4h` score `1.3361` n `91` status `ready` deltaP `22.4387` edge `0.0913` maxDD `-2.9013`
- `market_context_high->index_24h` score `1.0162` n `50` status `ready` deltaP `16.1806` edge `0.0795` maxDD `-1.2338`
- `news_risk_high->metal_24h` score `0.772` n `62` status `ready` deltaP `2.4194` edge `0.1756` maxDD `-2.192`
- `news_risk_high->commodity_24h` score `0.7467` n `62` status `ready` deltaP `16.2242` edge `0.1081` maxDD `-4.6429`
- `news_risk_high->crypto_alt_1h` score `0.6066` n `103` status `ready` deltaP `4.2149` edge `0.0787` maxDD `-2.4998`
- `market_context_high->fx_24h` score `0.5102` n `50` status `ready` deltaP `14.4306` edge `0.071` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

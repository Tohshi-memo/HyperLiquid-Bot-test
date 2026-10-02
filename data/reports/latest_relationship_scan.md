# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T00:22:34.882515+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6602`

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

- `market_context_high->unknown_1h` score `338.6196` n `50` status `ready` deltaP `9.6766` edge `28.1587` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.2451` n `50` status `ready` deltaP `8.3841` edge `23.8812` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.4372` n `85` status `ready` deltaP `37.5777` edge `1.3902` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.8302` n `50` status `ready` deltaP `35.6458` edge `0.8065` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2669` n `50` status `ready` deltaP `19.0671` edge `0.5488` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.7333` n `50` status `ready` deltaP `13.9306` edge `0.6392` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `4.9886` n `50` status `ready` deltaP `16.3415` edge `0.4361` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.6601` n `50` status `ready` deltaP `19.0417` edge `0.5285` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `3.5757` n `85` status `ready` deltaP `15.9987` edge `0.5067` maxDD `-15.8971`
- `market_context_high->crypto_major_1h` score `3.0395` n `50` status `ready` deltaP `14.7485` edge `0.2` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9949` n `50` status `ready` deltaP `14.0539` edge `0.2222` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.964` n `50` status `ready` deltaP `33.2988` edge `0.0385` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.8344` n `98` status `ready` deltaP `24.9595` edge `0.1394` maxDD `-2.9013`
- `news_risk_high->crypto_alt_4h` score `2.4107` n `98` status `ready` deltaP `9.6068` edge `0.2712` maxDD `-6.4152`
- `news_risk_high->equity_24h` score `2.2234` n `85` status `ready` deltaP `14.5711` edge `0.4228` maxDD `-9.4579`
- `news_risk_high->commodity_24h` score `1.8125` n `85` status `ready` deltaP `28.2271` edge `0.1566` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.6312` n `85` status `ready` deltaP `17.7185` edge `0.2184` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.5378` n `85` status `ready` deltaP `18.9093` edge `0.0499` maxDD `-0.4916`
- `market_context_high->fx_1h` score `1.4879` n `50` status `ready` deltaP `20.7904` edge `0.0118` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9206` n `50` status `ready` deltaP `14.7917` edge `0.0765` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

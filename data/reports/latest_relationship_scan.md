# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T08:22:39.274879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4052`

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

- `market_context_high->unknown_24h` score `84.6722` n `30` status `ready` deltaP `3.9931` edge `7.0294` maxDD `0.0`
- `news_risk_high->equity_24h` score `49.733` n `50` status `ready` deltaP `53.4514` edge `3.8587` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1059` n `50` status `ready` deltaP `40.6389` edge `2.5493` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.3902` n `30` status `ready` deltaP `12.1527` edge `1.5226` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.2414` n `30` status `ready` deltaP `42.6389` edge `1.6122` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.111` n `50` status `ready` deltaP `38.3049` edge `0.8669` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.5282` n `50` status `ready` deltaP `22.8194` edge `1.52` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.2459` n `50` status `ready` deltaP `44.7708` edge `0.3357` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1002` n `50` status `ready` deltaP `40.9722` edge `0.2352` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9868` n `50` status `ready` deltaP `44.3841` edge `0.1573` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.2174` n `50` status `ready` deltaP `26.5366` edge `0.3181` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.198` n `50` status `ready` deltaP `20.5366` edge `0.3505` maxDD `-9.0062`
- `market_context_high->metal_24h` score `3.871` n `30` status `ready` deltaP `47.5695` edge `0.2683` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.7683` n `50` status `ready` deltaP `19.4012` edge `0.2477` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.694` n `50` status `ready` deltaP `34.2866` edge `0.1046` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5353` n `50` status `ready` deltaP `24.3415` edge `0.084` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.191` n `50` status `ready` deltaP `24.8443` edge `0.0424` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.1777` n `50` status `ready` deltaP `15.8503` edge `0.0226` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9925` n `50` status `ready` deltaP `18.9028` edge `0.2185` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7749` n `50` status `ready` deltaP `19.4431` edge `0.0749` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

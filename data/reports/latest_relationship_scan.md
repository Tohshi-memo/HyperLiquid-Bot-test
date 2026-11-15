# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T19:07:26.849706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8274`

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

- `market_context_high->unknown_24h` score `563.3109` n `62` status `ready` deltaP `3.9861` edge `46.916` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.7329` n `50` status `ready` deltaP `50.565` edge `3.5446` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.842` n `62` status `ready` deltaP `46.436` edge `3.2481` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.929` n `62` status `ready` deltaP `63.18` edge `2.5139` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.2117` n `50` status `ready` deltaP `46.2149` edge `2.7821` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.1979` n `50` status `ready` deltaP `38.7622` edge `0.8711` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.4686` n `50` status `ready` deltaP `20.0832` edge `1.5306` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1664` n `62` status `ready` deltaP `49.4074` edge `0.3598` maxDD `-0.0251`
- `market_context_high->metal_24h` score `6.7272` n `62` status `ready` deltaP `63.767` edge `0.5265` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.6023` n `50` status `ready` deltaP `42.2461` edge `0.2989` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.5651` n `50` status `ready` deltaP `43.1542` edge `0.2594` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `5.7864` n `62` status `ready` deltaP `14.0214` edge `1.2549` maxDD `-64.2943`
- `news_risk_high->crypto_major_4h` score `5.3133` n `50` status `ready` deltaP `22.8232` edge `0.4282` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.9162` n `50` status `ready` deltaP `44.5366` edge `0.1504` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6698` n `50` status `ready` deltaP `27.4512` edge `0.3497` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0367` n `50` status `ready` deltaP `21.6467` edge `0.2551` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6784` n `50` status `ready` deltaP `34.2866` edge `0.1033` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5671` n `50` status `ready` deltaP `24.7988` edge `0.0836` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1849` n `50` status `ready` deltaP `24.994` edge `0.0409` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.307` n `50` status `ready` deltaP `17.3473` edge `0.0234` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

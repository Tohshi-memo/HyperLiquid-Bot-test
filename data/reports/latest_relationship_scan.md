# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T19:22:46.531370+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4374`

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

- `news_risk_high->equity_24h` score `53.5554` n `50` status `ready` deltaP `59.1572` edge `4.1392` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.7108` n `50` status `ready` deltaP `39.8653` edge `2.5038` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.9433` n `30` status `ready` deltaP `13.126` edge `1.5622` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.3482` n `50` status `ready` deltaP `43.86` edge `1.0163` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `11.8463` n `30` status `ready` deltaP `41.8653` edge `1.5667` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.8877` n `50` status `ready` deltaP `23.7927` edge `1.5596` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0275` n `50` status `ready` deltaP `50.1762` edge `0.3648` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2698` n `50` status `ready` deltaP `41.2781` edge `0.2473` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3115` n `50` status `ready` deltaP `46.8828` edge `0.1677` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.8712` n `50` status `ready` deltaP `28.274` edge `0.361` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.5376` n `50` status `ready` deltaP `22.4262` edge `0.3662` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.454` n `50` status `ready` deltaP `21.8685` edge `0.2884` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0458` n `50` status `ready` deltaP `36.7945` edge `0.1172` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.7864` n `30` status `ready` deltaP `46.9776` edge `0.2614` maxDD `-3.7989`
- `news_risk_high->index_4h` score `3.0858` n `50` status `ready` deltaP `28.8371` edge `0.0999` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2852` n `50` status `ready` deltaP `25.6622` edge `0.0448` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5008` n `50` status `ready` deltaP `19.2138` edge `0.0271` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9079` n `50` status `ready` deltaP `18.3109` edge `0.2116` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8923` n `50` status `ready` deltaP `18.1106` edge `0.0916` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8059` n `50` status `ready` deltaP `19.0643` edge `0.0814` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

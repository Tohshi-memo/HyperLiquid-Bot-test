# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T11:22:29.945243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1538` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0749` n `13`; crypto_alt avg `-0.0895` n `239`; crypto_major avg `-0.0931` n `8`; equity avg `0.145` n `160`; fx avg `-0.0047` n `6`; index avg `0.0098` n `27`; metal avg `0.0007` n `20`; unknown avg `-0.0246` n `1262`
- 1h: commodity avg `0.3256` n `13`; crypto_alt avg `-0.2288` n `239`; crypto_major avg `-0.2977` n `8`; equity avg `-0.422` n `160`; fx avg `0.0124` n `6`; index avg `-0.0177` n `27`; metal avg `-0.0711` n `20`; unknown avg `19.2141` n `1256`
- 4h: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.6474` n `239`; crypto_major avg `-1.177` n `8`; equity avg `-0.2077` n `160`; fx avg `-0.0119` n `6`; index avg `-0.0232` n `27`; metal avg `-0.2101` n `20`; unknown avg `19.3714` n `1219`
- 24h: commodity avg `-0.1217` n `13`; crypto_alt avg `0.13` n `239`; crypto_major avg `-0.6838` n `8`; equity avg `3.6147` n `160`; fx avg `-0.0006` n `6`; index avg `0.4045` n `27`; metal avg `-0.0554` n `20`; unknown avg `5.1997` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2339`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal

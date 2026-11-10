# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T12:22:31.852642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0465` n `13`; crypto_alt avg `0.2322` n `239`; crypto_major avg `0.113` n `8`; equity avg `-0.047` n `160`; fx avg `0.0031` n `6`; index avg `0.0001` n `27`; metal avg `-0.0088` n `20`; unknown avg `0.0207` n `1262`
- 1h: commodity avg `-0.1101` n `13`; crypto_alt avg `0.3978` n `239`; crypto_major avg `0.2164` n `8`; equity avg `-0.1514` n `160`; fx avg `0.0026` n `6`; index avg `-0.0093` n `27`; metal avg `0.0225` n `20`; unknown avg `0.5079` n `1250`
- 4h: commodity avg `0.0256` n `13`; crypto_alt avg `-0.1426` n `239`; crypto_major avg `-0.6776` n `8`; equity avg `-0.6317` n `160`; fx avg `-0.0046` n `6`; index avg `-0.0511` n `27`; metal avg `-0.2042` n `20`; unknown avg `19.1007` n `1229`
- 24h: commodity avg `-0.2778` n `13`; crypto_alt avg `0.0644` n `239`; crypto_major avg `-0.5342` n `8`; equity avg `3.4165` n `160`; fx avg `-0.0012` n `6`; index avg `0.4024` n `27`; metal avg `-0.0839` n `20`; unknown avg `4.8591` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2362`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal

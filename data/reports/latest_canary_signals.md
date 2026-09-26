# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T18:07:27.820756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.0347` n `234`; crypto_major avg `0.0002` n `8`; equity avg `0.0095` n `141`; fx avg `-0.0034` n `6`; index avg `0.0011` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.2177` n `959`
- 1h: commodity avg `0.0289` n `12`; crypto_alt avg `-0.2281` n `234`; crypto_major avg `-0.1325` n `8`; equity avg `-0.0138` n `141`; fx avg `0.0036` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0016` n `20`; unknown avg `7.8144` n `959`
- 4h: commodity avg `-0.0265` n `12`; crypto_alt avg `0.6523` n `234`; crypto_major avg `0.1147` n `8`; equity avg `0.1022` n `141`; fx avg `-0.0099` n `6`; index avg `0.0087` n `26`; metal avg `0.0019` n `20`; unknown avg `11.1461` n `945`
- 24h: commodity avg `0.3241` n `12`; crypto_alt avg `2.5398` n `234`; crypto_major avg `-0.1031` n `8`; equity avg `-0.0322` n `141`; fx avg `0.0214` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0043` n `20`; unknown avg `3.607` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal

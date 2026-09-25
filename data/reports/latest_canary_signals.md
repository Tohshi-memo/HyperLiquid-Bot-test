# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T08:07:25.818831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.1913` n `234`; crypto_major avg `0.0772` n `8`; equity avg `-0.0393` n `141`; fx avg `-0.0037` n `6`; index avg `-0.015` n `26`; metal avg `0.0455` n `20`; unknown avg `0.1809` n `926`
- 1h: commodity avg `0.1122` n `12`; crypto_alt avg `0.4115` n `234`; crypto_major avg `0.1629` n `8`; equity avg `-0.0793` n `141`; fx avg `0.0038` n `6`; index avg `-0.0234` n `26`; metal avg `0.0083` n `20`; unknown avg `3.7574` n `926`
- 4h: commodity avg `0.0686` n `12`; crypto_alt avg `0.677` n `234`; crypto_major avg `0.058` n `8`; equity avg `0.3033` n `141`; fx avg `-0.0143` n `6`; index avg `0.0634` n `26`; metal avg `0.0723` n `20`; unknown avg `2.2631` n `904`
- 24h: commodity avg `0.2296` n `12`; crypto_alt avg `1.9041` n `234`; crypto_major avg `0.1439` n `8`; equity avg `1.0607` n `141`; fx avg `-0.1622` n `6`; index avg `0.1695` n `26`; metal avg `-0.1818` n `20`; unknown avg `13.8849` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal

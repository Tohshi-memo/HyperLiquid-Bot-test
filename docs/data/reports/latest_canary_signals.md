# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T03:22:26.113721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.0558` n `230`; crypto_major avg `-0.0575` n `8`; equity avg `-0.0183` n `102`; fx avg `-0.0184` n `6`; index avg `-0.0155` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.0066` n `781`
- 1h: commodity avg `0.0621` n `12`; crypto_alt avg `-0.0913` n `230`; crypto_major avg `-0.1809` n `8`; equity avg `-0.0369` n `102`; fx avg `-0.0092` n `6`; index avg `-0.0211` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0917` n `781`
- 4h: commodity avg `-0.1282` n `12`; crypto_alt avg `0.5587` n `230`; crypto_major avg `0.1125` n `8`; equity avg `0.0882` n `102`; fx avg `0.0086` n `6`; index avg `0.0287` n `25`; metal avg `-0.0277` n `20`; unknown avg `4.9752` n `781`
- 24h: commodity avg `0.9512` n `12`; crypto_alt avg `0.159` n `230`; crypto_major avg `-1.54` n `8`; equity avg `-2.158` n `102`; fx avg `-0.1454` n `6`; index avg `-0.2293` n `25`; metal avg `-0.1357` n `20`; unknown avg `4.9042` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T03:07:26.727007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.026` n `12`; crypto_alt avg `0.2272` n `228`; crypto_major avg `0.2345` n `8`; equity avg `0.1681` n `88`; fx avg `0.002` n `6`; index avg `0.0227` n `23`; metal avg `0.0731` n `20`; unknown avg `-0.0476` n `765`
- 1h: commodity avg `0.0592` n `12`; crypto_alt avg `0.8364` n `228`; crypto_major avg `0.8049` n `8`; equity avg `0.4863` n `88`; fx avg `-0.0121` n `6`; index avg `0.1083` n `23`; metal avg `0.1503` n `20`; unknown avg `0.7062` n `765`
- 4h: commodity avg `-0.0473` n `12`; crypto_alt avg `0.8072` n `228`; crypto_major avg `0.9574` n `8`; equity avg `-0.4991` n `88`; fx avg `0.0769` n `6`; index avg `-0.2054` n `23`; metal avg `-0.4365` n `20`; unknown avg `0.0736` n `765`
- 24h: commodity avg `0.0327` n `12`; crypto_alt avg `-0.9751` n `228`; crypto_major avg `-0.5156` n `8`; equity avg `0.6907` n `88`; fx avg `0.1617` n `6`; index avg `0.0296` n `23`; metal avg `-0.0034` n `20`; unknown avg `6.9172` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal

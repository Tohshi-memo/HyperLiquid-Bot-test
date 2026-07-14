# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T16:52:27.961077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `-0.0006` n `230`; crypto_major avg `-0.0807` n `8`; equity avg `0.0508` n `92`; fx avg `-0.0117` n `6`; index avg `0.0057` n `25`; metal avg `0.0223` n `20`; unknown avg `-0.0604` n `766`
- 1h: commodity avg `-0.1078` n `12`; crypto_alt avg `0.0142` n `230`; crypto_major avg `0.0111` n `8`; equity avg `0.1618` n `92`; fx avg `-0.018` n `6`; index avg `0.0363` n `25`; metal avg `-0.0305` n `20`; unknown avg `-0.0808` n `766`
- 4h: commodity avg `-0.2471` n `12`; crypto_alt avg `0.7192` n `230`; crypto_major avg `1.1078` n `8`; equity avg `-0.1196` n `92`; fx avg `-0.0262` n `6`; index avg `0.0963` n `25`; metal avg `0.0823` n `20`; unknown avg `-0.1991` n `758`
- 24h: commodity avg `0.6333` n `12`; crypto_alt avg `1.5789` n `230`; crypto_major avg `3.1346` n `8`; equity avg `0.9451` n `92`; fx avg `-0.0219` n `6`; index avg `0.3332` n `25`; metal avg `0.6555` n `20`; unknown avg `-0.0715` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal

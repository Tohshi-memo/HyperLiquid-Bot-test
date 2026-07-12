# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T22:22:26.956946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0539` n `12`; crypto_alt avg `-0.0946` n `230`; crypto_major avg `-0.1219` n `8`; equity avg `-0.1005` n `92`; fx avg `0.0187` n `6`; index avg `-0.0155` n `25`; metal avg `-0.0301` n `20`; unknown avg `0.0008` n `765`
- 1h: commodity avg `-0.1444` n `12`; crypto_alt avg `-0.7372` n `230`; crypto_major avg `-0.6775` n `8`; equity avg `-0.2892` n `92`; fx avg `-0.0125` n `6`; index avg `-0.0786` n `25`; metal avg `-0.1877` n `20`; unknown avg `0.2838` n `765`
- 4h: commodity avg `-0.1383` n `12`; crypto_alt avg `-0.8222` n `230`; crypto_major avg `-0.7611` n `8`; equity avg `-0.2384` n `92`; fx avg `-0.0464` n `6`; index avg `-0.1089` n `25`; metal avg `-0.1986` n `20`; unknown avg `0.1223` n `765`
- 24h: commodity avg `0.1045` n `12`; crypto_alt avg `-1.7099` n `230`; crypto_major avg `-1.1901` n `8`; equity avg `-0.4933` n `92`; fx avg `-0.0571` n `6`; index avg `-0.1837` n `25`; metal avg `-0.2838` n `20`; unknown avg `0.2732` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal

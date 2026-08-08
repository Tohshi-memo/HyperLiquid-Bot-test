# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T06:22:25.688918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.0227` n `230`; crypto_major avg `0.0242` n `8`; equity avg `-0.0261` n `112`; fx avg `-0.0033` n `6`; index avg `-0.0013` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.0193` n `784`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `0.0363` n `230`; crypto_major avg `0.0458` n `8`; equity avg `-0.0702` n `112`; fx avg `0.001` n `6`; index avg `-0.0113` n `25`; metal avg `0.0094` n `20`; unknown avg `-0.0213` n `752`
- 4h: commodity avg `0.0147` n `12`; crypto_alt avg `0.2814` n `230`; crypto_major avg `0.4055` n `8`; equity avg `-0.222` n `112`; fx avg `0.0024` n `6`; index avg `-0.0465` n `25`; metal avg `0.0151` n `20`; unknown avg `0.13` n `751`
- 24h: commodity avg `-0.2029` n `12`; crypto_alt avg `-0.2574` n `230`; crypto_major avg `0.5751` n `8`; equity avg `1.287` n `112`; fx avg `-0.0671` n `6`; index avg `0.1138` n `25`; metal avg `0.0726` n `20`; unknown avg `-0.0108` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T00:07:28.041514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0379` n `12`; crypto_alt avg `0.1697` n `228`; crypto_major avg `0.0172` n `8`; equity avg `0.0632` n `74`; fx avg `0.0262` n `6`; index avg `0.1123` n `23`; metal avg `0.0314` n `18`; unknown avg `-0.0907` n `643`
- 1h: commodity avg `-0.0378` n `12`; crypto_alt avg `0.2195` n `228`; crypto_major avg `-0.0681` n `8`; equity avg `0.0974` n `74`; fx avg `0.0369` n `6`; index avg `0.1127` n `23`; metal avg `0.0484` n `18`; unknown avg `-0.1636` n `643`
- 4h: commodity avg `-0.3733` n `12`; crypto_alt avg `-0.1189` n `228`; crypto_major avg `-0.5105` n `8`; equity avg `0.3203` n `74`; fx avg `0.0491` n `6`; index avg `0.2252` n `23`; metal avg `0.0996` n `18`; unknown avg `0.4245` n `643`
- 24h: commodity avg `-0.8648` n `12`; crypto_alt avg `-0.6246` n `228`; crypto_major avg `-0.4217` n `8`; equity avg `-0.7614` n `74`; fx avg `0.0001` n `6`; index avg `0.3524` n `23`; metal avg `0.2282` n `18`; unknown avg `41.9222` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal

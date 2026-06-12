# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T07:22:30.767048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.073` n `12`; crypto_alt avg `-0.1275` n `228`; crypto_major avg `-0.0495` n `8`; equity avg `-0.0498` n `74`; fx avg `-0.016` n `6`; index avg `-0.1197` n `23`; metal avg `-0.2637` n `18`; unknown avg `0.0069` n `557`
- 1h: commodity avg `-0.0908` n `12`; crypto_alt avg `-0.2213` n `228`; crypto_major avg `-0.3283` n `8`; equity avg `-0.5004` n `74`; fx avg `0.0042` n `6`; index avg `-0.3365` n `23`; metal avg `-0.4574` n `18`; unknown avg `13.1936` n `557`
- 4h: commodity avg `-0.3776` n `12`; crypto_alt avg `-0.8824` n `228`; crypto_major avg `-0.9752` n `8`; equity avg `-1.0584` n `74`; fx avg `0.0038` n `6`; index avg `-0.4585` n `23`; metal avg `-0.8577` n `18`; unknown avg `18.6694` n `535`
- 24h: commodity avg `-1.9467` n `12`; crypto_alt avg `0.6938` n `228`; crypto_major avg `0.8995` n `8`; equity avg `2.0362` n `74`; fx avg `-0.0544` n `6`; index avg `1.0786` n `23`; metal avg `1.8762` n `18`; unknown avg `1.4848` n `534`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal

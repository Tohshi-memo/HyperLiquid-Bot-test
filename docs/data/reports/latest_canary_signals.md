# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T14:22:30.988413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `0.1957` n `230`; crypto_major avg `0.1928` n `8`; equity avg `-0.0112` n `96`; fx avg `0.0098` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.0314` n `770`
- 1h: commodity avg `0.0018` n `12`; crypto_alt avg `0.2181` n `230`; crypto_major avg `0.3491` n `8`; equity avg `0.0343` n `96`; fx avg `0.0055` n `6`; index avg `-0.0162` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.0323` n `770`
- 4h: commodity avg `0.0095` n `12`; crypto_alt avg `-0.0589` n `230`; crypto_major avg `0.1214` n `8`; equity avg `-0.1213` n `96`; fx avg `-0.0009` n `6`; index avg `-0.0382` n `25`; metal avg `-0.0232` n `20`; unknown avg `-0.0308` n `769`
- 24h: commodity avg `0.4029` n `12`; crypto_alt avg `-0.557` n `230`; crypto_major avg `0.3893` n `8`; equity avg `-0.3667` n `96`; fx avg `0.0219` n `6`; index avg `0.0374` n `25`; metal avg `0.1581` n `20`; unknown avg `0.0229` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal

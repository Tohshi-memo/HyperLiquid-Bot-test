# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T07:37:26.507064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `12`; crypto_alt avg `0.0767` n `229`; crypto_major avg `-0.0` n `8`; equity avg `0.0569` n `88`; fx avg `-0.0029` n `6`; index avg `0.0013` n `25`; metal avg `0.1153` n `20`; unknown avg `0.8215` n `765`
- 1h: commodity avg `-0.0373` n `12`; crypto_alt avg `0.085` n `229`; crypto_major avg `0.0374` n `8`; equity avg `0.0682` n `88`; fx avg `-0.0208` n `6`; index avg `0.0099` n `25`; metal avg `0.1121` n `20`; unknown avg `0.9485` n `763`
- 4h: commodity avg `0.0452` n `12`; crypto_alt avg `0.3164` n `229`; crypto_major avg `0.5049` n `8`; equity avg `0.5352` n `88`; fx avg `-0.1751` n `6`; index avg `0.2016` n `25`; metal avg `0.0763` n `20`; unknown avg `0.6618` n `743`
- 24h: commodity avg `0.3912` n `12`; crypto_alt avg `2.5309` n `228`; crypto_major avg `3.7704` n `8`; equity avg `0.7131` n `88`; fx avg `-0.1738` n `6`; index avg `0.2775` n `25`; metal avg `1.3875` n `20`; unknown avg `6.5467` n `741`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal

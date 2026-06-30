# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T10:52:30.999573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `0.0738` n `228`; crypto_major avg `0.199` n `8`; equity avg `0.0938` n `88`; fx avg `-0.0029` n `6`; index avg `0.0154` n `23`; metal avg `0.05` n `20`; unknown avg `0.0145` n `765`
- 1h: commodity avg `-0.0342` n `12`; crypto_alt avg `-0.0217` n `228`; crypto_major avg `0.0146` n `8`; equity avg `0.0995` n `88`; fx avg `0.0178` n `6`; index avg `0.0108` n `23`; metal avg `0.1009` n `20`; unknown avg `0.0442` n `765`
- 4h: commodity avg `0.1859` n `12`; crypto_alt avg `-0.5423` n `228`; crypto_major avg `-0.2977` n `8`; equity avg `-0.0846` n `88`; fx avg `0.0228` n `6`; index avg `-0.0224` n `23`; metal avg `0.0616` n `20`; unknown avg `0.0142` n `765`
- 24h: commodity avg `0.1274` n `12`; crypto_alt avg `-0.807` n `228`; crypto_major avg `0.1141` n `8`; equity avg `1.2933` n `88`; fx avg `0.1386` n `6`; index avg `0.1151` n `23`; metal avg `0.3258` n `20`; unknown avg `9.0682` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal

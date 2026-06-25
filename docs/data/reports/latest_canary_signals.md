# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T21:52:24.966131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `-0.0733` n `228`; crypto_major avg `-0.0615` n `8`; equity avg `-0.0615` n `86`; fx avg `0.0118` n `6`; index avg `0.0116` n `23`; metal avg `-0.0041` n `20`; unknown avg `-0.1026` n `765`
- 1h: commodity avg `0.004` n `12`; crypto_alt avg `0.9665` n `228`; crypto_major avg `1.0668` n `8`; equity avg `-0.051` n `86`; fx avg `-0.0033` n `6`; index avg `0.0063` n `23`; metal avg `0.0555` n `20`; unknown avg `1.1106` n `765`
- 4h: commodity avg `-0.103` n `12`; crypto_alt avg `0.5743` n `228`; crypto_major avg `0.634` n `8`; equity avg `0.1977` n `86`; fx avg `0.0044` n `6`; index avg `0.0172` n `23`; metal avg `-0.0556` n `20`; unknown avg `1.1362` n `765`
- 24h: commodity avg `0.3696` n `12`; crypto_alt avg `-1.0161` n `228`; crypto_major avg `-1.0621` n `8`; equity avg `-2.1319` n `86`; fx avg `0.1287` n `6`; index avg `-0.1606` n `23`; metal avg `0.3026` n `20`; unknown avg `1.1207` n `700`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal

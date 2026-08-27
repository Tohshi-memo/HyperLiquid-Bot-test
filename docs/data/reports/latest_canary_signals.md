# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T11:37:25.223911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.2383` n `231`; crypto_major avg `-0.3894` n `8`; equity avg `-0.1391` n `127`; fx avg `-0.012` n `6`; index avg `-0.0221` n `26`; metal avg `0.0192` n `20`; unknown avg `0.0427` n `792`
- 1h: commodity avg `-0.0248` n `12`; crypto_alt avg `0.3223` n `231`; crypto_major avg `0.072` n `8`; equity avg `-0.0868` n `127`; fx avg `-0.0235` n `6`; index avg `0.0039` n `26`; metal avg `0.1108` n `20`; unknown avg `0.0027` n `792`
- 4h: commodity avg `0.2493` n `12`; crypto_alt avg `0.5168` n `231`; crypto_major avg `0.8442` n `8`; equity avg `0.2335` n `127`; fx avg `-0.0266` n `6`; index avg `0.0335` n `26`; metal avg `0.0172` n `20`; unknown avg `0.0602` n `791`
- 24h: commodity avg `0.4315` n `12`; crypto_alt avg `1.2015` n `231`; crypto_major avg `1.6985` n `8`; equity avg `1.775` n `127`; fx avg `-0.1102` n `6`; index avg `0.2777` n `26`; metal avg `-0.3122` n `20`; unknown avg `0.4814` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal

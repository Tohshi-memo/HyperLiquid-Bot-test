# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T23:07:32.580910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `0.0318` n `229`; crypto_major avg `0.0102` n `8`; equity avg `0.0198` n `91`; fx avg `0.002` n `6`; index avg `0.0078` n `25`; metal avg `-0.0143` n `20`; unknown avg `-0.0228` n `763`
- 1h: commodity avg `0.0075` n `12`; crypto_alt avg `-0.1513` n `229`; crypto_major avg `-0.1752` n `8`; equity avg `-0.1867` n `91`; fx avg `0.0194` n `6`; index avg `-0.0498` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.0497` n `763`
- 4h: commodity avg `0.0217` n `12`; crypto_alt avg `0.4374` n `229`; crypto_major avg `0.4393` n `8`; equity avg `-0.0403` n `91`; fx avg `0.0225` n `6`; index avg `-0.0407` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.3166` n `763`
- 24h: commodity avg `0.1951` n `12`; crypto_alt avg `0.4598` n `229`; crypto_major avg `-0.1121` n `8`; equity avg `-1.022` n `90`; fx avg `0.145` n `6`; index avg `-0.0274` n `25`; metal avg `-0.3659` n `20`; unknown avg `-0.4507` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal

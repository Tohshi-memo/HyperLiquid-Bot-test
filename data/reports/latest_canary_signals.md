# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T21:52:29.637494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `-0.212` n `233`; crypto_major avg `-0.138` n `8`; equity avg `0.0025` n `134`; fx avg `-0.0085` n `6`; index avg `0.0094` n `26`; metal avg `-0.0078` n `20`; unknown avg `-0.0635` n `789`
- 1h: commodity avg `0.0073` n `12`; crypto_alt avg `-0.2669` n `233`; crypto_major avg `-0.1496` n `8`; equity avg `0.0284` n `134`; fx avg `-0.0156` n `6`; index avg `0.0073` n `26`; metal avg `0.0497` n `20`; unknown avg `3.4645` n `771`
- 4h: commodity avg `0.4009` n `12`; crypto_alt avg `-0.9729` n `233`; crypto_major avg `-0.4828` n `8`; equity avg `-0.56` n `134`; fx avg `-0.0733` n `6`; index avg `-0.1044` n `26`; metal avg `-0.2128` n `20`; unknown avg `0.586` n `749`
- 24h: commodity avg `0.1172` n `12`; crypto_alt avg `-0.7202` n `232`; crypto_major avg `-0.1744` n `8`; equity avg `0.2891` n `134`; fx avg `-0.1228` n `6`; index avg `-0.1715` n `26`; metal avg `-0.2914` n `20`; unknown avg `5.8327` n `704`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal

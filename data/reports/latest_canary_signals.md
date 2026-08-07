# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T23:07:28.636000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0244` n `12`; crypto_alt avg `0.0557` n `230`; crypto_major avg `0.0346` n `8`; equity avg `-0.0709` n `112`; fx avg `-0.0002` n `6`; index avg `-0.0029` n `25`; metal avg `0.0118` n `20`; unknown avg `-0.0729` n `782`
- 1h: commodity avg `-0.0021` n `12`; crypto_alt avg `0.0267` n `230`; crypto_major avg `-0.0269` n `8`; equity avg `-0.0296` n `112`; fx avg `-0.0033` n `6`; index avg `0.0027` n `25`; metal avg `0.0427` n `20`; unknown avg `0.0519` n `782`
- 4h: commodity avg `-0.125` n `12`; crypto_alt avg `-0.3353` n `230`; crypto_major avg `0.0144` n `8`; equity avg `0.143` n `112`; fx avg `0.0264` n `6`; index avg `-0.0102` n `25`; metal avg `0.0332` n `20`; unknown avg `-0.1509` n `782`
- 24h: commodity avg `-0.1936` n `12`; crypto_alt avg `-0.4088` n `230`; crypto_major avg `-0.1628` n `8`; equity avg `1.6425` n `112`; fx avg `-0.1113` n `6`; index avg `0.082` n `25`; metal avg `0.4888` n `20`; unknown avg `0.079` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal

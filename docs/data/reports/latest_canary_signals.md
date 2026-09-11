# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T12:22:29.450544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0813` n `12`; crypto_alt avg `-0.057` n `233`; crypto_major avg `0.0298` n `8`; equity avg `0.0751` n `136`; fx avg `-0.0101` n `6`; index avg `0.0276` n `26`; metal avg `0.0284` n `20`; unknown avg `-0.0391` n `796`
- 1h: commodity avg `-0.0049` n `12`; crypto_alt avg `0.2316` n `233`; crypto_major avg `0.2192` n `8`; equity avg `0.0965` n `136`; fx avg `0.0085` n `6`; index avg `0.042` n `26`; metal avg `-0.0069` n `20`; unknown avg `-0.0122` n `794`
- 4h: commodity avg `-0.2877` n `12`; crypto_alt avg `-1.2475` n `233`; crypto_major avg `-0.6569` n `8`; equity avg `0.1155` n `136`; fx avg `-0.0789` n `6`; index avg `0.0687` n `26`; metal avg `-0.0427` n `20`; unknown avg `-0.2682` n `788`
- 24h: commodity avg `-0.0619` n `12`; crypto_alt avg `-1.9099` n `233`; crypto_major avg `-1.6346` n `8`; equity avg `-0.3656` n `136`; fx avg `-0.1068` n `6`; index avg `0.0307` n `26`; metal avg `-0.2771` n `20`; unknown avg `1.3618` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal

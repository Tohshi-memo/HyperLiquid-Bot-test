# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T06:52:31.844771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `12`; crypto_alt avg `0.0791` n `228`; crypto_major avg `0.0078` n `8`; equity avg `0.045` n `88`; fx avg `0.0016` n `6`; index avg `0.0124` n `23`; metal avg `0.0107` n `20`; unknown avg `-0.2015` n `764`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `-0.0555` n `228`; crypto_major avg `-0.0229` n `8`; equity avg `0.1407` n `88`; fx avg `0.0036` n `6`; index avg `0.0244` n `23`; metal avg `0.022` n `20`; unknown avg `-0.3541` n `748`
- 4h: commodity avg `0.0603` n `12`; crypto_alt avg `-0.4825` n `228`; crypto_major avg `-0.3973` n `8`; equity avg `0.1283` n `88`; fx avg `0.0023` n `6`; index avg `0.0073` n `23`; metal avg `0.0111` n `20`; unknown avg `-0.8131` n `732`
- 24h: commodity avg `-0.1577` n `12`; crypto_alt avg `1.3396` n `228`; crypto_major avg `0.9656` n `8`; equity avg `1.4254` n `87`; fx avg `0.0577` n `6`; index avg `0.0278` n `23`; metal avg `0.7038` n `20`; unknown avg `-0.5461` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2036`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal

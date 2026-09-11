# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T05:07:24.766415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0537` n `12`; crypto_alt avg `-0.0363` n `233`; crypto_major avg `-0.0156` n `8`; equity avg `-0.0432` n `136`; fx avg `0.0141` n `6`; index avg `-0.0176` n `26`; metal avg `0.0104` n `20`; unknown avg `-0.3401` n `794`
- 1h: commodity avg `-0.1847` n `12`; crypto_alt avg `0.3829` n `233`; crypto_major avg `0.352` n `8`; equity avg `0.2829` n `136`; fx avg `0.0138` n `6`; index avg `0.067` n `26`; metal avg `0.1471` n `20`; unknown avg `17.8078` n `788`
- 4h: commodity avg `-0.0938` n `12`; crypto_alt avg `0.3242` n `233`; crypto_major avg `0.23` n `8`; equity avg `-0.2266` n `136`; fx avg `-0.0271` n `6`; index avg `0.0169` n `26`; metal avg `0.0135` n `20`; unknown avg `-0.189` n `780`
- 24h: commodity avg `0.9803` n `12`; crypto_alt avg `-1.2541` n `233`; crypto_major avg `-1.807` n `8`; equity avg `-1.94` n `136`; fx avg `0.0871` n `6`; index avg `-0.315` n `26`; metal avg `-1.2013` n `20`; unknown avg `-0.3497` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal

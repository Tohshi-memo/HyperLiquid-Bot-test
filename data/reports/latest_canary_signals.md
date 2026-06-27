# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T07:07:30.211419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.1012` n `228`; crypto_major avg `-0.0144` n `8`; equity avg `0.0272` n `88`; fx avg `0.0024` n `6`; index avg `-0.0014` n `23`; metal avg `-0.0048` n `20`; unknown avg `0.8524` n `764`
- 1h: commodity avg `0.0288` n `12`; crypto_alt avg `-0.0186` n `228`; crypto_major avg `0.1668` n `8`; equity avg `0.2109` n `88`; fx avg `0.0017` n `6`; index avg `0.0287` n `23`; metal avg `0.0161` n `20`; unknown avg `-0.1925` n `764`
- 4h: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.252` n `228`; crypto_major avg `-0.02` n `8`; equity avg `0.1527` n `88`; fx avg `0.0044` n `6`; index avg `0.0085` n `23`; metal avg `0.0002` n `20`; unknown avg `-0.1689` n `732`
- 24h: commodity avg `-0.169` n `12`; crypto_alt avg `0.9223` n `228`; crypto_major avg `0.4995` n `8`; equity avg `1.4859` n `87`; fx avg `0.0636` n `6`; index avg `0.0288` n `23`; metal avg `0.684` n `20`; unknown avg `-0.5594` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal

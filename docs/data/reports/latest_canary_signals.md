# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T21:37:31.243105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.0585` n `230`; crypto_major avg `-0.028` n `8`; equity avg `0.0039` n `114`; fx avg `-0.0072` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0146` n `20`; unknown avg `-0.0815` n `791`
- 1h: commodity avg `-0.0282` n `12`; crypto_alt avg `-0.4307` n `230`; crypto_major avg `-0.1683` n `8`; equity avg `0.0194` n `114`; fx avg `-0.0003` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0159` n `20`; unknown avg `0.2828` n `791`
- 4h: commodity avg `0.0333` n `12`; crypto_alt avg `-0.5469` n `230`; crypto_major avg `-0.3463` n `8`; equity avg `0.0405` n `114`; fx avg `0.0133` n `6`; index avg `0.0006` n `25`; metal avg `-0.0424` n `20`; unknown avg `0.1188` n `791`
- 24h: commodity avg `0.0565` n `12`; crypto_alt avg `-0.7493` n `230`; crypto_major avg `-0.2985` n `8`; equity avg `0.2876` n `114`; fx avg `-0.0051` n `6`; index avg `0.0361` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0039` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2199`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal

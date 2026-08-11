# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T21:52:25.254083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `0.0191` n `230`; crypto_major avg `0.066` n `8`; equity avg `0.0121` n `113`; fx avg `-0.0027` n `6`; index avg `-0.0214` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.0829` n `786`
- 1h: commodity avg `-0.0054` n `12`; crypto_alt avg `0.1156` n `230`; crypto_major avg `0.2583` n `8`; equity avg `0.0468` n `113`; fx avg `0.0028` n `6`; index avg `-0.0031` n `25`; metal avg `0.0004` n `20`; unknown avg `0.0097` n `785`
- 4h: commodity avg `-0.0771` n `12`; crypto_alt avg `0.4886` n `230`; crypto_major avg `0.7905` n `8`; equity avg `0.6142` n `113`; fx avg `0.0011` n `6`; index avg `0.0204` n `25`; metal avg `-0.0281` n `20`; unknown avg `0.5929` n `785`
- 24h: commodity avg `0.0747` n `12`; crypto_alt avg `-1.0821` n `230`; crypto_major avg `0.5849` n `8`; equity avg `1.1992` n `113`; fx avg `-0.0655` n `6`; index avg `0.1048` n `25`; metal avg `-0.2535` n `20`; unknown avg `-0.2071` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.22`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T07:07:26.605140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `-0.1377` n `230`; crypto_major avg `-0.1206` n `8`; equity avg `-0.0239` n `96`; fx avg `0.0043` n `6`; index avg `-0.0124` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.0077` n `769`
- 1h: commodity avg `0.0754` n `12`; crypto_alt avg `-0.0549` n `230`; crypto_major avg `0.0085` n `8`; equity avg `-0.0888` n `96`; fx avg `0.0008` n `6`; index avg `-0.0413` n `25`; metal avg `-0.0119` n `20`; unknown avg `-0.1395` n `769`
- 4h: commodity avg `0.0003` n `12`; crypto_alt avg `-0.5079` n `230`; crypto_major avg `-0.3292` n `8`; equity avg `-0.2133` n `96`; fx avg `0.0013` n `6`; index avg `-0.0067` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.0992` n `737`
- 24h: commodity avg `0.8659` n `12`; crypto_alt avg `-0.3831` n `230`; crypto_major avg `0.2977` n `8`; equity avg `1.1754` n `96`; fx avg `0.0478` n `6`; index avg `0.1521` n `25`; metal avg `0.2415` n `20`; unknown avg `0.2449` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal

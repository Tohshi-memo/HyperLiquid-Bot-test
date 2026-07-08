# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T20:37:28.203309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0652` n `12`; crypto_alt avg `-0.1402` n `229`; crypto_major avg `-0.1698` n `8`; equity avg `-0.1171` n `91`; fx avg `-0.0246` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0771` n `20`; unknown avg `-0.0632` n `764`
- 1h: commodity avg `0.2404` n `12`; crypto_alt avg `-0.1579` n `229`; crypto_major avg `-0.1554` n `8`; equity avg `-0.0761` n `91`; fx avg `-0.0063` n `6`; index avg `-0.0385` n `25`; metal avg `-0.1979` n `20`; unknown avg `-0.1247` n `764`
- 4h: commodity avg `-0.0661` n `12`; crypto_alt avg `0.3554` n `229`; crypto_major avg `0.3751` n `8`; equity avg `0.9422` n `91`; fx avg `-0.0457` n `6`; index avg `0.1332` n `25`; metal avg `0.2717` n `20`; unknown avg `1.3886` n `764`
- 24h: commodity avg `0.5088` n `12`; crypto_alt avg `-2.3345` n `229`; crypto_major avg `-2.8453` n `8`; equity avg `0.7617` n `91`; fx avg `-0.0146` n `6`; index avg `-0.0771` n `25`; metal avg `-0.841` n `20`; unknown avg `0.0398` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal

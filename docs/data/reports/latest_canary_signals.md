# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T17:01:51.917223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `0.0402` n `229`; crypto_major avg `0.1024` n `8`; equity avg `0.0249` n `88`; fx avg `0.0031` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.0235` n `765`
- 1h: commodity avg `0.0246` n `12`; crypto_alt avg `0.0904` n `229`; crypto_major avg `0.0387` n `8`; equity avg `0.0023` n `88`; fx avg `-0.0074` n `6`; index avg `0.0414` n `25`; metal avg `0.065` n `20`; unknown avg `-0.1407` n `765`
- 4h: commodity avg `0.0519` n `12`; crypto_alt avg `0.2518` n `229`; crypto_major avg `0.24` n `8`; equity avg `0.0498` n `88`; fx avg `-0.0349` n `6`; index avg `0.0086` n `25`; metal avg `0.0097` n `20`; unknown avg `0.9736` n `765`
- 24h: commodity avg `0.2932` n `12`; crypto_alt avg `2.4937` n `229`; crypto_major avg `1.9576` n `8`; equity avg `2.1303` n `88`; fx avg `-0.0327` n `6`; index avg `0.5997` n `25`; metal avg `0.5846` n `20`; unknown avg `8.422` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0481`, n `668`, weak_sample_signal

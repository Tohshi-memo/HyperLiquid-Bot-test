# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T06:07:26.765253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.1598` n `229`; crypto_major avg `0.1604` n `8`; equity avg `0.1964` n `88`; fx avg `-0.0892` n `6`; index avg `0.0591` n `25`; metal avg `0.0037` n `20`; unknown avg `0.14` n `745`
- 1h: commodity avg `0.0555` n `12`; crypto_alt avg `0.4312` n `229`; crypto_major avg `0.649` n `8`; equity avg `0.1782` n `88`; fx avg `-0.0854` n `6`; index avg `0.0422` n `25`; metal avg `-0.0479` n `20`; unknown avg `0.451` n `745`
- 4h: commodity avg `0.1418` n `12`; crypto_alt avg `0.2033` n `229`; crypto_major avg `0.4678` n `8`; equity avg `0.4934` n `88`; fx avg `-0.0228` n `6`; index avg `0.1494` n `25`; metal avg `-0.0333` n `20`; unknown avg `0.0732` n `745`
- 24h: commodity avg `0.4755` n `12`; crypto_alt avg `2.4964` n `228`; crypto_major avg `3.6944` n `8`; equity avg `0.2596` n `88`; fx avg `-0.1021` n `6`; index avg `0.2129` n `25`; metal avg `1.1457` n `20`; unknown avg `6.4509` n `743`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal

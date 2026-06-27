# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T05:44:05.702638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `0.0287` n `228`; crypto_major avg `-0.1422` n `8`; equity avg `-0.0245` n `88`; fx avg `-0.0029` n `6`; index avg `0.0017` n `23`; metal avg `-0.0018` n `20`; unknown avg `-0.3768` n `764`
- 1h: commodity avg `0.0011` n `12`; crypto_alt avg `-0.3227` n `228`; crypto_major avg `-0.3361` n `8`; equity avg `-0.0473` n `88`; fx avg `0.0053` n `6`; index avg `-0.0101` n `23`; metal avg `-0.0189` n `20`; unknown avg `-0.0376` n `764`
- 4h: commodity avg `-0.0391` n `12`; crypto_alt avg `0.0661` n `228`; crypto_major avg `0.2445` n `8`; equity avg `0.0548` n `88`; fx avg `0.0046` n `6`; index avg `0.0049` n `23`; metal avg `-0.008` n `20`; unknown avg `-1.4147` n `764`
- 24h: commodity avg `-0.1635` n `12`; crypto_alt avg `1.8058` n `228`; crypto_major avg `1.528` n `8`; equity avg `1.5499` n `87`; fx avg `0.0068` n `6`; index avg `0.0489` n `23`; metal avg `1.0786` n `20`; unknown avg `-0.5336` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal

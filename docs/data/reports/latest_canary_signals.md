# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T19:37:23.863068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.0175` n `230`; crypto_major avg `-0.0333` n `8`; equity avg `-0.0181` n `96`; fx avg `0.0041` n `6`; index avg `0.0034` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0211` n `770`
- 1h: commodity avg `0.0537` n `12`; crypto_alt avg `-0.0255` n `230`; crypto_major avg `0.0876` n `8`; equity avg `-0.0088` n `96`; fx avg `0.0185` n `6`; index avg `0.0093` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.1594` n `770`
- 4h: commodity avg `0.2482` n `12`; crypto_alt avg `0.2782` n `230`; crypto_major avg `0.4668` n `8`; equity avg `-0.0039` n `96`; fx avg `-0.0684` n `6`; index avg `-0.0283` n `25`; metal avg `-0.0235` n `20`; unknown avg `0.0025` n `770`
- 24h: commodity avg `0.5347` n `12`; crypto_alt avg `-0.5732` n `230`; crypto_major avg `0.2306` n `8`; equity avg `-0.6834` n `96`; fx avg `-0.148` n `6`; index avg `-0.0422` n `25`; metal avg `0.003` n `20`; unknown avg `-0.0417` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal

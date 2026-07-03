# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T11:52:26.938421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `12`; crypto_alt avg `0.143` n `229`; crypto_major avg `0.2067` n `8`; equity avg `-0.0178` n `88`; fx avg `-0.0023` n `6`; index avg `-0.0013` n `25`; metal avg `-0.0138` n `20`; unknown avg `-0.104` n `765`
- 1h: commodity avg `-0.0406` n `12`; crypto_alt avg `0.1508` n `229`; crypto_major avg `0.0866` n `8`; equity avg `-0.0518` n `88`; fx avg `0.0053` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0089` n `20`; unknown avg `0.3348` n `765`
- 4h: commodity avg `-0.0639` n `12`; crypto_alt avg `0.9932` n `229`; crypto_major avg `0.9078` n `8`; equity avg `0.2557` n `88`; fx avg `0.0738` n `6`; index avg `0.0233` n `25`; metal avg `-0.1015` n `20`; unknown avg `0.953` n `755`
- 24h: commodity avg `0.5148` n `12`; crypto_alt avg `2.1123` n `229`; crypto_major avg `2.3523` n `8`; equity avg `0.0253` n `88`; fx avg `-0.0555` n `6`; index avg `0.1832` n `25`; metal avg `1.168` n `20`; unknown avg `6.1987` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal

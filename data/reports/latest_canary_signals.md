# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T12:52:31.746136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0813` n `13`; crypto_alt avg `0.1015` n `237`; crypto_major avg `0.1422` n `8`; equity avg `0.2522` n `151`; fx avg `0.0093` n `6`; index avg `0.0618` n `26`; metal avg `0.0784` n `20`; unknown avg `0.6844` n `1198`
- 1h: commodity avg `-0.2546` n `13`; crypto_alt avg `0.5148` n `237`; crypto_major avg `0.4444` n `8`; equity avg `0.3308` n `151`; fx avg `0.0213` n `6`; index avg `0.0704` n `26`; metal avg `0.0218` n `20`; unknown avg `1.0438` n `1190`
- 4h: commodity avg `-0.1531` n `13`; crypto_alt avg `0.4715` n `237`; crypto_major avg `0.4463` n `8`; equity avg `-0.3468` n `151`; fx avg `0.0113` n `6`; index avg `-0.0209` n `26`; metal avg `-0.0929` n `20`; unknown avg `2.2659` n `1188`
- 24h: commodity avg `0.084` n `13`; crypto_alt avg `0.1731` n `237`; crypto_major avg `-0.558` n `8`; equity avg `-2.2971` n `151`; fx avg `-0.0046` n `6`; index avg `-0.274` n `26`; metal avg `-0.2208` n `20`; unknown avg `1.0443` n `1057`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal

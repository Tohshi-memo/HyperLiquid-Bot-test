# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T06:37:33.459061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `-0.046` n `229`; crypto_major avg `-0.0526` n `8`; equity avg `0.0682` n `91`; fx avg `0.0307` n `6`; index avg `0.0132` n `25`; metal avg `-0.0519` n `20`; unknown avg `-0.0149` n `765`
- 1h: commodity avg `-0.0817` n `12`; crypto_alt avg `-0.2449` n `229`; crypto_major avg `-0.2551` n `8`; equity avg `-0.2978` n `91`; fx avg `-0.074` n `6`; index avg `-0.0841` n `25`; metal avg `0.0404` n `20`; unknown avg `-0.041` n `733`
- 4h: commodity avg `-0.0798` n `12`; crypto_alt avg `-0.1517` n `229`; crypto_major avg `0.0106` n `8`; equity avg `-0.528` n `91`; fx avg `-0.0747` n `6`; index avg `-0.0934` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0036` n `733`
- 24h: commodity avg `-0.9076` n `12`; crypto_alt avg `0.4324` n `229`; crypto_major avg `0.6633` n `8`; equity avg `0.6008` n `91`; fx avg `-0.1136` n `6`; index avg `0.2082` n `25`; metal avg `0.3792` n `20`; unknown avg `-0.0394` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T14:07:30.950912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0727` n `12`; crypto_alt avg `0.4836` n `228`; crypto_major avg `0.5285` n `8`; equity avg `0.1212` n `88`; fx avg `0.0027` n `6`; index avg `0.0325` n `23`; metal avg `0.0269` n `20`; unknown avg `-0.0558` n `765`
- 1h: commodity avg `-0.0854` n `12`; crypto_alt avg `1.0629` n `228`; crypto_major avg `1.0057` n `8`; equity avg `0.6973` n `88`; fx avg `0.0098` n `6`; index avg `0.1584` n `23`; metal avg `0.0747` n `20`; unknown avg `0.3248` n `765`
- 4h: commodity avg `0.1473` n `12`; crypto_alt avg `-0.4256` n `228`; crypto_major avg `-0.4493` n `8`; equity avg `0.194` n `88`; fx avg `-0.0015` n `6`; index avg `0.1752` n `23`; metal avg `-0.0445` n `20`; unknown avg `0.0407` n `765`
- 24h: commodity avg `0.421` n `12`; crypto_alt avg `-0.7441` n `228`; crypto_major avg `0.2345` n `8`; equity avg `3.0014` n `88`; fx avg `0.0703` n `6`; index avg `0.5163` n `23`; metal avg `0.3663` n `20`; unknown avg `8.7861` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal

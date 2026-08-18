# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T13:22:27.636398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0567` n `12`; crypto_alt avg `-0.0267` n `230`; crypto_major avg `-0.0051` n `8`; equity avg `-0.0066` n `114`; fx avg `-0.0004` n `6`; index avg `-0.0025` n `25`; metal avg `-0.0451` n `20`; unknown avg `-0.0483` n `795`
- 1h: commodity avg `0.0462` n `12`; crypto_alt avg `-0.032` n `230`; crypto_major avg `-0.2558` n `8`; equity avg `-0.3248` n `114`; fx avg `0.003` n `6`; index avg `-0.0406` n `25`; metal avg `-0.1426` n `20`; unknown avg `-0.0037` n `795`
- 4h: commodity avg `0.1333` n `12`; crypto_alt avg `0.1726` n `230`; crypto_major avg `-0.0161` n `8`; equity avg `-0.1614` n `114`; fx avg `-0.0086` n `6`; index avg `0.0147` n `25`; metal avg `-0.0256` n `20`; unknown avg `0.003` n `795`
- 24h: commodity avg `0.5914` n `12`; crypto_alt avg `-0.5728` n `230`; crypto_major avg `0.2242` n `8`; equity avg `-2.469` n `114`; fx avg `-0.0634` n `6`; index avg `-0.5037` n `25`; metal avg `-0.1881` n `20`; unknown avg `-0.0611` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T21:22:38.813989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `12`; crypto_alt avg `-0.1018` n `230`; crypto_major avg `-0.1047` n `8`; equity avg `-0.0042` n `112`; fx avg `0.0026` n `6`; index avg `-0.0052` n `25`; metal avg `0.0013` n `20`; unknown avg `-0.0158` n `782`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.058` n `230`; crypto_major avg `-0.1925` n `8`; equity avg `0.0463` n `112`; fx avg `0.0253` n `6`; index avg `0.0123` n `25`; metal avg `0.0752` n `20`; unknown avg `0.2045` n `782`
- 4h: commodity avg `-0.2464` n `12`; crypto_alt avg `-0.0344` n `230`; crypto_major avg `0.3007` n `8`; equity avg `0.2896` n `112`; fx avg `0.0218` n `6`; index avg `0.0492` n `25`; metal avg `0.1078` n `20`; unknown avg `-0.0921` n `782`
- 24h: commodity avg `-0.0451` n `12`; crypto_alt avg `-0.1909` n `230`; crypto_major avg `-0.1295` n `8`; equity avg `2.1155` n `112`; fx avg `-0.1327` n `6`; index avg `0.1164` n `25`; metal avg `0.4032` n `20`; unknown avg `-0.0225` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal

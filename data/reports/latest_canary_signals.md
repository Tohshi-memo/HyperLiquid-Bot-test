# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T14:01:09.556473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0605` n `12`; crypto_alt avg `0.1131` n `229`; crypto_major avg `-0.0306` n `8`; equity avg `0.0891` n `91`; fx avg `0.0096` n `6`; index avg `0.0091` n `25`; metal avg `0.0502` n `20`; unknown avg `0.1042` n `765`
- 1h: commodity avg `-0.5343` n `12`; crypto_alt avg `0.3517` n `229`; crypto_major avg `0.4815` n `8`; equity avg `0.7577` n `91`; fx avg `0.0002` n `6`; index avg `0.1487` n `25`; metal avg `0.2754` n `20`; unknown avg `0.2509` n `765`
- 4h: commodity avg `-0.4241` n `12`; crypto_alt avg `0.1964` n `229`; crypto_major avg `-0.0695` n `8`; equity avg `1.1685` n `91`; fx avg `-0.02` n `6`; index avg `0.3123` n `25`; metal avg `0.4081` n `20`; unknown avg `0.2273` n `764`
- 24h: commodity avg `-0.7409` n `12`; crypto_alt avg `1.4979` n `229`; crypto_major avg `0.9599` n `8`; equity avg `2.6054` n `91`; fx avg `0.0934` n `6`; index avg `0.4892` n `25`; metal avg `0.976` n `20`; unknown avg `0.98` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal

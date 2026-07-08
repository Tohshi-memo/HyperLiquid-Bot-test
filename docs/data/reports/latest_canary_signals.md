# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T20:07:26.093910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0817` n `12`; crypto_alt avg `0.1965` n `229`; crypto_major avg `0.2064` n `8`; equity avg `0.1523` n `91`; fx avg `-0.0032` n `6`; index avg `0.0103` n `25`; metal avg `-0.0151` n `20`; unknown avg `0.062` n `764`
- 1h: commodity avg `0.1553` n `12`; crypto_alt avg `0.1166` n `229`; crypto_major avg `0.3083` n `8`; equity avg `0.3846` n `91`; fx avg `0.0007` n `6`; index avg `0.0359` n `25`; metal avg `-0.0812` n `20`; unknown avg `1.2195` n `764`
- 4h: commodity avg `-0.3116` n `12`; crypto_alt avg `0.5857` n `229`; crypto_major avg `0.6432` n `8`; equity avg `1.4417` n `91`; fx avg `-0.0197` n `6`; index avg `0.2925` n `25`; metal avg `0.412` n `20`; unknown avg `1.3491` n `764`
- 24h: commodity avg `0.4812` n `12`; crypto_alt avg `-2.2018` n `229`; crypto_major avg `-2.6611` n `8`; equity avg `1.0066` n `91`; fx avg `0.0018` n `6`; index avg `-0.0387` n `25`; metal avg `-0.8436` n `20`; unknown avg `0.06` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal

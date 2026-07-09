# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T16:52:30.098257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.178` n `229`; crypto_major avg `-0.2141` n `8`; equity avg `0.1006` n `91`; fx avg `0.0064` n `6`; index avg `0.0158` n `25`; metal avg `-0.0238` n `20`; unknown avg `-0.0256` n `765`
- 1h: commodity avg `-0.0795` n `12`; crypto_alt avg `-0.2521` n `229`; crypto_major avg `-0.3159` n `8`; equity avg `-0.2004` n `91`; fx avg `0.0035` n `6`; index avg `-0.0114` n `25`; metal avg `-0.0325` n `20`; unknown avg `-0.1354` n `765`
- 4h: commodity avg `-0.9496` n `12`; crypto_alt avg `-0.3354` n `229`; crypto_major avg `-0.1074` n `8`; equity avg `0.5322` n `91`; fx avg `-0.0125` n `6`; index avg `0.1318` n `25`; metal avg `0.2788` n `20`; unknown avg `-0.0569` n `765`
- 24h: commodity avg `-1.1554` n `12`; crypto_alt avg `0.8202` n `229`; crypto_major avg `0.3007` n `8`; equity avg `2.6189` n `91`; fx avg `0.0615` n `6`; index avg `0.4042` n `25`; metal avg `1.0926` n `20`; unknown avg `1.0388` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal

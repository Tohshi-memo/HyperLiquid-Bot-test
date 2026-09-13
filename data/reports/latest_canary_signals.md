# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T07:52:25.372557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.0207` n `233`; crypto_major avg `0.0296` n `8`; equity avg `-0.0384` n `136`; fx avg `0.0021` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0016` n `20`; unknown avg `1.137` n `838`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.17` n `233`; crypto_major avg `-0.1677` n `8`; equity avg `-0.1485` n `136`; fx avg `0.0022` n `6`; index avg `-0.0181` n `26`; metal avg `-0.0109` n `20`; unknown avg `-0.0595` n `836`
- 4h: commodity avg `0.0691` n `12`; crypto_alt avg `-0.1621` n `233`; crypto_major avg `-0.3689` n `8`; equity avg `-0.5047` n `136`; fx avg `-0.005` n `6`; index avg `-0.0835` n `26`; metal avg `-0.0044` n `20`; unknown avg `24.559` n `804`
- 24h: commodity avg `0.1532` n `12`; crypto_alt avg `0.1817` n `233`; crypto_major avg `-0.5625` n `8`; equity avg `-0.9213` n `136`; fx avg `-0.0111` n `6`; index avg `-0.1477` n `26`; metal avg `0.0219` n `20`; unknown avg `0.119` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal

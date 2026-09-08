# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T17:52:36.872652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.648` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.032` n `12`; crypto_alt avg `-0.0927` n `233`; crypto_major avg `-0.0062` n `8`; equity avg `-0.051` n `134`; fx avg `-0.0005` n `6`; index avg `-0.006` n `26`; metal avg `-0.0248` n `20`; unknown avg `0.3798` n `797`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.4025` n `233`; crypto_major avg `-0.2275` n `8`; equity avg `0.0523` n `134`; fx avg `0.0089` n `6`; index avg `0.0316` n `26`; metal avg `0.0111` n `20`; unknown avg `0.4293` n `795`
- 4h: commodity avg `-0.2561` n `12`; crypto_alt avg `1.5633` n `232`; crypto_major avg `1.6482` n `8`; equity avg `1.0165` n `134`; fx avg `0.0323` n `6`; index avg `0.0515` n `26`; metal avg `0.0002` n `20`; unknown avg `1.0842` n `759`
- 24h: commodity avg `-0.3088` n `12`; crypto_alt avg `0.4035` n `232`; crypto_major avg `0.1725` n `8`; equity avg `0.9606` n `134`; fx avg `-0.0559` n `6`; index avg `-0.046` n `26`; metal avg `-0.0489` n `20`; unknown avg `7138.4446` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal

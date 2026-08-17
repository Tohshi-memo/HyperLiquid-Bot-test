# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T21:07:26.765782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0261` n `12`; crypto_alt avg `0.0517` n `230`; crypto_major avg `0.0611` n `8`; equity avg `0.0298` n `114`; fx avg `-0.007` n `6`; index avg `0.014` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.0272` n `792`
- 1h: commodity avg `0.0222` n `12`; crypto_alt avg `0.1491` n `230`; crypto_major avg `0.1619` n `8`; equity avg `0.0378` n `114`; fx avg `0.0024` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0116` n `20`; unknown avg `-0.0908` n `792`
- 4h: commodity avg `0.3033` n `12`; crypto_alt avg `-0.0416` n `230`; crypto_major avg `-0.0082` n `8`; equity avg `-0.5956` n `114`; fx avg `0.0004` n `6`; index avg `-0.1158` n `25`; metal avg `-0.0823` n `20`; unknown avg `-0.0034` n `792`
- 24h: commodity avg `0.3929` n `12`; crypto_alt avg `0.2602` n `230`; crypto_major avg `1.0236` n `8`; equity avg `1.0166` n `114`; fx avg `0.0151` n `6`; index avg `0.0555` n `25`; metal avg `0.2081` n `20`; unknown avg `0.2013` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal

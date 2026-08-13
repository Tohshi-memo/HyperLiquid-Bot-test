# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T18:07:35.743853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0744` n `12`; crypto_alt avg `0.0563` n `230`; crypto_major avg `0.006` n `8`; equity avg `-0.1219` n `113`; fx avg `0.0018` n `6`; index avg `-0.0236` n `25`; metal avg `-0.0292` n `20`; unknown avg `0.0014` n `787`
- 1h: commodity avg `-0.1547` n `12`; crypto_alt avg `0.1631` n `230`; crypto_major avg `0.1278` n `8`; equity avg `-0.1534` n `113`; fx avg `0.0067` n `6`; index avg `-0.0262` n `25`; metal avg `-0.1051` n `20`; unknown avg `0.0985` n `787`
- 4h: commodity avg `0.1814` n `12`; crypto_alt avg `-0.5814` n `230`; crypto_major avg `-0.3328` n `8`; equity avg `0.1473` n `113`; fx avg `-0.0086` n `6`; index avg `0.066` n `25`; metal avg `-0.0815` n `20`; unknown avg `-0.1971` n `787`
- 24h: commodity avg `-0.4899` n `12`; crypto_alt avg `-0.686` n `230`; crypto_major avg `-0.1824` n `8`; equity avg `1.194` n `113`; fx avg `0.0025` n `6`; index avg `0.3111` n `25`; metal avg `-0.4252` n `20`; unknown avg `-0.0573` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2329`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal

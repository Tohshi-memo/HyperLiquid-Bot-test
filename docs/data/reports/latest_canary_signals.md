# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T14:05:03.217785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1541` n `12`; crypto_alt avg `-0.0105` n `230`; crypto_major avg `-0.1194` n `8`; equity avg `0.2331` n `113`; fx avg `0.0008` n `6`; index avg `0.0436` n `25`; metal avg `-0.0262` n `20`; unknown avg `0.0424` n `787`
- 1h: commodity avg `-0.1665` n `12`; crypto_alt avg `0.0142` n `230`; crypto_major avg `-0.0878` n `8`; equity avg `1.3314` n `113`; fx avg `-0.0112` n `6`; index avg `0.1866` n `25`; metal avg `-0.138` n `20`; unknown avg `0.013` n `787`
- 4h: commodity avg `-0.3978` n `12`; crypto_alt avg `0.0778` n `230`; crypto_major avg `-0.007` n `8`; equity avg `1.4851` n `113`; fx avg `-0.0388` n `6`; index avg `0.2447` n `25`; metal avg `-0.0412` n `20`; unknown avg `0.1282` n `787`
- 24h: commodity avg `-0.6192` n `12`; crypto_alt avg `-0.2994` n `230`; crypto_major avg `0.3164` n `8`; equity avg `1.8347` n `113`; fx avg `-0.0109` n `6`; index avg `0.2686` n `25`; metal avg `-0.5862` n `20`; unknown avg `0.346` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2302`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal

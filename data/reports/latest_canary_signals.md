# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T15:52:31.944422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `0.161` n `230`; crypto_major avg `-0.034` n `8`; equity avg `-0.0874` n `114`; fx avg `0.0103` n `6`; index avg `-0.0186` n `25`; metal avg `0.0403` n `20`; unknown avg `-0.0147` n `791`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `0.3536` n `230`; crypto_major avg `0.4147` n `8`; equity avg `-0.662` n `114`; fx avg `0.0535` n `6`; index avg `-0.114` n `25`; metal avg `0.0202` n `20`; unknown avg `0.1938` n `791`
- 4h: commodity avg `0.1478` n `12`; crypto_alt avg `0.2632` n `230`; crypto_major avg `0.0515` n `8`; equity avg `-1.1272` n `114`; fx avg `0.0861` n `6`; index avg `-0.1984` n `25`; metal avg `0.1232` n `20`; unknown avg `-0.2265` n `786`
- 24h: commodity avg `-0.1189` n `12`; crypto_alt avg `-0.3974` n `230`; crypto_major avg `-0.719` n `8`; equity avg `-0.3808` n `114`; fx avg `0.0793` n `6`; index avg `-0.069` n `25`; metal avg `0.1474` n `20`; unknown avg `0.3151` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal

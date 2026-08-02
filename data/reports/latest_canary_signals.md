# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T12:52:29.016993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.034` n `12`; crypto_alt avg `-0.0123` n `230`; crypto_major avg `-0.0599` n `8`; equity avg `0.0228` n `102`; fx avg `0.0031` n `6`; index avg `0.0019` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.0193` n `782`
- 1h: commodity avg `-0.0912` n `12`; crypto_alt avg `0.0292` n `230`; crypto_major avg `-0.0855` n `8`; equity avg `0.0442` n `102`; fx avg `0.0228` n `6`; index avg `-0.0077` n `25`; metal avg `0.0107` n `20`; unknown avg `-0.0302` n `782`
- 4h: commodity avg `0.1377` n `12`; crypto_alt avg `-0.1821` n `230`; crypto_major avg `-0.371` n `8`; equity avg `-0.2103` n `102`; fx avg `0.0931` n `6`; index avg `-0.0815` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0527` n `782`
- 24h: commodity avg `-1.1004` n `12`; crypto_alt avg `0.1896` n `230`; crypto_major avg `-0.046` n `8`; equity avg `0.8025` n `102`; fx avg `-0.0861` n `6`; index avg `0.215` n `25`; metal avg `0.2418` n `20`; unknown avg `0.2107` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal

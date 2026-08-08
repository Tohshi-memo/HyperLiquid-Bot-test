# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T02:07:23.879628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `0.0126` n `230`; crypto_major avg `0.0277` n `8`; equity avg `0.0691` n `112`; fx avg `-0.0012` n `6`; index avg `0.0056` n `25`; metal avg `-0.015` n `20`; unknown avg `-0.0932` n `783`
- 1h: commodity avg `-0.0292` n `12`; crypto_alt avg `0.1421` n `230`; crypto_major avg `0.1656` n `8`; equity avg `0.1226` n `112`; fx avg `-0.0008` n `6`; index avg `0.0271` n `25`; metal avg `-0.0497` n `20`; unknown avg `-0.1449` n `783`
- 4h: commodity avg `0.0062` n `12`; crypto_alt avg `0.2167` n `230`; crypto_major avg `0.1569` n `8`; equity avg `0.2311` n `112`; fx avg `-0.0056` n `6`; index avg `0.0095` n `25`; metal avg `0.034` n `20`; unknown avg `-0.1979` n `782`
- 24h: commodity avg `-0.1557` n `12`; crypto_alt avg `-0.5117` n `230`; crypto_major avg `0.037` n `8`; equity avg `1.9778` n `112`; fx avg `-0.0718` n `6`; index avg `0.2159` n `25`; metal avg `0.2822` n `20`; unknown avg `-0.0775` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal

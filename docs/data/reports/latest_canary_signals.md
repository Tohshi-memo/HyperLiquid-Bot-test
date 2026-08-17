# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T22:37:29.482841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.093` n `230`; crypto_major avg `-0.012` n `8`; equity avg `0.0022` n `114`; fx avg `-0.013` n `6`; index avg `0.0073` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.0229` n `793`
- 1h: commodity avg `0.0435` n `12`; crypto_alt avg `-0.3065` n `230`; crypto_major avg `-0.0346` n `8`; equity avg `0.1118` n `114`; fx avg `0.0132` n `6`; index avg `0.0203` n `25`; metal avg `-0.0108` n `20`; unknown avg `-0.049` n `792`
- 4h: commodity avg `0.1477` n `12`; crypto_alt avg `-0.3607` n `230`; crypto_major avg `-0.183` n `8`; equity avg `-0.1081` n `114`; fx avg `0.0129` n `6`; index avg `-0.011` n `25`; metal avg `0.0401` n `20`; unknown avg `-0.065` n `792`
- 24h: commodity avg `0.5724` n `12`; crypto_alt avg `0.5966` n `230`; crypto_major avg `1.5543` n `8`; equity avg `1.2337` n `114`; fx avg `0.0338` n `6`; index avg `0.0608` n `25`; metal avg `0.1753` n `20`; unknown avg `0.3604` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal

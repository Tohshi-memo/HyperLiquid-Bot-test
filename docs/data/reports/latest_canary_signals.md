# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T00:52:26.159357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0478` n `12`; crypto_alt avg `-0.1689` n `230`; crypto_major avg `-0.1029` n `8`; equity avg `-0.306` n `92`; fx avg `-0.0049` n `6`; index avg `-0.0909` n `25`; metal avg `0.0135` n `20`; unknown avg `0.0793` n `766`
- 1h: commodity avg `0.1405` n `12`; crypto_alt avg `0.367` n `230`; crypto_major avg `0.4152` n `8`; equity avg `-0.4269` n `92`; fx avg `0.0507` n `6`; index avg `-0.1342` n `25`; metal avg `-0.025` n `20`; unknown avg `-0.0543` n `766`
- 4h: commodity avg `-0.0941` n `12`; crypto_alt avg `-0.4272` n `230`; crypto_major avg `-0.3587` n `8`; equity avg `-0.9007` n `92`; fx avg `0.0221` n `6`; index avg `-0.2226` n `25`; metal avg `-0.2248` n `20`; unknown avg `0.0435` n `765`
- 24h: commodity avg `0.0028` n `12`; crypto_alt avg `0.1854` n `230`; crypto_major avg `0.8214` n `8`; equity avg `-0.8182` n `92`; fx avg `-0.005` n `6`; index avg `-0.2016` n `25`; metal avg `-0.2692` n `20`; unknown avg `0.3963` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal

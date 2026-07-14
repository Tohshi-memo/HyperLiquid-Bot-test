# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T22:52:31.800283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.1364` n `230`; crypto_major avg `-0.161` n `8`; equity avg `0.0058` n `92`; fx avg `-0.0015` n `6`; index avg `0.01` n `25`; metal avg `-0.0142` n `20`; unknown avg `0.1612` n `768`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `0.1844` n `230`; crypto_major avg `0.2744` n `8`; equity avg `-0.0029` n `92`; fx avg `0.0068` n `6`; index avg `0.0072` n `25`; metal avg `-0.0684` n `20`; unknown avg `-0.2215` n `768`
- 4h: commodity avg `0.0539` n `12`; crypto_alt avg `0.3429` n `230`; crypto_major avg `0.3288` n `8`; equity avg `0.1471` n `92`; fx avg `0.0154` n `6`; index avg `0.001` n `25`; metal avg `-0.007` n `20`; unknown avg `-0.2397` n `768`
- 24h: commodity avg `0.202` n `12`; crypto_alt avg `2.4997` n `230`; crypto_major avg `3.9987` n `8`; equity avg `1.4551` n `92`; fx avg `0.0173` n `6`; index avg `0.44` n `25`; metal avg `0.5311` n `20`; unknown avg `0.2628` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal

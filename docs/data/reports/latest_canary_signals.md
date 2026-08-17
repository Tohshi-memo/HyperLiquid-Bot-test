# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T15:37:25.410378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `0.1584` n `230`; crypto_major avg `0.1551` n `8`; equity avg `0.0007` n `114`; fx avg `0.0029` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0103` n `20`; unknown avg `-0.0279` n `792`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `0.207` n `230`; crypto_major avg `0.3629` n `8`; equity avg `0.4339` n `114`; fx avg `0.009` n `6`; index avg `0.0388` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.0099` n `792`
- 4h: commodity avg `0.1453` n `12`; crypto_alt avg `0.0097` n `230`; crypto_major avg `0.1613` n `8`; equity avg `0.5285` n `114`; fx avg `0.0239` n `6`; index avg `0.0759` n `25`; metal avg `0.0879` n `20`; unknown avg `0.0084` n `792`
- 24h: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.0879` n `230`; crypto_major avg `0.9461` n `8`; equity avg `1.6461` n `114`; fx avg `0.0051` n `6`; index avg `0.2215` n `25`; metal avg `0.3064` n `20`; unknown avg `0.0775` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal

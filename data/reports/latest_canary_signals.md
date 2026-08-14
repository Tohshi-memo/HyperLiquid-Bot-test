# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T00:06:18.824150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `0.0695` n `230`; crypto_major avg `0.0804` n `8`; equity avg `0.0168` n `113`; fx avg `0.0008` n `6`; index avg `0.0124` n `25`; metal avg `-0.0297` n `20`; unknown avg `0.153` n `787`
- 1h: commodity avg `0.0574` n `12`; crypto_alt avg `0.0978` n `230`; crypto_major avg `0.0878` n `8`; equity avg `0.0061` n `113`; fx avg `-0.0049` n `6`; index avg `0.039` n `25`; metal avg `0.0235` n `20`; unknown avg `0.0054` n `787`
- 4h: commodity avg `0.045` n `12`; crypto_alt avg `0.3475` n `230`; crypto_major avg `0.0311` n `8`; equity avg `0.298` n `113`; fx avg `-0.0045` n `6`; index avg `0.0703` n `25`; metal avg `0.0598` n `20`; unknown avg `0.0376` n `787`
- 24h: commodity avg `-0.3626` n `12`; crypto_alt avg `0.3738` n `230`; crypto_major avg `0.5391` n `8`; equity avg `1.3008` n `113`; fx avg `0.0499` n `6`; index avg `0.3073` n `25`; metal avg `-0.5299` n `20`; unknown avg `0.1563` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal

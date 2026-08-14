# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T02:52:27.893261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `0.0136` n `230`; crypto_major avg `0.0437` n `8`; equity avg `-0.0574` n `113`; fx avg `0.0002` n `6`; index avg `-0.009` n `25`; metal avg `-0.0221` n `20`; unknown avg `0.0403` n `787`
- 1h: commodity avg `0.0678` n `12`; crypto_alt avg `-0.1001` n `230`; crypto_major avg `0.017` n `8`; equity avg `-0.0057` n `113`; fx avg `-0.0022` n `6`; index avg `0.0118` n `25`; metal avg `0.0756` n `20`; unknown avg `-0.1195` n `787`
- 4h: commodity avg `0.0706` n `12`; crypto_alt avg `-0.0026` n `230`; crypto_major avg `-0.0374` n `8`; equity avg `-0.3933` n `113`; fx avg `-0.0568` n `6`; index avg `-0.0582` n `25`; metal avg `-0.1524` n `20`; unknown avg `0.3723` n `787`
- 24h: commodity avg `-0.2771` n `12`; crypto_alt avg `0.2752` n `230`; crypto_major avg `0.3763` n `8`; equity avg `0.81` n `113`; fx avg `-0.0103` n `6`; index avg `0.2169` n `25`; metal avg `-0.5713` n `20`; unknown avg `1.1041` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2458`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal

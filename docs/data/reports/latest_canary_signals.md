# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T14:07:34.282044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2046` n `12`; crypto_alt avg `0.2103` n `230`; crypto_major avg `0.2763` n `8`; equity avg `0.084` n `108`; fx avg `-0.0079` n `6`; index avg `-0.0123` n `25`; metal avg `0.136` n `20`; unknown avg `0.0526` n `782`
- 1h: commodity avg `-0.2452` n `12`; crypto_alt avg `0.042` n `230`; crypto_major avg `0.1814` n `8`; equity avg `0.6433` n `108`; fx avg `-0.0181` n `6`; index avg `0.0541` n `25`; metal avg `0.2273` n `20`; unknown avg `0.0021` n `782`
- 4h: commodity avg `-0.4309` n `12`; crypto_alt avg `0.081` n `230`; crypto_major avg `0.2654` n `8`; equity avg `0.7106` n `108`; fx avg `-0.0357` n `6`; index avg `0.1551` n `25`; metal avg `0.2993` n `20`; unknown avg `0.0094` n `781`
- 24h: commodity avg `-0.2605` n `12`; crypto_alt avg `0.9562` n `230`; crypto_major avg `0.8146` n `8`; equity avg `1.9056` n `108`; fx avg `0.0631` n `6`; index avg `0.4184` n `25`; metal avg `0.7555` n `20`; unknown avg `0.7424` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal

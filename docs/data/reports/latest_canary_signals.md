# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T04:49:08.568709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `-0.0536` n `230`; crypto_major avg `0.0119` n `8`; equity avg `0.0893` n `108`; fx avg `0.0259` n `6`; index avg `0.0189` n `25`; metal avg `-0.0262` n `20`; unknown avg `-0.0832` n `781`
- 1h: commodity avg `0.1035` n `12`; crypto_alt avg `0.1887` n `230`; crypto_major avg `0.1313` n `8`; equity avg `0.1303` n `108`; fx avg `0.0366` n `6`; index avg `0.0119` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0541` n `781`
- 4h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.6058` n `230`; crypto_major avg `0.4703` n `8`; equity avg `0.6594` n `108`; fx avg `0.0238` n `6`; index avg `0.0344` n `25`; metal avg `0.3341` n `20`; unknown avg `-0.1345` n `781`
- 24h: commodity avg `-1.4563` n `12`; crypto_alt avg `0.1843` n `230`; crypto_major avg `0.2505` n `8`; equity avg `4.0781` n `108`; fx avg `0.0203` n `6`; index avg `0.8539` n `25`; metal avg `0.987` n `20`; unknown avg `0.3656` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal

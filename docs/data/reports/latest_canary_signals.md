# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T21:37:23.317945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.0629` n `230`; crypto_major avg `-0.04` n `8`; equity avg `0.0128` n `92`; fx avg `0.0047` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.0227` n `765`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.206` n `230`; crypto_major avg `-0.2567` n `8`; equity avg `-0.0131` n `92`; fx avg `-0.0238` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0123` n `765`
- 4h: commodity avg `0.0611` n `12`; crypto_alt avg `-0.3769` n `230`; crypto_major avg `-0.3488` n `8`; equity avg `0.0304` n `92`; fx avg `-0.0482` n `6`; index avg `-0.0226` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.0654` n `765`
- 24h: commodity avg `0.6417` n `12`; crypto_alt avg `-1.6139` n `230`; crypto_major avg `-0.9815` n `8`; equity avg `-0.2047` n `92`; fx avg `-0.0378` n `6`; index avg `-0.0987` n `25`; metal avg `-0.1031` n `20`; unknown avg `0.2843` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal

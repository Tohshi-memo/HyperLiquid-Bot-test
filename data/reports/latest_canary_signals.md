# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T02:52:28.080488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0153` n `12`; crypto_alt avg `0.1365` n `230`; crypto_major avg `0.1401` n `8`; equity avg `0.0902` n `108`; fx avg `0.0144` n `6`; index avg `0.0062` n `25`; metal avg `-0.0151` n `20`; unknown avg `-0.0826` n `782`
- 1h: commodity avg `-0.0159` n `12`; crypto_alt avg `-0.1352` n `230`; crypto_major avg `-0.3868` n `8`; equity avg `0.572` n `108`; fx avg `0.0404` n `6`; index avg `0.0789` n `25`; metal avg `-0.0444` n `20`; unknown avg `-0.0186` n `782`
- 4h: commodity avg `0.1182` n `12`; crypto_alt avg `-0.1793` n `230`; crypto_major avg `-0.5626` n `8`; equity avg `-0.1576` n `108`; fx avg `-0.0228` n `6`; index avg `-0.1735` n `25`; metal avg `0.2088` n `20`; unknown avg `-0.0571` n `782`
- 24h: commodity avg `0.1916` n `12`; crypto_alt avg `-0.1467` n `230`; crypto_major avg `-0.5587` n `8`; equity avg `-1.3752` n `108`; fx avg `0.0239` n `6`; index avg `-0.2938` n `25`; metal avg `0.6313` n `20`; unknown avg `0.9017` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal

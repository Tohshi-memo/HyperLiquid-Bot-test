# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T20:32:25.010690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `-0.0542` n `230`; crypto_major avg `-0.0228` n `8`; equity avg `0.0057` n `96`; fx avg `-0.0081` n `6`; index avg `0.0022` n `25`; metal avg `-0.0162` n `20`; unknown avg `-0.0134` n `769`
- 1h: commodity avg `0.1173` n `12`; crypto_alt avg `-0.1139` n `230`; crypto_major avg `-0.1093` n `8`; equity avg `-0.4758` n `96`; fx avg `-0.04` n `6`; index avg `-0.0829` n `25`; metal avg `-0.0292` n `20`; unknown avg `-0.0159` n `769`
- 4h: commodity avg `0.115` n `12`; crypto_alt avg `-0.2114` n `230`; crypto_major avg `0.2232` n `8`; equity avg `-0.6871` n `96`; fx avg `-0.0259` n `6`; index avg `-0.1114` n `25`; metal avg `-0.0536` n `20`; unknown avg `0.2493` n `769`
- 24h: commodity avg `0.6975` n `12`; crypto_alt avg `-1.2921` n `230`; crypto_major avg `-1.276` n `8`; equity avg `-1.46` n `94`; fx avg `0.0724` n `6`; index avg `-0.2795` n `25`; metal avg `-0.0263` n `20`; unknown avg `-0.0464` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal

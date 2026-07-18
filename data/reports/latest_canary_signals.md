# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T01:02:57.439043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.0701` n `230`; crypto_major avg `-0.0597` n `8`; equity avg `0.0285` n `96`; fx avg `0.0212` n `6`; index avg `0.0031` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0164` n `769`
- 1h: commodity avg `-0.0592` n `12`; crypto_alt avg `-0.0809` n `230`; crypto_major avg `-0.0338` n `8`; equity avg `0.109` n `96`; fx avg `0.0255` n `6`; index avg `0.0566` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.0981` n `769`
- 4h: commodity avg `-0.0372` n `12`; crypto_alt avg `-0.0237` n `230`; crypto_major avg `-0.225` n `8`; equity avg `0.0974` n `96`; fx avg `0.0027` n `6`; index avg `0.0149` n `25`; metal avg `0.0743` n `20`; unknown avg `-0.0393` n `769`
- 24h: commodity avg `0.609` n `12`; crypto_alt avg `-0.7857` n `230`; crypto_major avg `-0.9579` n `8`; equity avg `-0.5596` n `94`; fx avg `0.0865` n `6`; index avg `-0.1451` n `25`; metal avg `0.0191` n `20`; unknown avg `0.1094` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal

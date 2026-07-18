# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T01:07:23.685711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.1059` n `230`; crypto_major avg `-0.0567` n `8`; equity avg `0.0267` n `96`; fx avg `0.0194` n `6`; index avg `-0.0039` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0386` n `769`
- 1h: commodity avg `-0.0674` n `12`; crypto_alt avg `-0.1168` n `230`; crypto_major avg `-0.0308` n `8`; equity avg `0.1072` n `96`; fx avg `0.0237` n `6`; index avg `0.0496` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.1221` n `769`
- 4h: commodity avg `-0.0454` n `12`; crypto_alt avg `-0.0591` n `230`; crypto_major avg `-0.222` n `8`; equity avg `0.0955` n `96`; fx avg `0.0009` n `6`; index avg `0.0078` n `25`; metal avg `0.0743` n `20`; unknown avg `-0.0672` n `769`
- 24h: commodity avg `0.6006` n `12`; crypto_alt avg `-0.8205` n `230`; crypto_major avg `-0.9551` n `8`; equity avg `-0.5589` n `94`; fx avg `0.0848` n `6`; index avg `-0.1522` n `25`; metal avg `0.0191` n `20`; unknown avg `0.1079` n `736`

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
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal

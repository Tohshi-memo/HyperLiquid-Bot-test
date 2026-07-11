# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T04:37:29.076468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.0219` n `229`; crypto_major avg `-0.0145` n `8`; equity avg `-0.0475` n `92`; fx avg `0.0` n `6`; index avg `0.0016` n `25`; metal avg `0.0072` n `20`; unknown avg `-0.036` n `765`
- 1h: commodity avg `-0.0511` n `12`; crypto_alt avg `-0.1054` n `229`; crypto_major avg `-0.0556` n `8`; equity avg `-0.0647` n `92`; fx avg `-0.0008` n `6`; index avg `0.0064` n `25`; metal avg `-0.0079` n `20`; unknown avg `-0.0727` n `763`
- 4h: commodity avg `-0.0933` n `12`; crypto_alt avg `0.3021` n `229`; crypto_major avg `0.1061` n `8`; equity avg `0.0075` n `92`; fx avg `0.0033` n `6`; index avg `0.0106` n `25`; metal avg `0.0286` n `20`; unknown avg `0.299` n `763`
- 24h: commodity avg `-0.3911` n `12`; crypto_alt avg `0.4303` n `229`; crypto_major avg `-0.2994` n `8`; equity avg `-0.8332` n `92`; fx avg `-0.1947` n `6`; index avg `0.0213` n `25`; metal avg `-0.0182` n `20`; unknown avg `4.2139` n `730`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T22:37:29.165812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0281` n `12`; crypto_alt avg `0.1099` n `230`; crypto_major avg `0.147` n `8`; equity avg `0.0023` n `102`; fx avg `0.0045` n `6`; index avg `0.0187` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0276` n `779`
- 1h: commodity avg `0.0204` n `12`; crypto_alt avg `0.1395` n `230`; crypto_major avg `0.3719` n `8`; equity avg `0.255` n `102`; fx avg `0.0337` n `6`; index avg `0.0727` n `25`; metal avg `0.017` n `20`; unknown avg `-0.1459` n `779`
- 4h: commodity avg `0.0742` n `12`; crypto_alt avg `0.3009` n `230`; crypto_major avg `0.3939` n `8`; equity avg `1.5511` n `102`; fx avg `0.0673` n `6`; index avg `0.2258` n `25`; metal avg `0.0805` n `20`; unknown avg `-0.1379` n `779`
- 24h: commodity avg `-0.0186` n `12`; crypto_alt avg `1.0521` n `230`; crypto_major avg `1.8411` n `8`; equity avg `7.4342` n `102`; fx avg `-0.3997` n `6`; index avg `0.9178` n `25`; metal avg `0.5516` n `20`; unknown avg `0.1082` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal

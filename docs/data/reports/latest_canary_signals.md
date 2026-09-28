# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T06:08:05.594480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0275` n `12`; crypto_alt avg `0.215` n `234`; crypto_major avg `0.1105` n `8`; equity avg `0.0862` n `141`; fx avg `0.0066` n `6`; index avg `0.0152` n `26`; metal avg `0.0417` n `20`; unknown avg `1.0759` n `936`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.3914` n `234`; crypto_major avg `-0.484` n `8`; equity avg `-0.1792` n `141`; fx avg `0.0275` n `6`; index avg `-0.0299` n `26`; metal avg `-0.0378` n `20`; unknown avg `1.0581` n `936`
- 4h: commodity avg `0.0332` n `12`; crypto_alt avg `-1.4013` n `234`; crypto_major avg `-0.7891` n `8`; equity avg `-0.3801` n `141`; fx avg `-0.0115` n `6`; index avg `-0.0223` n `26`; metal avg `-0.171` n `20`; unknown avg `1.274` n `926`
- 24h: commodity avg `-0.3377` n `12`; crypto_alt avg `-2.035` n `234`; crypto_major avg `-2.0848` n `8`; equity avg `-1.5882` n `141`; fx avg `0.0849` n `6`; index avg `-0.1611` n `26`; metal avg `-0.7602` n `20`; unknown avg `3.5583` n `815`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal

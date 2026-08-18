# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T04:22:27.540096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.0059` n `230`; crypto_major avg `0.0294` n `8`; equity avg `-0.0181` n `114`; fx avg `0.009` n `6`; index avg `-0.0035` n `25`; metal avg `0.0` n `20`; unknown avg `0.0033` n `793`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `0.0613` n `230`; crypto_major avg `0.0798` n `8`; equity avg `0.3152` n `114`; fx avg `0.0305` n `6`; index avg `0.0229` n `25`; metal avg `-0.0264` n `20`; unknown avg `-0.0143` n `793`
- 4h: commodity avg `0.0596` n `12`; crypto_alt avg `-1.0455` n `230`; crypto_major avg `-0.5791` n `8`; equity avg `-1.6749` n `114`; fx avg `-0.0053` n `6`; index avg `-0.272` n `25`; metal avg `-0.3219` n `20`; unknown avg `0.3718` n `793`
- 24h: commodity avg `0.6514` n `12`; crypto_alt avg `-1.5243` n `230`; crypto_major avg `-0.136` n `8`; equity avg `-1.1008` n `114`; fx avg `-0.0143` n `6`; index avg `-0.2963` n `25`; metal avg `-0.2057` n `20`; unknown avg `0.009` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal

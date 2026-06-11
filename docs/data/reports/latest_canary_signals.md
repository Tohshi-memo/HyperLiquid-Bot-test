# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T10:52:30.788035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0613` n `12`; crypto_alt avg `-0.0518` n `228`; crypto_major avg `0.0823` n `8`; equity avg `-0.0577` n `74`; fx avg `0.0048` n `6`; index avg `0.023` n `23`; metal avg `0.0504` n `18`; unknown avg `-0.015` n `556`
- 1h: commodity avg `-0.157` n `12`; crypto_alt avg `-0.1376` n `228`; crypto_major avg `-0.0191` n `8`; equity avg `0.0235` n `74`; fx avg `-0.0217` n `6`; index avg `0.0479` n `23`; metal avg `-0.0139` n `18`; unknown avg `-1.6846` n `556`
- 4h: commodity avg `-0.6866` n `12`; crypto_alt avg `0.2692` n `228`; crypto_major avg `0.3637` n `8`; equity avg `0.6503` n `74`; fx avg `-0.0822` n `6`; index avg `0.3372` n `23`; metal avg `-0.1249` n `18`; unknown avg `0.7002` n `548`
- 24h: commodity avg `0.2032` n `12`; crypto_alt avg `1.4459` n `228`; crypto_major avg `1.5651` n `8`; equity avg `0.9216` n `74`; fx avg `-0.0068` n `6`; index avg `0.2822` n `23`; metal avg `-0.6507` n `18`; unknown avg `4.431` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal

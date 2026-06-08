# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T08:22:26.921293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.3727` n `228`; crypto_major avg `-0.5748` n `8`; equity avg `0.0577` n `74`; fx avg `-0.004` n `6`; index avg `0.0715` n `23`; metal avg `0.0101` n `18`; unknown avg `-0.1884` n `517`
- 1h: commodity avg `-0.0751` n `12`; crypto_alt avg `-0.1567` n `228`; crypto_major avg `-0.6246` n `8`; equity avg `0.3347` n `74`; fx avg `-0.0275` n `6`; index avg `0.1312` n `23`; metal avg `-0.2071` n `18`; unknown avg `-0.1177` n `517`
- 4h: commodity avg `0.1039` n `12`; crypto_alt avg `0.3262` n `228`; crypto_major avg `0.0097` n `8`; equity avg `0.1274` n `74`; fx avg `-0.2232` n `6`; index avg `0.1184` n `23`; metal avg `-0.465` n `18`; unknown avg `-0.239` n `507`
- 24h: commodity avg `1.0121` n `12`; crypto_alt avg `0.2768` n `228`; crypto_major avg `1.2849` n `8`; equity avg `0.9866` n `74`; fx avg `-0.3356` n `6`; index avg `0.1543` n `23`; metal avg `-0.8134` n `18`; unknown avg `-4.8778` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal

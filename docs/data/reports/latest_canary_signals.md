# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T00:52:25.521515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2407` n `12`; crypto_alt avg `0.0629` n `228`; crypto_major avg `-0.0401` n `8`; equity avg `-0.1286` n `74`; fx avg `-0.0011` n `6`; index avg `0.0218` n `23`; metal avg `0.1298` n `18`; unknown avg `-0.0371` n `547`
- 1h: commodity avg `0.0566` n `12`; crypto_alt avg `-0.1253` n `228`; crypto_major avg `-0.3855` n `8`; equity avg `0.1031` n `74`; fx avg `-0.0778` n `6`; index avg `0.0263` n `23`; metal avg `-0.2302` n `18`; unknown avg `-0.2587` n `547`
- 4h: commodity avg `0.071` n `12`; crypto_alt avg `-0.7224` n `228`; crypto_major avg `-1.1895` n `8`; equity avg `-0.5959` n `74`; fx avg `-0.0676` n `6`; index avg `-0.214` n `23`; metal avg `-0.9614` n `18`; unknown avg `-0.4963` n `547`
- 24h: commodity avg `-0.5501` n `12`; crypto_alt avg `0.4898` n `228`; crypto_major avg `-1.823` n `8`; equity avg `-1.6729` n `74`; fx avg `0.0425` n `6`; index avg `-0.6221` n `23`; metal avg `-1.9337` n `18`; unknown avg `-0.3048` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0375`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0362`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.033`, n `668`, weak_sample_signal

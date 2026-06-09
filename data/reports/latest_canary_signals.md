# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T19:37:42.266102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `0.1532` n `228`; crypto_major avg `0.1505` n `8`; equity avg `0.0803` n `74`; fx avg `-0.0076` n `6`; index avg `0.0184` n `23`; metal avg `-0.0049` n `18`; unknown avg `0.0771` n `547`
- 1h: commodity avg `-0.179` n `12`; crypto_alt avg `0.1165` n `228`; crypto_major avg `0.1198` n `8`; equity avg `-0.1084` n `74`; fx avg `-0.0042` n `6`; index avg `-0.0184` n `23`; metal avg `-0.2748` n `18`; unknown avg `0.055` n `547`
- 4h: commodity avg `0.0522` n `12`; crypto_alt avg `1.4116` n `228`; crypto_major avg `0.8635` n `8`; equity avg `0.6923` n `74`; fx avg `-0.0398` n `6`; index avg `0.078` n `23`; metal avg `-0.0776` n `18`; unknown avg `0.0521` n `547`
- 24h: commodity avg `-0.9752` n `12`; crypto_alt avg `-2.1491` n `228`; crypto_major avg `-2.9033` n `8`; equity avg `-2.0262` n `74`; fx avg `0.0938` n `6`; index avg `-1.2862` n `23`; metal avg `-1.461` n `18`; unknown avg `-1.4235` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0456`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0438`, n `668`, weak_sample_signal

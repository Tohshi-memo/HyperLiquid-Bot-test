# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T01:07:29.001332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2536` n `12`; crypto_alt avg `0.0806` n `228`; crypto_major avg `0.178` n `8`; equity avg `0.1223` n `78`; fx avg `0.0502` n `6`; index avg `0.0411` n `23`; metal avg `0.3855` n `18`; unknown avg `0.9905` n `694`
- 1h: commodity avg `-0.2543` n `12`; crypto_alt avg `0.7766` n `228`; crypto_major avg `0.6715` n `8`; equity avg `0.3447` n `78`; fx avg `0.0606` n `6`; index avg `0.165` n `23`; metal avg `0.8779` n `18`; unknown avg `0.6614` n `694`
- 4h: commodity avg `-0.2638` n `12`; crypto_alt avg `0.9162` n `228`; crypto_major avg `0.7629` n `8`; equity avg `-0.3192` n `78`; fx avg `0.1463` n `6`; index avg `0.0279` n `23`; metal avg `0.8505` n `18`; unknown avg `1.2687` n `694`
- 24h: commodity avg `-0.1483` n `12`; crypto_alt avg `0.0866` n `228`; crypto_major avg `-0.7557` n `8`; equity avg `-0.4483` n `78`; fx avg `-0.0333` n `6`; index avg `0.0222` n `23`; metal avg `0.7153` n `18`; unknown avg `0.8615` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal

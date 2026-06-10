# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T14:52:35.053831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1538` n `12`; crypto_alt avg `-0.064` n `228`; crypto_major avg `0.1215` n `8`; equity avg `-0.3593` n `74`; fx avg `-0.0018` n `6`; index avg `-0.3565` n `23`; metal avg `-0.2451` n `18`; unknown avg `0.1531` n `548`
- 1h: commodity avg `0.0673` n `12`; crypto_alt avg `-0.72` n `228`; crypto_major avg `-0.4647` n `8`; equity avg `-0.3532` n `74`; fx avg `-0.047` n `6`; index avg `-0.1208` n `23`; metal avg `-0.7112` n `18`; unknown avg `0.0107` n `547`
- 4h: commodity avg `0.9252` n `12`; crypto_alt avg `0.7611` n `228`; crypto_major avg `1.1662` n `8`; equity avg `1.6476` n `74`; fx avg `-0.0211` n `6`; index avg `0.7019` n `23`; metal avg `0.2096` n `18`; unknown avg `1.4277` n `547`
- 24h: commodity avg `1.0616` n `12`; crypto_alt avg `0.5704` n `228`; crypto_major avg `-0.4199` n `8`; equity avg `-0.3461` n `74`; fx avg `-0.0784` n `6`; index avg `-0.2577` n `23`; metal avg `-1.675` n `18`; unknown avg `1.6636` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T19:37:26.036606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0892` n `228`; crypto_major avg `0.0166` n `8`; equity avg `-0.0082` n `74`; fx avg `0.0131` n `6`; index avg `-0.0241` n `23`; metal avg `-0.0723` n `18`; unknown avg `0.0937` n `645`
- 1h: commodity avg `0.1239` n `12`; crypto_alt avg `0.4522` n `228`; crypto_major avg `0.2716` n `8`; equity avg `0.086` n `74`; fx avg `-0.0061` n `6`; index avg `-0.0181` n `23`; metal avg `-0.0658` n `18`; unknown avg `0.2073` n `645`
- 4h: commodity avg `0.1344` n `12`; crypto_alt avg `0.2284` n `228`; crypto_major avg `0.0058` n `8`; equity avg `-0.0562` n `74`; fx avg `0.0041` n `6`; index avg `-0.0644` n `23`; metal avg `-0.0566` n `18`; unknown avg `-0.2544` n `645`
- 24h: commodity avg `0.2347` n `12`; crypto_alt avg `-1.1135` n `228`; crypto_major avg `-0.4932` n `8`; equity avg `0.2635` n `74`; fx avg `-0.0491` n `6`; index avg `0.2042` n `23`; metal avg `-0.1801` n `18`; unknown avg `1.0662` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal

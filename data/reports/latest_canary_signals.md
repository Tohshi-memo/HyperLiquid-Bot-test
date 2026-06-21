# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T17:07:26.267161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `12`; crypto_alt avg `0.0869` n `228`; crypto_major avg `0.0269` n `8`; equity avg `0.0054` n `78`; fx avg `-0.0214` n `6`; index avg `0.0025` n `23`; metal avg `-0.0096` n `18`; unknown avg `-0.0562` n `702`
- 1h: commodity avg `0.1477` n `12`; crypto_alt avg `-0.0577` n `228`; crypto_major avg `0.112` n `8`; equity avg `0.0174` n `78`; fx avg `-0.0868` n `6`; index avg `0.0028` n `23`; metal avg `-0.0038` n `18`; unknown avg `-0.6665` n `702`
- 4h: commodity avg `0.2243` n `12`; crypto_alt avg `0.3373` n `228`; crypto_major avg `0.4189` n `8`; equity avg `-0.0133` n `78`; fx avg `0.0146` n `6`; index avg `0.0003` n `23`; metal avg `-0.0276` n `18`; unknown avg `-0.523` n `702`
- 24h: commodity avg `0.123` n `12`; crypto_alt avg `1.5767` n `228`; crypto_major avg `0.4235` n `8`; equity avg `0.4214` n `78`; fx avg `-0.0691` n `6`; index avg `0.0335` n `23`; metal avg `-0.0459` n `18`; unknown avg `-0.1036` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal

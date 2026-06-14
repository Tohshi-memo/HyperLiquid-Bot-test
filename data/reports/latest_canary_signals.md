# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T08:48:04.988932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `0.0589` n `228`; crypto_major avg `-0.0098` n `8`; equity avg `-0.0712` n `74`; fx avg `0.0013` n `6`; index avg `-0.0028` n `23`; metal avg `0.0023` n `18`; unknown avg `-0.3222` n `645`
- 1h: commodity avg `0.027` n `12`; crypto_alt avg `0.3142` n `228`; crypto_major avg `0.1154` n `8`; equity avg `0.0492` n `74`; fx avg `-0.0008` n `6`; index avg `0.0204` n `23`; metal avg `0.029` n `18`; unknown avg `2.1149` n `645`
- 4h: commodity avg `-0.2833` n `12`; crypto_alt avg `0.3269` n `228`; crypto_major avg `-0.0231` n `8`; equity avg `0.1945` n `74`; fx avg `-0.0055` n `6`; index avg `0.0174` n `23`; metal avg `0.0326` n `18`; unknown avg `1.8751` n `625`
- 24h: commodity avg `-0.9186` n `12`; crypto_alt avg `0.6506` n `228`; crypto_major avg `0.7975` n `8`; equity avg `0.6927` n `74`; fx avg `0.039` n `6`; index avg `0.2634` n `23`; metal avg `0.2599` n `18`; unknown avg `-0.7692` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal

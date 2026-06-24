# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T08:07:28.887637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0644` n `12`; crypto_alt avg `0.0802` n `228`; crypto_major avg `-0.0498` n `8`; equity avg `0.1552` n `86`; fx avg `-0.0168` n `6`; index avg `0.0272` n `23`; metal avg `-0.0545` n `20`; unknown avg `0.0181` n `764`
- 1h: commodity avg `-0.0623` n `12`; crypto_alt avg `-0.0775` n `228`; crypto_major avg `-0.1307` n `8`; equity avg `0.1195` n `86`; fx avg `-0.0392` n `6`; index avg `0.0227` n `23`; metal avg `-0.1026` n `20`; unknown avg `-0.07` n `764`
- 4h: commodity avg `-0.0882` n `12`; crypto_alt avg `0.1132` n `228`; crypto_major avg `0.0939` n `8`; equity avg `0.6984` n `86`; fx avg `0.0447` n `6`; index avg `0.223` n `23`; metal avg `0.1728` n `20`; unknown avg `-0.0657` n `732`
- 24h: commodity avg `-0.523` n `12`; crypto_alt avg `-0.6175` n `228`; crypto_major avg `-0.9649` n `8`; equity avg `4.8585` n `86`; fx avg `-0.0457` n `6`; index avg `0.1173` n `23`; metal avg `-0.1788` n `20`; unknown avg `0.3281` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal

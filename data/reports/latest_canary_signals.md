# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T20:52:26.464272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.79` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.5004` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.0375` n `229`; crypto_major avg `0.0293` n `8`; equity avg `-0.0281` n `88`; fx avg `-0.0007` n `6`; index avg `-0.0018` n `25`; metal avg `0.0034` n `20`; unknown avg `0.1005` n `765`
- 1h: commodity avg `-0.0613` n `12`; crypto_alt avg `0.5766` n `229`; crypto_major avg `0.6254` n `8`; equity avg `-0.0384` n `88`; fx avg `-0.0193` n `6`; index avg `-0.0342` n `25`; metal avg `0.0017` n `20`; unknown avg `0.2632` n `765`
- 4h: commodity avg `-0.0707` n `12`; crypto_alt avg `0.9339` n `229`; crypto_major avg `1.4833` n `8`; equity avg `0.0297` n `88`; fx avg `-0.0157` n `6`; index avg `-0.0289` n `25`; metal avg `-0.0171` n `20`; unknown avg `1.8677` n `765`
- 24h: commodity avg `0.1` n `12`; crypto_alt avg `3.4339` n `229`; crypto_major avg `3.5355` n `8`; equity avg `1.7733` n `88`; fx avg `-0.0929` n `6`; index avg `0.4875` n `25`; metal avg `0.5801` n `20`; unknown avg `8.3026` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal

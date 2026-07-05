# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T20:52:30.401950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0469` n `229`; crypto_major avg `0.0414` n `8`; equity avg `-0.0109` n `88`; fx avg `-0.0088` n `6`; index avg `-0.0` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0776` n `765`
- 1h: commodity avg `-0.0372` n `12`; crypto_alt avg `-0.0012` n `229`; crypto_major avg `0.0266` n `8`; equity avg `0.0049` n `88`; fx avg `-0.0231` n `6`; index avg `-0.0034` n `25`; metal avg `0.0127` n `20`; unknown avg `-0.095` n `765`
- 4h: commodity avg `-0.0754` n `12`; crypto_alt avg `0.3963` n `229`; crypto_major avg `0.3603` n `8`; equity avg `0.1252` n `88`; fx avg `-0.0224` n `6`; index avg `0.0043` n `25`; metal avg `0.0064` n `20`; unknown avg `0.677` n `765`
- 24h: commodity avg `-0.0339` n `12`; crypto_alt avg `-0.9187` n `229`; crypto_major avg `-0.3298` n `8`; equity avg `0.3376` n `88`; fx avg `-0.0692` n `6`; index avg `0.0849` n `25`; metal avg `0.0305` n `20`; unknown avg `1.1344` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T01:52:29.018426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.7` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1002` n `12`; crypto_alt avg `-0.4386` n `229`; crypto_major avg `-0.5324` n `8`; equity avg `-0.3498` n `88`; fx avg `0.0102` n `6`; index avg `-0.1335` n `25`; metal avg `-0.0669` n `20`; unknown avg `0.3712` n `765`
- 1h: commodity avg `0.0715` n `12`; crypto_alt avg `-0.1925` n `229`; crypto_major avg `-0.2928` n `8`; equity avg `-0.8686` n `88`; fx avg `0.0271` n `6`; index avg `-0.2207` n `25`; metal avg `0.0242` n `20`; unknown avg `0.0304` n `765`
- 4h: commodity avg `-0.1647` n `12`; crypto_alt avg `-0.1661` n `229`; crypto_major avg `0.4355` n `8`; equity avg `-0.9963` n `88`; fx avg `0.0882` n `6`; index avg `-0.1263` n `25`; metal avg `0.102` n `20`; unknown avg `0.0849` n `765`
- 24h: commodity avg `-0.1573` n `12`; crypto_alt avg `0.4269` n `229`; crypto_major avg `1.5415` n `8`; equity avg `-0.6972` n `88`; fx avg `0.0611` n `6`; index avg `-0.0569` n `25`; metal avg `0.098` n `20`; unknown avg `1.4326` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal

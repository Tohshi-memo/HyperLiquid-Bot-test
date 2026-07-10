# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T11:22:27.936428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.0801` n `229`; crypto_major avg `0.0232` n `8`; equity avg `0.1214` n `91`; fx avg `-0.0051` n `6`; index avg `0.0086` n `25`; metal avg `0.0352` n `20`; unknown avg `0.0113` n `766`
- 1h: commodity avg `0.0907` n `12`; crypto_alt avg `0.0589` n `229`; crypto_major avg `0.0692` n `8`; equity avg `0.4741` n `91`; fx avg `0.0087` n `6`; index avg `0.0501` n `25`; metal avg `0.002` n `20`; unknown avg `0.076` n `766`
- 4h: commodity avg `0.1663` n `12`; crypto_alt avg `0.5194` n `229`; crypto_major avg `0.6428` n `8`; equity avg `0.7532` n `91`; fx avg `0.0181` n `6`; index avg `0.098` n `25`; metal avg `-0.1385` n `20`; unknown avg `0.1142` n `765`
- 24h: commodity avg `-0.974` n `12`; crypto_alt avg `1.3972` n `229`; crypto_major avg `2.1527` n `8`; equity avg `1.1769` n `91`; fx avg `-0.1088` n `6`; index avg `0.3026` n `25`; metal avg `0.2381` n `20`; unknown avg `0.0531` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T21:07:34.776536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.1449` n `228`; crypto_major avg `-0.1194` n `8`; equity avg `0.0292` n `88`; fx avg `-0.0017` n `6`; index avg `0.0139` n `23`; metal avg `0.0083` n `20`; unknown avg `0.0275` n `765`
- 1h: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.4296` n `228`; crypto_major avg `-0.4193` n `8`; equity avg `0.0922` n `88`; fx avg `0.0036` n `6`; index avg `0.0223` n `23`; metal avg `0.0443` n `20`; unknown avg `-0.0625` n `765`
- 4h: commodity avg `-0.0797` n `12`; crypto_alt avg `-0.1183` n `228`; crypto_major avg `0.7659` n `8`; equity avg `0.6657` n `88`; fx avg `-0.0114` n `6`; index avg `0.092` n `23`; metal avg `0.197` n `20`; unknown avg `-0.234` n `765`
- 24h: commodity avg `-0.372` n `12`; crypto_alt avg `1.3494` n `228`; crypto_major avg `2.726` n `8`; equity avg `1.6912` n `88`; fx avg `0.1737` n `6`; index avg `0.1642` n `23`; metal avg `-0.4883` n `20`; unknown avg `1.245` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal

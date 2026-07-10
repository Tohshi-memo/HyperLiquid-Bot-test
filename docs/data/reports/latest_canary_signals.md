# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T18:04:47.571629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `12`; crypto_alt avg `-0.0365` n `229`; crypto_major avg `-0.0022` n `8`; equity avg `-0.043` n `92`; fx avg `-0.0029` n `6`; index avg `0.0094` n `25`; metal avg `-0.0266` n `20`; unknown avg `-0.0082` n `765`
- 1h: commodity avg `0.0312` n `12`; crypto_alt avg `-0.1626` n `229`; crypto_major avg `-0.2107` n `8`; equity avg `0.0727` n `92`; fx avg `-0.0249` n `6`; index avg `0.0623` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0394` n `765`
- 4h: commodity avg `0.0533` n `12`; crypto_alt avg `-0.2803` n `229`; crypto_major avg `-0.4331` n `8`; equity avg `0.1863` n `92`; fx avg `-0.016` n `6`; index avg `0.1113` n `25`; metal avg `-0.0563` n `20`; unknown avg `-0.099` n `765`
- 24h: commodity avg `-0.2735` n `12`; crypto_alt avg `0.3759` n `229`; crypto_major avg `0.4675` n `8`; equity avg `-0.8824` n `92`; fx avg `-0.1801` n `6`; index avg `0.0263` n `25`; metal avg `-0.2003` n `20`; unknown avg `-0.2408` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal

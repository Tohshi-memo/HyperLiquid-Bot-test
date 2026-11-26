# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T13:22:29.034203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0689` n `13`; crypto_alt avg `-0.035` n `239`; crypto_major avg `0.0359` n `8`; equity avg `0.0486` n `168`; fx avg `-0.0072` n `6`; index avg `0.0109` n `27`; metal avg `0.0217` n `20`; unknown avg `0.1135` n `1265`
- 1h: commodity avg `0.0313` n `13`; crypto_alt avg `-0.016` n `239`; crypto_major avg `0.3556` n `8`; equity avg `0.1065` n `168`; fx avg `0.0015` n `6`; index avg `-0.0001` n `27`; metal avg `0.0075` n `20`; unknown avg `-0.014` n `1261`
- 4h: commodity avg `0.2246` n `13`; crypto_alt avg `0.0674` n `239`; crypto_major avg `0.0543` n `8`; equity avg `0.3859` n `168`; fx avg `0.0012` n `6`; index avg `0.0576` n `27`; metal avg `-0.0825` n `20`; unknown avg `1.9469` n `1249`
- 24h: commodity avg `0.297` n `13`; crypto_alt avg `4.61` n `239`; crypto_major avg `3.8793` n `8`; equity avg `4.4957` n `168`; fx avg `0.0777` n `6`; index avg `0.4252` n `27`; metal avg `0.7525` n `20`; unknown avg `426.395` n `1059`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal

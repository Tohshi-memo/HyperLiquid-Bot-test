# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T12:37:27.558102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0368` n `13`; crypto_alt avg `-0.1288` n `239`; crypto_major avg `-0.1065` n `8`; equity avg `-0.3455` n `162`; fx avg `-0.0126` n `6`; index avg `-0.016` n `27`; metal avg `-0.0756` n `20`; unknown avg `2.2949` n `1257`
- 1h: commodity avg `-0.0594` n `13`; crypto_alt avg `-0.3464` n `239`; crypto_major avg `-0.2821` n `8`; equity avg `-0.5521` n `162`; fx avg `-0.0314` n `6`; index avg `-0.0121` n `27`; metal avg `-0.0576` n `20`; unknown avg `22.4493` n `1243`
- 4h: commodity avg `-0.2597` n `13`; crypto_alt avg `-0.8111` n `239`; crypto_major avg `-0.9343` n `8`; equity avg `-0.5652` n `162`; fx avg `-0.0526` n `6`; index avg `0.0136` n `27`; metal avg `-0.2551` n `20`; unknown avg `20.6685` n `1249`
- 24h: commodity avg `-0.1818` n `13`; crypto_alt avg `-2.7345` n `239`; crypto_major avg `-1.8888` n `8`; equity avg `-2.1002` n `162`; fx avg `-0.1327` n `6`; index avg `-0.1197` n `27`; metal avg `-0.9203` n `20`; unknown avg `1.3725` n `1140`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal

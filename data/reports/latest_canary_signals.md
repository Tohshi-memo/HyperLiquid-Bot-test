# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T21:07:23.910680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `13`; crypto_alt avg `0.056` n `239`; crypto_major avg `0.1893` n `8`; equity avg `0.0271` n `166`; fx avg `-0.0029` n `6`; index avg `-0.0021` n `27`; metal avg `-0.0007` n `20`; unknown avg `-0.137` n `1238`
- 1h: commodity avg `0.0218` n `13`; crypto_alt avg `0.1734` n `239`; crypto_major avg `0.3404` n `8`; equity avg `0.0745` n `166`; fx avg `-0.0067` n `6`; index avg `0.0088` n `27`; metal avg `-0.0219` n `20`; unknown avg `201.0185` n `1244`
- 4h: commodity avg `-0.0055` n `13`; crypto_alt avg `-0.2366` n `239`; crypto_major avg `0.0189` n `8`; equity avg `0.0747` n `166`; fx avg `-0.0014` n `6`; index avg `-0.0193` n `27`; metal avg `-0.0778` n `20`; unknown avg `0.3736` n `1219`
- 24h: commodity avg `-0.1135` n `13`; crypto_alt avg `0.6624` n `239`; crypto_major avg `0.6894` n `8`; equity avg `0.8587` n `166`; fx avg `-0.004` n `6`; index avg `0.088` n `27`; metal avg `-0.0368` n `20`; unknown avg `235.4832` n `1062`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal

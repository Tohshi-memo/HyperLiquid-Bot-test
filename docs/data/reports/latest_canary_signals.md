# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T23:52:41.829529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `13`; crypto_alt avg `-0.1056` n `239`; crypto_major avg `-0.2564` n `8`; equity avg `-0.1435` n `166`; fx avg `-0.0016` n `6`; index avg `-0.0562` n `27`; metal avg `-0.0612` n `20`; unknown avg `158.1927` n `1266`
- 1h: commodity avg `0.0404` n `13`; crypto_alt avg `0.6015` n `239`; crypto_major avg `0.0822` n `8`; equity avg `-0.6173` n `166`; fx avg `-0.0098` n `6`; index avg `-0.1551` n `27`; metal avg `-0.0946` n `20`; unknown avg `0.0972` n `1256`
- 4h: commodity avg `0.1521` n `13`; crypto_alt avg `-0.6783` n `239`; crypto_major avg `-0.8034` n `8`; equity avg `0.3102` n `166`; fx avg `0.0012` n `6`; index avg `-0.0215` n `27`; metal avg `-0.0735` n `20`; unknown avg `164.848` n `1214`
- 24h: commodity avg `-1.0672` n `13`; crypto_alt avg `0.7082` n `239`; crypto_major avg `0.4899` n `8`; equity avg `5.3661` n `166`; fx avg `-0.1856` n `6`; index avg `0.4239` n `27`; metal avg `0.1563` n `20`; unknown avg `1.9615` n `1045`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal

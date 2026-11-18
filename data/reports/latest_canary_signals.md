# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T18:52:27.805020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0821` n `13`; crypto_alt avg `0.2075` n `239`; crypto_major avg `-0.0973` n `8`; equity avg `-0.1096` n `164`; fx avg `0.0031` n `6`; index avg `-0.0102` n `27`; metal avg `-0.0184` n `20`; unknown avg `0.0504` n `1265`
- 1h: commodity avg `0.1812` n `13`; crypto_alt avg `0.2456` n `239`; crypto_major avg `0.2628` n `8`; equity avg `0.0164` n `164`; fx avg `0.0107` n `6`; index avg `0.0079` n `27`; metal avg `0.11` n `20`; unknown avg `0.7709` n `1263`
- 4h: commodity avg `0.0415` n `13`; crypto_alt avg `-0.3424` n `239`; crypto_major avg `-0.2807` n `8`; equity avg `0.4311` n `164`; fx avg `-0.0115` n `6`; index avg `0.0576` n `27`; metal avg `-0.0476` n `20`; unknown avg `2.2063` n `1257`
- 24h: commodity avg `-0.4288` n `13`; crypto_alt avg `0.6927` n `239`; crypto_major avg `0.0091` n `8`; equity avg `0.676` n `164`; fx avg `-0.1759` n `6`; index avg `0.0907` n `27`; metal avg `-1.1` n `20`; unknown avg `0.1257` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal

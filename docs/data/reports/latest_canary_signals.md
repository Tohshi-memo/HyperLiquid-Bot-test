# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T07:22:22.965306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.0023` n `239`; crypto_major avg `0.0267` n `8`; equity avg `-0.0067` n `166`; fx avg `-0.0132` n `6`; index avg `0.0029` n `27`; metal avg `0.0023` n `20`; unknown avg `-0.0045` n `1261`
- 1h: commodity avg `-0.0444` n `13`; crypto_alt avg `-0.108` n `239`; crypto_major avg `0.1904` n `8`; equity avg `-0.0215` n `166`; fx avg `-0.0081` n `6`; index avg `0.0031` n `27`; metal avg `0.0134` n `20`; unknown avg `0.2437` n `1255`
- 4h: commodity avg `-0.0402` n `13`; crypto_alt avg `-0.0725` n `239`; crypto_major avg `-0.2945` n `8`; equity avg `-0.1641` n `166`; fx avg `-0.0122` n `6`; index avg `0.0049` n `27`; metal avg `0.0126` n `20`; unknown avg `1.2909` n `1223`
- 24h: commodity avg `-0.0246` n `13`; crypto_alt avg `1.0683` n `239`; crypto_major avg `1.4983` n `8`; equity avg `0.4518` n `166`; fx avg `0.0538` n `6`; index avg `0.0901` n `27`; metal avg `0.0421` n `20`; unknown avg `235.0763` n `1072`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal

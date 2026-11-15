# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T10:22:27.666555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5492` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0107` n `13`; crypto_alt avg `0.16` n `239`; crypto_major avg `0.0215` n `8`; equity avg `0.0131` n `162`; fx avg `0.0031` n `6`; index avg `0.0007` n `27`; metal avg `0.0036` n `20`; unknown avg `0.1328` n `1261`
- 1h: commodity avg `-0.0193` n `13`; crypto_alt avg `0.0522` n `239`; crypto_major avg `0.021` n `8`; equity avg `-0.0522` n `162`; fx avg `0.0104` n `6`; index avg `-0.0005` n `27`; metal avg `0.0063` n `20`; unknown avg `-0.0263` n `1261`
- 4h: commodity avg `-0.056` n `13`; crypto_alt avg `0.946` n `239`; crypto_major avg `1.7291` n `8`; equity avg `0.369` n `162`; fx avg `-0.0187` n `6`; index avg `0.0411` n `27`; metal avg `0.1799` n `20`; unknown avg `0.4158` n `1243`
- 24h: commodity avg `0.0138` n `13`; crypto_alt avg `-3.8841` n `239`; crypto_major avg `-3.0916` n `8`; equity avg `-0.7266` n `162`; fx avg `0.0385` n `6`; index avg `-0.0608` n `27`; metal avg `-0.3354` n `20`; unknown avg `44.3644` n `1128`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal

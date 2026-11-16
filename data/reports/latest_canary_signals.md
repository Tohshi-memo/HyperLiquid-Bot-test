# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T07:52:38.695369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `13`; crypto_alt avg `-0.1039` n `239`; crypto_major avg `-0.1214` n `8`; equity avg `0.0352` n `162`; fx avg `0.0005` n `6`; index avg `0.0043` n `27`; metal avg `-0.0828` n `20`; unknown avg `0.2352` n `1265`
- 1h: commodity avg `-0.1001` n `13`; crypto_alt avg `0.0527` n `239`; crypto_major avg `0.2247` n `8`; equity avg `0.108` n `162`; fx avg `0.0045` n `6`; index avg `0.0239` n `27`; metal avg `0.004` n `20`; unknown avg `85.3148` n `1179`
- 4h: commodity avg `0.0967` n `13`; crypto_alt avg `-0.3234` n `239`; crypto_major avg `-0.1532` n `8`; equity avg `-0.5187` n `162`; fx avg `-0.0429` n `6`; index avg `-0.0417` n `27`; metal avg `-0.1189` n `20`; unknown avg `89.9936` n `1115`
- 24h: commodity avg `-0.299` n `13`; crypto_alt avg `0.6855` n `239`; crypto_major avg `1.8975` n `8`; equity avg `-0.0711` n `162`; fx avg `-0.0618` n `6`; index avg `-0.0218` n `27`; metal avg `0.0553` n `20`; unknown avg `0.7075` n `1075`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T13:07:24.040376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0453` n `13`; crypto_alt avg `0.1955` n `239`; crypto_major avg `0.317` n `8`; equity avg `0.1821` n `162`; fx avg `0.0214` n `6`; index avg `0.0212` n `27`; metal avg `0.0219` n `20`; unknown avg `0.2573` n `1259`
- 1h: commodity avg `-0.084` n `13`; crypto_alt avg `-0.4685` n `239`; crypto_major avg `-0.2086` n `8`; equity avg `-0.0215` n `162`; fx avg `0.0244` n `6`; index avg `0.0209` n `27`; metal avg `0.0106` n `20`; unknown avg `0.6436` n `1261`
- 4h: commodity avg `-0.1007` n `13`; crypto_alt avg `-0.2043` n `239`; crypto_major avg `0.0243` n `8`; equity avg `-0.6109` n `162`; fx avg `-0.0065` n `6`; index avg `-0.0685` n `27`; metal avg `0.0604` n `20`; unknown avg `0.2415` n `1253`
- 24h: commodity avg `-0.5519` n `13`; crypto_alt avg `-2.1647` n `239`; crypto_major avg `-1.9168` n `8`; equity avg `-1.4458` n `162`; fx avg `-0.0282` n `6`; index avg `-0.0981` n `27`; metal avg `0.0709` n `20`; unknown avg `22.4326` n `1054`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal

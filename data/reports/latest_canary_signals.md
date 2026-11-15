# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T10:52:27.553825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `-0.0975` n `239`; crypto_major avg `-0.0382` n `8`; equity avg `0.0105` n `162`; fx avg `-0.0069` n `6`; index avg `0.0004` n `27`; metal avg `-0.0064` n `20`; unknown avg `0.0192` n `1265`
- 1h: commodity avg `0.0117` n `13`; crypto_alt avg `0.1062` n `239`; crypto_major avg `0.1665` n `8`; equity avg `0.0274` n `162`; fx avg `-0.0059` n `6`; index avg `0.0005` n `27`; metal avg `-0.0081` n `20`; unknown avg `-0.0694` n `1261`
- 4h: commodity avg `-0.0698` n `13`; crypto_alt avg `0.7128` n `239`; crypto_major avg `1.5865` n `8`; equity avg `0.3221` n `162`; fx avg `-0.0261` n `6`; index avg `0.0396` n `27`; metal avg `0.1475` n `20`; unknown avg `0.7698` n `1245`
- 24h: commodity avg `0.008` n `13`; crypto_alt avg `-3.768` n `239`; crypto_major avg `-3.2465` n `8`; equity avg `-0.7444` n `162`; fx avg `0.0296` n `6`; index avg `-0.0558` n `27`; metal avg `-0.3569` n `20`; unknown avg `-0.5806` n `1134`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal

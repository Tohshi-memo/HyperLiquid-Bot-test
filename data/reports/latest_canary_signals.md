# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T01:22:26.107453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0618` n `12`; crypto_alt avg `0.0987` n `230`; crypto_major avg `-0.0055` n `8`; equity avg `0.1604` n `92`; fx avg `-0.0056` n `6`; index avg `0.0227` n `25`; metal avg `0.0104` n `20`; unknown avg `0.0351` n `768`
- 1h: commodity avg `-0.1081` n `12`; crypto_alt avg `0.0489` n `230`; crypto_major avg `-0.1906` n `8`; equity avg `-0.1907` n `92`; fx avg `-0.0069` n `6`; index avg `-0.0655` n `25`; metal avg `0.0329` n `20`; unknown avg `0.18` n `768`
- 4h: commodity avg `0.0133` n `12`; crypto_alt avg `0.2998` n `230`; crypto_major avg `-0.1552` n `8`; equity avg `0.466` n `92`; fx avg `0.0229` n `6`; index avg `0.0773` n `25`; metal avg `0.0708` n `20`; unknown avg `0.5759` n `766`
- 24h: commodity avg `0.1093` n `12`; crypto_alt avg `1.631` n `230`; crypto_major avg `2.76` n `8`; equity avg `1.5685` n `92`; fx avg `0.0852` n `6`; index avg `0.4371` n `25`; metal avg `0.7356` n `20`; unknown avg `0.1239` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal

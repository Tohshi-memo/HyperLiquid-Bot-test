# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T10:37:28.410894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.048` n `12`; crypto_alt avg `-0.0203` n `230`; crypto_major avg `0.0073` n `8`; equity avg `0.2234` n `96`; fx avg `-0.0177` n `6`; index avg `0.052` n `25`; metal avg `-0.0283` n `20`; unknown avg `0.0282` n `769`
- 1h: commodity avg `-0.0065` n `12`; crypto_alt avg `0.1872` n `230`; crypto_major avg `0.1873` n `8`; equity avg `0.9112` n `96`; fx avg `-0.0362` n `6`; index avg `0.1428` n `25`; metal avg `-0.0309` n `20`; unknown avg `0.0765` n `769`
- 4h: commodity avg `0.2884` n `12`; crypto_alt avg `0.0839` n `230`; crypto_major avg `0.239` n `8`; equity avg `0.5994` n `96`; fx avg `-0.012` n `6`; index avg `0.0662` n `25`; metal avg `-0.0202` n `20`; unknown avg `0.1608` n `768`
- 24h: commodity avg `0.0191` n `12`; crypto_alt avg `-1.4113` n `230`; crypto_major avg `-2.5719` n `8`; equity avg `-4.3434` n `94`; fx avg `-0.0267` n `6`; index avg `-0.5885` n `25`; metal avg `-0.7237` n `20`; unknown avg `-0.395` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal

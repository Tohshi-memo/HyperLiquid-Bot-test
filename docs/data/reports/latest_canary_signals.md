# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T19:52:31.255487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0304` n `12`; crypto_alt avg `0.0941` n `233`; crypto_major avg `0.0425` n `8`; equity avg `-0.1076` n `136`; fx avg `0.0001` n `6`; index avg `-0.0188` n `27`; metal avg `-0.0672` n `20`; unknown avg `1.1755` n `908`
- 1h: commodity avg `0.1519` n `12`; crypto_alt avg `-0.353` n `233`; crypto_major avg `-0.4337` n `8`; equity avg `-0.4337` n `136`; fx avg `0.0132` n `6`; index avg `-0.0847` n `27`; metal avg `-0.1658` n `20`; unknown avg `9.1075` n `906`
- 4h: commodity avg `-0.2182` n `12`; crypto_alt avg `0.8211` n `233`; crypto_major avg `1.0936` n `8`; equity avg `-0.1444` n `136`; fx avg `0.0151` n `6`; index avg `-0.0195` n `27`; metal avg `-0.077` n `20`; unknown avg `0.8963` n `878`
- 24h: commodity avg `0.1434` n `12`; crypto_alt avg `0.5532` n `233`; crypto_major avg `2.4563` n `8`; equity avg `-0.5798` n `136`; fx avg `0.0639` n `6`; index avg `-0.1767` n `27`; metal avg `-0.4643` n `20`; unknown avg `3.9052` n `696`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal

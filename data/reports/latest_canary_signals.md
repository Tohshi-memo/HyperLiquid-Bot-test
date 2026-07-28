# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T03:52:30.156242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.0677` n `230`; crypto_major avg `0.0638` n `8`; equity avg `0.0573` n `102`; fx avg `0.0222` n `6`; index avg `0.0305` n `25`; metal avg `0.0056` n `20`; unknown avg `0.0286` n `774`
- 1h: commodity avg `0.1492` n `12`; crypto_alt avg `0.0887` n `230`; crypto_major avg `0.2229` n `8`; equity avg `0.2906` n `102`; fx avg `0.0306` n `6`; index avg `0.0631` n `25`; metal avg `0.0657` n `20`; unknown avg `0.0527` n `774`
- 4h: commodity avg `-0.1694` n `12`; crypto_alt avg `-0.0769` n `230`; crypto_major avg `-0.3444` n `8`; equity avg `-1.2098` n `102`; fx avg `0.0153` n `6`; index avg `-0.2475` n `25`; metal avg `-0.247` n `20`; unknown avg `0.3626` n `774`
- 24h: commodity avg `-0.8556` n `12`; crypto_alt avg `-3.7797` n `230`; crypto_major avg `-3.2806` n `8`; equity avg `-3.0608` n `102`; fx avg `-0.1074` n `6`; index avg `-0.6349` n `25`; metal avg `-0.2425` n `20`; unknown avg `1161.8879` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1836`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal

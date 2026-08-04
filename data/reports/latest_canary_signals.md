# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T04:52:29.623946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `12`; crypto_alt avg `0.1176` n `230`; crypto_major avg `0.1722` n `8`; equity avg `0.1378` n `107`; fx avg `-0.0057` n `6`; index avg `0.0162` n `25`; metal avg `-0.0001` n `20`; unknown avg `1.2409` n `781`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `0.1081` n `230`; crypto_major avg `0.2389` n `8`; equity avg `0.0929` n `107`; fx avg `0.0047` n `6`; index avg `0.017` n `25`; metal avg `0.0656` n `20`; unknown avg `3.3324` n `781`
- 4h: commodity avg `0.0422` n `12`; crypto_alt avg `0.7062` n `230`; crypto_major avg `0.9293` n `8`; equity avg `0.6973` n `107`; fx avg `0.09` n `6`; index avg `0.0958` n `25`; metal avg `0.2713` n `20`; unknown avg `1.2367` n `780`
- 24h: commodity avg `0.3694` n `12`; crypto_alt avg `1.3667` n `230`; crypto_major avg `1.4212` n `8`; equity avg `1.7387` n `107`; fx avg `0.0331` n `6`; index avg `0.1169` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.2067` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal

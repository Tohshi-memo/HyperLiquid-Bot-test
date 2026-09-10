# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T02:22:35.138285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `-0.2265` n `233`; crypto_major avg `-0.0772` n `8`; equity avg `-0.0205` n `134`; fx avg `0.011` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0358` n `20`; unknown avg `1.3397` n `797`
- 1h: commodity avg `-0.0542` n `12`; crypto_alt avg `-0.5075` n `233`; crypto_major avg `-0.0442` n `8`; equity avg `-0.0027` n `134`; fx avg `-0.0181` n `6`; index avg `0.043` n `26`; metal avg `-0.005` n `20`; unknown avg `1.7079` n `795`
- 4h: commodity avg `-0.1369` n `12`; crypto_alt avg `-0.4879` n `233`; crypto_major avg `-0.1329` n `8`; equity avg `-0.401` n `134`; fx avg `-0.0037` n `6`; index avg `-0.0265` n `26`; metal avg `0.0091` n `20`; unknown avg `1.4515` n `779`
- 24h: commodity avg `-0.0058` n `12`; crypto_alt avg `-3.5563` n `233`; crypto_major avg `-2.3118` n `8`; equity avg `-1.4384` n `134`; fx avg `-0.0256` n `6`; index avg `-0.2466` n `26`; metal avg `0.4397` n `20`; unknown avg `2.1545` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal

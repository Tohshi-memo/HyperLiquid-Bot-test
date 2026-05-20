# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T09:07:22.159726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.083` n `12`; crypto_alt avg `-0.035` n `228`; crypto_major avg `-0.0917` n `8`; equity avg `-0.1172` n `66`; fx avg `-0.0056` n `6`; index avg `-0.0363` n `23`; metal avg `-0.1233` n `18`; unknown avg `-0.3041` n `384`
- 1h: commodity avg `-0.2633` n `12`; crypto_alt avg `-0.0596` n `228`; crypto_major avg `-0.0055` n `8`; equity avg `0.0374` n `66`; fx avg `-0.0405` n `6`; index avg `0.1751` n `23`; metal avg `0.1174` n `18`; unknown avg `0.3201` n `384`
- 4h: commodity avg `-0.6724` n `12`; crypto_alt avg `0.6845` n `228`; crypto_major avg `0.5606` n `8`; equity avg `0.771` n `66`; fx avg `-0.0901` n `6`; index avg `0.4185` n `23`; metal avg `0.8337` n `18`; unknown avg `0.6021` n `374`
- 24h: commodity avg `-0.2973` n `12`; crypto_alt avg `0.1739` n `228`; crypto_major avg `-0.1308` n `8`; equity avg `0.8386` n `66`; fx avg `-0.1482` n `6`; index avg `-0.1317` n `23`; metal avg `-0.6876` n `18`; unknown avg `0.5805` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal

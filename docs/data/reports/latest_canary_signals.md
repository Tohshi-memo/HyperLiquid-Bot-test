# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T04:37:30.448049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `0.1158` n `232`; crypto_major avg `0.1324` n `8`; equity avg `-0.063` n `134`; fx avg `0.0135` n `6`; index avg `-0.0163` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.3692` n `791`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `-0.0287` n `232`; crypto_major avg `0.0066` n `8`; equity avg `-0.0725` n `134`; fx avg `0.0559` n `6`; index avg `-0.0273` n `26`; metal avg `0.0467` n `20`; unknown avg `0.3429` n `789`
- 4h: commodity avg `0.062` n `12`; crypto_alt avg `-0.2153` n `232`; crypto_major avg `-0.437` n `8`; equity avg `0.299` n `134`; fx avg `-0.0091` n `6`; index avg `0.0826` n `26`; metal avg `0.0806` n `20`; unknown avg `0.8288` n `783`
- 24h: commodity avg `0.1312` n `12`; crypto_alt avg `0.7821` n `232`; crypto_major avg `-0.7496` n `8`; equity avg `0.6542` n `134`; fx avg `-0.2893` n `6`; index avg `0.1917` n `26`; metal avg `0.4389` n `20`; unknown avg `7376.0613` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal

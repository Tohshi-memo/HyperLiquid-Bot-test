# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T16:22:28.867690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.3607` n `234`; crypto_major avg `0.2329` n `8`; equity avg `0.0682` n `140`; fx avg `0.0176` n `6`; index avg `0.0201` n `26`; metal avg `0.0141` n `20`; unknown avg `0.6122` n `935`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `1.1386` n `234`; crypto_major avg `0.6889` n `8`; equity avg `0.1936` n `140`; fx avg `0.0297` n `6`; index avg `0.0251` n `26`; metal avg `0.0099` n `20`; unknown avg `0.3925` n `889`
- 4h: commodity avg `-0.0058` n `12`; crypto_alt avg `1.4072` n `234`; crypto_major avg `1.0287` n `8`; equity avg `0.2375` n `140`; fx avg `0.0175` n `6`; index avg `0.0297` n `26`; metal avg `0.0105` n `20`; unknown avg `1.2884` n `889`
- 24h: commodity avg `0.4374` n `12`; crypto_alt avg `-0.9557` n `234`; crypto_major avg `-1.4889` n `8`; equity avg `-0.0639` n `140`; fx avg `-0.023` n `6`; index avg `-0.0363` n `26`; metal avg `-0.0109` n `20`; unknown avg `168.2711` n `795`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal

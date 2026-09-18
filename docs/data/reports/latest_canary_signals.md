# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T09:37:36.113829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0906` n `12`; crypto_alt avg `-0.0893` n `234`; crypto_major avg `-0.2753` n `8`; equity avg `-0.1729` n `140`; fx avg `0.0555` n `6`; index avg `-0.0261` n `26`; metal avg `-0.0673` n `20`; unknown avg `13.3184` n `927`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.2784` n `234`; crypto_major avg `0.2567` n `8`; equity avg `-0.2224` n `140`; fx avg `0.0348` n `6`; index avg `-0.0388` n `26`; metal avg `-0.0119` n `20`; unknown avg `13.1836` n `925`
- 4h: commodity avg `-0.0573` n `12`; crypto_alt avg `0.9457` n `234`; crypto_major avg `0.5883` n `8`; equity avg `0.1388` n `140`; fx avg `0.0972` n `6`; index avg `0.0133` n `26`; metal avg `0.1929` n `20`; unknown avg `9.8063` n `863`
- 24h: commodity avg `-0.2847` n `12`; crypto_alt avg `5.2645` n `234`; crypto_major avg `3.7325` n `8`; equity avg `1.6388` n `140`; fx avg `0.2114` n `6`; index avg `0.2415` n `26`; metal avg `0.7074` n `20`; unknown avg `4.4017` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal

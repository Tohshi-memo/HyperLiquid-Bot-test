# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T21:07:34.093288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `-0.0978` n `232`; crypto_major avg `-0.0586` n `8`; equity avg `-0.008` n `129`; fx avg `0.0154` n `6`; index avg `0.0228` n `26`; metal avg `0.0006` n `20`; unknown avg `0.7921` n `785`
- 1h: commodity avg `0.0668` n `12`; crypto_alt avg `-0.0184` n `232`; crypto_major avg `-0.0982` n `8`; equity avg `0.034` n `129`; fx avg `0.0061` n `6`; index avg `0.0241` n `26`; metal avg `-0.0335` n `20`; unknown avg `0.9503` n `773`
- 4h: commodity avg `0.0772` n `12`; crypto_alt avg `0.3132` n `232`; crypto_major avg `0.371` n `8`; equity avg `0.3641` n `129`; fx avg `0.0194` n `6`; index avg `0.0742` n `26`; metal avg `0.0695` n `20`; unknown avg `0.1487` n `773`
- 24h: commodity avg `0.2382` n `12`; crypto_alt avg `-0.0525` n `231`; crypto_major avg `0.0666` n `8`; equity avg `0.1086` n `129`; fx avg `-0.0911` n `6`; index avg `-0.0937` n `26`; metal avg `-0.4136` n `20`; unknown avg `0.1002` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal

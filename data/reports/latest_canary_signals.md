# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T02:22:26.529159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `-0.1176` n `230`; crypto_major avg `-0.1337` n `8`; equity avg `0.0396` n `113`; fx avg `0.0046` n `6`; index avg `0.0023` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.0355` n `787`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `0.0737` n `230`; crypto_major avg `-0.0693` n `8`; equity avg `-0.0277` n `113`; fx avg `-0.0201` n `6`; index avg `0.0168` n `25`; metal avg `-0.0377` n `20`; unknown avg `-0.019` n `787`
- 4h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.0055` n `230`; crypto_major avg `-0.1824` n `8`; equity avg `-0.3661` n `113`; fx avg `-0.0403` n `6`; index avg `-0.0511` n `25`; metal avg `-0.2013` n `20`; unknown avg `0.6919` n `787`
- 24h: commodity avg `-0.3279` n `12`; crypto_alt avg `0.3692` n `230`; crypto_major avg `0.4676` n `8`; equity avg `0.7719` n `113`; fx avg `0.0147` n `6`; index avg `0.2189` n `25`; metal avg `-0.6887` n `20`; unknown avg `1.1456` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2452`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.208`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal

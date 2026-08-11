# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T20:22:28.381169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `-0.0838` n `230`; crypto_major avg `-0.0758` n `8`; equity avg `0.2935` n `113`; fx avg `-0.0063` n `6`; index avg `0.0267` n `25`; metal avg `-0.0109` n `20`; unknown avg `0.0058` n `785`
- 1h: commodity avg `-0.053` n `12`; crypto_alt avg `0.3993` n `230`; crypto_major avg `0.6906` n `8`; equity avg `0.4467` n `113`; fx avg `-0.0081` n `6`; index avg `0.0542` n `25`; metal avg `0.0366` n `20`; unknown avg `0.4907` n `785`
- 4h: commodity avg `0.0885` n `12`; crypto_alt avg `0.3993` n `230`; crypto_major avg `0.7416` n `8`; equity avg `0.458` n `113`; fx avg `0.0006` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0888` n `20`; unknown avg `0.2879` n `785`
- 24h: commodity avg `0.1144` n `12`; crypto_alt avg `-1.5243` n `230`; crypto_major avg `0.165` n `8`; equity avg `1.0076` n `113`; fx avg `-0.0774` n `6`; index avg `0.1301` n `25`; metal avg `-0.204` n `20`; unknown avg `-0.2621` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2053`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal

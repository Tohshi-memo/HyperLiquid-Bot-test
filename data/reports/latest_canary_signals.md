# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T23:52:24.876316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `0.0012` n `230`; crypto_major avg `-0.0026` n `8`; equity avg `0.0452` n `113`; fx avg `-0.0011` n `6`; index avg `0.0118` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.0526` n `786`
- 1h: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.0496` n `230`; crypto_major avg `0.07` n `8`; equity avg `0.0767` n `113`; fx avg `-0.0014` n `6`; index avg `0.0098` n `25`; metal avg `-0.0149` n `20`; unknown avg `-0.0207` n `786`
- 4h: commodity avg `-0.0549` n `12`; crypto_alt avg `0.2737` n `230`; crypto_major avg `0.6475` n `8`; equity avg `0.6075` n `113`; fx avg `-0.008` n `6`; index avg `0.0395` n `25`; metal avg `0.0108` n `20`; unknown avg `0.1166` n `785`
- 24h: commodity avg `0.1415` n `12`; crypto_alt avg `-1.1692` n `230`; crypto_major avg `0.8004` n `8`; equity avg `1.5632` n `113`; fx avg `-0.064` n `6`; index avg `0.1465` n `25`; metal avg `-0.2209` n `20`; unknown avg `-0.0675` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.223`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2156`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal

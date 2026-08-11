# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T19:22:28.103705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0416` n `12`; crypto_alt avg `0.1101` n `230`; crypto_major avg `0.0813` n `8`; equity avg `0.1836` n `113`; fx avg `0.0041` n `6`; index avg `0.0167` n `25`; metal avg `0.0107` n `20`; unknown avg `0.1982` n `785`
- 1h: commodity avg `0.071` n `12`; crypto_alt avg `0.0042` n `230`; crypto_major avg `-0.1513` n `8`; equity avg `0.1331` n `113`; fx avg `0.0085` n `6`; index avg `0.0041` n `25`; metal avg `0.0293` n `20`; unknown avg `-0.0655` n `785`
- 4h: commodity avg `0.198` n `12`; crypto_alt avg `-0.4602` n `230`; crypto_major avg `-0.0738` n `8`; equity avg `-0.261` n `113`; fx avg `0.0109` n `6`; index avg `-0.101` n `25`; metal avg `-0.1422` n `20`; unknown avg `-0.1342` n `785`
- 24h: commodity avg `0.2168` n `12`; crypto_alt avg `-1.9152` n `230`; crypto_major avg `-0.389` n `8`; equity avg `0.1703` n `113`; fx avg `-0.0552` n `6`; index avg `0.0293` n `25`; metal avg `-0.2655` n `20`; unknown avg `-0.2886` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2002`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal

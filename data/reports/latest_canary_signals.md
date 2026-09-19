# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T03:52:27.922124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `0.0688` n `234`; crypto_major avg `0.0663` n `8`; equity avg `0.0032` n `140`; fx avg `0.0013` n `6`; index avg `-0.011` n `26`; metal avg `0.0055` n `20`; unknown avg `1.2803` n `942`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.1544` n `234`; crypto_major avg `-0.1697` n `8`; equity avg `-0.0292` n `140`; fx avg `0.0057` n `6`; index avg `-0.0012` n `26`; metal avg `0.0006` n `20`; unknown avg `3.0422` n `938`
- 4h: commodity avg `-0.0182` n `12`; crypto_alt avg `0.6374` n `234`; crypto_major avg `0.6172` n `8`; equity avg `-0.1171` n `140`; fx avg `-0.0177` n `6`; index avg `-0.004` n `26`; metal avg `-0.0199` n `20`; unknown avg `0.392` n `932`
- 24h: commodity avg `0.1374` n `12`; crypto_alt avg `4.1494` n `234`; crypto_major avg `4.8363` n `8`; equity avg `0.6963` n `140`; fx avg `0.0325` n `6`; index avg `0.021` n `26`; metal avg `0.0819` n `20`; unknown avg `3.9376` n `785`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal

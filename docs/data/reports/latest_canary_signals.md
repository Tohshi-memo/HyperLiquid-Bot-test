# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T10:07:28.058404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `0.0674` n `230`; crypto_major avg `0.0482` n `8`; equity avg `0.0388` n `113`; fx avg `0.0082` n `6`; index avg `0.0047` n `25`; metal avg `0.0146` n `20`; unknown avg `-0.0172` n `786`
- 1h: commodity avg `-0.1` n `12`; crypto_alt avg `0.3904` n `230`; crypto_major avg `0.4902` n `8`; equity avg `0.0776` n `113`; fx avg `-0.0266` n `6`; index avg `0.0125` n `25`; metal avg `0.1156` n `20`; unknown avg `0.0323` n `786`
- 4h: commodity avg `-0.1448` n `12`; crypto_alt avg `-0.2176` n `230`; crypto_major avg `0.4935` n `8`; equity avg `0.5987` n `113`; fx avg `-0.0132` n `6`; index avg `0.0953` n `25`; metal avg `0.2949` n `20`; unknown avg `-0.0915` n `786`
- 24h: commodity avg `-0.1836` n `12`; crypto_alt avg `-1.0784` n `230`; crypto_major avg `0.8441` n `8`; equity avg `2.6857` n `113`; fx avg `-0.013` n `6`; index avg `0.2727` n `25`; metal avg `0.239` n `20`; unknown avg `-0.2011` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2361`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2263`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2047`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T06:22:25.373892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0916` n `12`; crypto_alt avg `-0.0039` n `233`; crypto_major avg `-0.0043` n `8`; equity avg `0.002` n `136`; fx avg `-0.0155` n `6`; index avg `-0.0032` n `26`; metal avg `0.0127` n `20`; unknown avg `4.2773` n `796`
- 1h: commodity avg `-0.1087` n `12`; crypto_alt avg `0.1041` n `233`; crypto_major avg `0.2092` n `8`; equity avg `0.4206` n `136`; fx avg `-0.0011` n `6`; index avg `0.0634` n `26`; metal avg `0.1765` n `20`; unknown avg `4.9885` n `772`
- 4h: commodity avg `-0.255` n `12`; crypto_alt avg `0.8422` n `233`; crypto_major avg `0.6348` n `8`; equity avg `0.4486` n `136`; fx avg `-0.0382` n `6`; index avg `0.1122` n `26`; metal avg `0.2999` n `20`; unknown avg `30.588` n `764`
- 24h: commodity avg `0.9816` n `12`; crypto_alt avg `-1.1614` n `233`; crypto_major avg `-1.4593` n `8`; equity avg `-1.4585` n `136`; fx avg `0.068` n `6`; index avg `-0.2721` n `26`; metal avg `-0.9999` n `20`; unknown avg `2.6824` n `685`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal

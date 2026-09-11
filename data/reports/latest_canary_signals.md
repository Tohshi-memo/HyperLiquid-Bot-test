# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T20:07:26.359051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0377` n `12`; crypto_alt avg `0.4199` n `233`; crypto_major avg `0.3301` n `8`; equity avg `0.0225` n `136`; fx avg `-0.0051` n `6`; index avg `-0.0132` n `26`; metal avg `0.0369` n `20`; unknown avg `0.9407` n `810`
- 1h: commodity avg `-0.0277` n `12`; crypto_alt avg `0.8164` n `233`; crypto_major avg `0.6767` n `8`; equity avg `-0.0102` n `136`; fx avg `-0.0031` n `6`; index avg `-0.0023` n `26`; metal avg `0.0434` n `20`; unknown avg `3.3913` n `792`
- 4h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.8275` n `233`; crypto_major avg `-0.6926` n `8`; equity avg `-0.4127` n `136`; fx avg `0.007` n `6`; index avg `-0.055` n `26`; metal avg `-0.0579` n `20`; unknown avg `0.0919` n `740`
- 24h: commodity avg `-0.5466` n `12`; crypto_alt avg `0.714` n `233`; crypto_major avg `1.367` n `8`; equity avg `0.8046` n `136`; fx avg `-0.158` n `6`; index avg `0.3083` n `26`; metal avg `0.2884` n `20`; unknown avg `1.0348` n `670`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal

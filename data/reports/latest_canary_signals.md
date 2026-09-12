# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T06:28:32.401997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0222` n `12`; crypto_alt avg `0.2421` n `233`; crypto_major avg `0.0544` n `8`; equity avg `0.0009` n `136`; fx avg `0.0012` n `6`; index avg `-0.0015` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.0036` n `836`
- 1h: commodity avg `-0.0211` n `12`; crypto_alt avg `0.2613` n `233`; crypto_major avg `0.0433` n `8`; equity avg `-0.045` n `136`; fx avg `-0.0049` n `6`; index avg `0.0072` n `26`; metal avg `0.0011` n `20`; unknown avg `2.1719` n `810`
- 4h: commodity avg `-0.0982` n `12`; crypto_alt avg `0.0471` n `233`; crypto_major avg `-0.0937` n `8`; equity avg `-0.0968` n `136`; fx avg `-0.0104` n `6`; index avg `0.0083` n `26`; metal avg `0.0005` n `20`; unknown avg `2.3103` n `796`
- 24h: commodity avg `-0.493` n `12`; crypto_alt avg `0.8933` n `233`; crypto_major avg `0.6823` n `8`; equity avg `0.3364` n `136`; fx avg `-0.1293` n `6`; index avg `0.1876` n `26`; metal avg `-0.0713` n `20`; unknown avg `1.1267` n `692`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal

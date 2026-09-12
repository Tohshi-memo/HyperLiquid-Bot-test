# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T06:22:30.513528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0173` n `12`; crypto_alt avg `0.2027` n `233`; crypto_major avg `0.0631` n `8`; equity avg `-0.0035` n `136`; fx avg `0.0006` n `6`; index avg `0.0004` n `26`; metal avg `0.0042` n `20`; unknown avg `0.0864` n `836`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `0.2218` n `233`; crypto_major avg `0.0521` n `8`; equity avg `-0.0494` n `136`; fx avg `-0.0055` n `6`; index avg `0.0091` n `26`; metal avg `-0.0028` n `20`; unknown avg `2.2289` n `810`
- 4h: commodity avg `-0.0933` n `12`; crypto_alt avg `0.0078` n `233`; crypto_major avg `-0.0848` n `8`; equity avg `-0.1012` n `136`; fx avg `-0.011` n `6`; index avg `0.0102` n `26`; metal avg `-0.0034` n `20`; unknown avg `2.4061` n `796`
- 24h: commodity avg `-0.4881` n `12`; crypto_alt avg `0.8534` n `233`; crypto_major avg `0.6914` n `8`; equity avg `0.3321` n `136`; fx avg `-0.1299` n `6`; index avg `0.1895` n `26`; metal avg `-0.0752` n `20`; unknown avg `1.1401` n `692`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal

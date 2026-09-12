# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T08:07:26.731898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0179` n `12`; crypto_alt avg `0.0437` n `233`; crypto_major avg `0.0681` n `8`; equity avg `-0.0021` n `136`; fx avg `-0.0025` n `6`; index avg `-0.005` n `26`; metal avg `0.0004` n `20`; unknown avg `0.7244` n `836`
- 1h: commodity avg `0.0084` n `12`; crypto_alt avg `0.3484` n `233`; crypto_major avg `0.1815` n `8`; equity avg `0.0241` n `136`; fx avg `-0.0023` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.7788` n `836`
- 4h: commodity avg `-0.0698` n `12`; crypto_alt avg `0.6082` n `233`; crypto_major avg `0.2251` n `8`; equity avg `-0.0553` n `136`; fx avg `-0.0092` n `6`; index avg `0.0026` n `26`; metal avg `0.0198` n `20`; unknown avg `-0.0801` n `800`
- 24h: commodity avg `-0.4108` n `12`; crypto_alt avg `1.6774` n `233`; crypto_major avg `1.1735` n `8`; equity avg `0.3726` n `136`; fx avg `-0.137` n `6`; index avg `0.1832` n `26`; metal avg `-0.0156` n `20`; unknown avg `0.8254` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal

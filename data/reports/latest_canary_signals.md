# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T10:07:26.039461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0233` n `12`; crypto_alt avg `0.1229` n `233`; crypto_major avg `0.211` n `8`; equity avg `0.0311` n `136`; fx avg `-0.0014` n `6`; index avg `0.002` n `26`; metal avg `0.0011` n `20`; unknown avg `0.0072` n `836`
- 1h: commodity avg `0.0624` n `12`; crypto_alt avg `0.0752` n `233`; crypto_major avg `0.1999` n `8`; equity avg `0.0089` n `136`; fx avg `-0.0065` n `6`; index avg `-0.0023` n `26`; metal avg `0.0001` n `20`; unknown avg `0.0938` n `836`
- 4h: commodity avg `0.0413` n `12`; crypto_alt avg `0.713` n `233`; crypto_major avg `0.6703` n `8`; equity avg `0.0121` n `136`; fx avg `0.0027` n `6`; index avg `0.001` n `26`; metal avg `0.0134` n `20`; unknown avg `0.4853` n `828`
- 24h: commodity avg `-0.0586` n `12`; crypto_alt avg `1.8527` n `233`; crypto_major avg `1.5054` n `8`; equity avg `0.0007` n `136`; fx avg `-0.0688` n `6`; index avg `0.0864` n `26`; metal avg `-0.0506` n `20`; unknown avg `0.8833` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal

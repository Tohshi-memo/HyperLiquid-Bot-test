# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T14:07:25.639723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `0.1534` n `233`; crypto_major avg `0.152` n `8`; equity avg `0.0098` n `136`; fx avg `0.0029` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0009` n `20`; unknown avg `-0.1379` n `836`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `-0.0342` n `233`; crypto_major avg `0.0148` n `8`; equity avg `-0.0206` n `136`; fx avg `-0.0044` n `6`; index avg `-0.0002` n `26`; metal avg `0.0045` n `20`; unknown avg `-0.0479` n `836`
- 4h: commodity avg `0.0016` n `12`; crypto_alt avg `0.0497` n `233`; crypto_major avg `0.1334` n `8`; equity avg `0.0139` n `136`; fx avg `0.0004` n `6`; index avg `-0.0009` n `26`; metal avg `0.0384` n `20`; unknown avg `0.5804` n `824`
- 24h: commodity avg `-0.0949` n `12`; crypto_alt avg `-0.6089` n `233`; crypto_major avg `-1.8084` n `8`; equity avg `-0.1534` n `136`; fx avg `0.0078` n `6`; index avg `0.0592` n `26`; metal avg `-0.2663` n `20`; unknown avg `9.2344` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal

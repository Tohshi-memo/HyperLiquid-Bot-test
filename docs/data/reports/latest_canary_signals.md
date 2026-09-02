# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T22:22:32.920886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `-0.198` n `232`; crypto_major avg `-0.143` n `8`; equity avg `0.0628` n `133`; fx avg `0.0016` n `6`; index avg `0.0149` n `26`; metal avg `-0.0146` n `20`; unknown avg `16.3299` n `792`
- 1h: commodity avg `0.0446` n `12`; crypto_alt avg `-0.3375` n `232`; crypto_major avg `-0.3591` n `8`; equity avg `0.0422` n `133`; fx avg `0.0084` n `6`; index avg `0.0128` n `26`; metal avg `-0.0341` n `20`; unknown avg `16.2793` n `790`
- 4h: commodity avg `0.0502` n `12`; crypto_alt avg `-0.2782` n `232`; crypto_major avg `-0.3128` n `8`; equity avg `0.254` n `133`; fx avg `-0.0294` n `6`; index avg `-0.0004` n `26`; metal avg `0.0329` n `20`; unknown avg `-0.3941` n `772`
- 24h: commodity avg `0.1294` n `12`; crypto_alt avg `-0.1745` n `232`; crypto_major avg `-0.243` n `8`; equity avg `1.1142` n `133`; fx avg `-0.4046` n `6`; index avg `0.1368` n `26`; metal avg `0.463` n `20`; unknown avg `-0.3052` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal

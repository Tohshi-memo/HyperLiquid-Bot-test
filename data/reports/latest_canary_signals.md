# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T21:22:27.545749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0982` n `12`; crypto_alt avg `0.0129` n `233`; crypto_major avg `0.0179` n `8`; equity avg `0.0198` n `136`; fx avg `-0.0057` n `6`; index avg `0.0055` n `27`; metal avg `-0.0109` n `20`; unknown avg `1.3035` n `840`
- 1h: commodity avg `-0.0423` n `12`; crypto_alt avg `0.1953` n `233`; crypto_major avg `0.1495` n `8`; equity avg `0.12` n `136`; fx avg `0.0244` n `6`; index avg `0.0259` n `27`; metal avg `0.0153` n `20`; unknown avg `18.8149` n `808`
- 4h: commodity avg `0.0476` n `12`; crypto_alt avg `-0.0554` n `233`; crypto_major avg `0.1536` n `8`; equity avg `0.0708` n `136`; fx avg `0.0345` n `6`; index avg `0.0076` n `27`; metal avg `-0.0213` n `20`; unknown avg `3.7213` n `778`
- 24h: commodity avg `0.2771` n `12`; crypto_alt avg `0.3447` n `233`; crypto_major avg `-0.3324` n `8`; equity avg `-1.0915` n `136`; fx avg `0.0446` n `6`; index avg `-0.2218` n `26`; metal avg `-0.0653` n `20`; unknown avg `1.8005` n `698`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal

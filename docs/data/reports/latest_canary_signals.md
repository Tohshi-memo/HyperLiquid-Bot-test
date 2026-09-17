# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T23:22:41.929662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.2061` n `234`; crypto_major avg `0.0997` n `8`; equity avg `0.0132` n `140`; fx avg `-0.0018` n `6`; index avg `0.0012` n `26`; metal avg `0.0251` n `20`; unknown avg `-0.0973` n `919`
- 1h: commodity avg `-0.0155` n `12`; crypto_alt avg `0.8097` n `234`; crypto_major avg `0.6281` n `8`; equity avg `0.0309` n `140`; fx avg `-0.0009` n `6`; index avg `0.0063` n `26`; metal avg `0.0431` n `20`; unknown avg `0.9622` n `875`
- 4h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.6908` n `234`; crypto_major avg `0.6025` n `8`; equity avg `0.0245` n `140`; fx avg `-0.0025` n `6`; index avg `-0.0317` n `26`; metal avg `0.0182` n `20`; unknown avg `1.0239` n `791`
- 24h: commodity avg `-0.1924` n `12`; crypto_alt avg `3.8318` n `234`; crypto_major avg `2.1133` n `8`; equity avg `1.8538` n `138`; fx avg `-0.0053` n `6`; index avg `0.345` n `26`; metal avg `0.546` n `20`; unknown avg `2.1897` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T15:52:31.888836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0585` n `12`; crypto_alt avg `-0.1731` n `229`; crypto_major avg `-0.1415` n `8`; equity avg `-0.1192` n `91`; fx avg `0.0001` n `6`; index avg `-0.0663` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.148` n `766`
- 1h: commodity avg `-0.2607` n `12`; crypto_alt avg `0.0745` n `229`; crypto_major avg `-0.057` n `8`; equity avg `-0.0532` n `91`; fx avg `-0.0205` n `6`; index avg `-0.0048` n `25`; metal avg `0.0116` n `20`; unknown avg `-0.1423` n `766`
- 4h: commodity avg `-0.6717` n `12`; crypto_alt avg `-0.5677` n `229`; crypto_major avg `-0.9294` n `8`; equity avg `-0.8945` n `91`; fx avg `-0.0874` n `6`; index avg `0.0138` n `25`; metal avg `0.0474` n `20`; unknown avg `-0.1891` n `766`
- 24h: commodity avg `-0.6594` n `12`; crypto_alt avg `0.7315` n `229`; crypto_major avg `0.9175` n `8`; equity avg `-1.3248` n `91`; fx avg `-0.1543` n `6`; index avg `-0.0338` n `25`; metal avg `-0.2229` n `20`; unknown avg `-0.3091` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal

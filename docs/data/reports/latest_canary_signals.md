# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T14:52:26.281590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `0.3892` n `231`; crypto_major avg `0.4023` n `8`; equity avg `0.034` n `127`; fx avg `0.0018` n `6`; index avg `0.0023` n `26`; metal avg `0.0311` n `20`; unknown avg `0.0827` n `785`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.76` n `231`; crypto_major avg `0.6646` n `8`; equity avg `0.0471` n `127`; fx avg `0.0061` n `6`; index avg `0.0073` n `26`; metal avg `0.0299` n `20`; unknown avg `0.367` n `785`
- 4h: commodity avg `0.0137` n `12`; crypto_alt avg `1.0528` n `231`; crypto_major avg `0.7969` n `8`; equity avg `0.0178` n `127`; fx avg `-0.0009` n `6`; index avg `0.004` n `26`; metal avg `0.0369` n `20`; unknown avg `0.2736` n `753`
- 24h: commodity avg `0.0732` n `12`; crypto_alt avg `-1.2839` n `231`; crypto_major avg `-1.5992` n `8`; equity avg `-1.1327` n `127`; fx avg `-0.052` n `6`; index avg `-0.2268` n `26`; metal avg `-0.6664` n `20`; unknown avg `-0.2684` n `735`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal

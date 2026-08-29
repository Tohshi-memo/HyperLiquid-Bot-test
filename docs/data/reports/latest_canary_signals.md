# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T21:21:03.459532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `0.0244` n `231`; crypto_major avg `0.0257` n `8`; equity avg `0.0018` n `128`; fx avg `-0.0018` n `6`; index avg `0.0026` n `26`; metal avg `0.0032` n `20`; unknown avg `0.0164` n `792`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `-0.1097` n `231`; crypto_major avg `-0.0488` n `8`; equity avg `0.0057` n `128`; fx avg `-0.0034` n `6`; index avg `0.0019` n `26`; metal avg `0.0083` n `20`; unknown avg `4.1007` n `792`
- 4h: commodity avg `0.002` n `12`; crypto_alt avg `0.1372` n `231`; crypto_major avg `0.1889` n `8`; equity avg `0.1861` n `128`; fx avg `-0.0103` n `6`; index avg `0.037` n `26`; metal avg `0.0243` n `20`; unknown avg `0.1398` n `792`
- 24h: commodity avg `-0.0277` n `12`; crypto_alt avg `0.7799` n `231`; crypto_major avg `1.1798` n `8`; equity avg `0.419` n `128`; fx avg `-0.0155` n `6`; index avg `0.0766` n `26`; metal avg `0.1607` n `20`; unknown avg `0.1136` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2214`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal

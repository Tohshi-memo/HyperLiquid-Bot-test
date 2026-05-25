# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T09:22:16.656976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0339` n `12`; crypto_alt avg `-0.1477` n `228`; crypto_major avg `-0.1156` n `8`; equity avg `0.0234` n `67`; fx avg `0.0158` n `6`; index avg `-0.0116` n `23`; metal avg `-0.0397` n `18`; unknown avg `-0.0591` n `397`
- 1h: commodity avg `-0.1836` n `12`; crypto_alt avg `0.1003` n `228`; crypto_major avg `0.0629` n `8`; equity avg `0.0892` n `67`; fx avg `0.0017` n `6`; index avg `0.0373` n `23`; metal avg `0.0245` n `18`; unknown avg `0.0616` n `397`
- 4h: commodity avg `0.404` n `12`; crypto_alt avg `0.3086` n `228`; crypto_major avg `0.2422` n `8`; equity avg `0.0423` n `67`; fx avg `0.075` n `6`; index avg `0.0778` n `23`; metal avg `0.0489` n `18`; unknown avg `0.2732` n `387`
- 24h: commodity avg `0.0547` n `12`; crypto_alt avg `0.0582` n `228`; crypto_major avg `-0.0921` n `8`; equity avg `0.5313` n `67`; fx avg `0.006` n `6`; index avg `-0.0408` n `23`; metal avg `0.4331` n `18`; unknown avg `0.1199` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal

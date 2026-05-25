# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T10:37:18.310736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `0.0584` n `228`; crypto_major avg `0.0001` n `8`; equity avg `0.0178` n `67`; fx avg `0.0002` n `6`; index avg `0.0043` n `23`; metal avg `-0.009` n `18`; unknown avg `0.0362` n `397`
- 1h: commodity avg `-0.0502` n `12`; crypto_alt avg `0.3738` n `228`; crypto_major avg `-0.0717` n `8`; equity avg `0.1022` n `67`; fx avg `-0.0023` n `6`; index avg `0.0389` n `23`; metal avg `0.2446` n `18`; unknown avg `-0.0571` n `397`
- 4h: commodity avg `-0.0645` n `12`; crypto_alt avg `0.597` n `228`; crypto_major avg `0.3148` n `8`; equity avg `0.3418` n `67`; fx avg `0.0303` n `6`; index avg `0.0829` n `23`; metal avg `0.5171` n `18`; unknown avg `-0.1324` n `397`
- 24h: commodity avg `-0.1529` n `12`; crypto_alt avg `0.6745` n `228`; crypto_major avg `0.0855` n `8`; equity avg `0.5246` n `67`; fx avg `0.0009` n `6`; index avg `0.0099` n `23`; metal avg `0.7396` n `18`; unknown avg `0.9519` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal

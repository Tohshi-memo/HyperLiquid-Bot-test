# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T21:07:26.752104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `0.1061` n `239`; crypto_major avg `0.0271` n `8`; equity avg `0.0284` n `168`; fx avg `0.0076` n `6`; index avg `0.0035` n `27`; metal avg `-0.0` n `20`; unknown avg `1.31` n `1220`
- 1h: commodity avg `0.0238` n `13`; crypto_alt avg `-0.1593` n `239`; crypto_major avg `-0.0039` n `8`; equity avg `-0.0149` n `168`; fx avg `0.0065` n `6`; index avg `-0.0045` n `27`; metal avg `-0.0088` n `20`; unknown avg `1.7251` n `1204`
- 4h: commodity avg `0.1266` n `13`; crypto_alt avg `-0.4325` n `239`; crypto_major avg `-0.3983` n `8`; equity avg `0.1619` n `168`; fx avg `-0.0109` n `6`; index avg `0.0168` n `27`; metal avg `0.01` n `20`; unknown avg `0.742` n `1171`
- 24h: commodity avg `-0.0136` n `13`; crypto_alt avg `-3.352` n `239`; crypto_major avg `-1.394` n `8`; equity avg `-0.1159` n `168`; fx avg `-0.008` n `6`; index avg `-0.0184` n `27`; metal avg `0.0155` n `20`; unknown avg `18.9629` n `1051`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T10:07:26.767339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0466` n `12`; crypto_alt avg `0.089` n `228`; crypto_major avg `0.1107` n `8`; equity avg `0.1235` n `74`; fx avg `0.0237` n `6`; index avg `0.0087` n `23`; metal avg `-0.068` n `18`; unknown avg `0.0028` n `517`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `0.7439` n `228`; crypto_major avg `0.5362` n `8`; equity avg `0.1926` n `74`; fx avg `-0.0008` n `6`; index avg `0.1807` n `23`; metal avg `0.0846` n `18`; unknown avg `-0.0284` n `517`
- 4h: commodity avg `-0.2732` n `12`; crypto_alt avg `1.0157` n `228`; crypto_major avg `0.5464` n `8`; equity avg `1.1112` n `74`; fx avg `-0.1136` n `6`; index avg `0.5489` n `23`; metal avg `0.1585` n `18`; unknown avg `-0.0654` n `517`
- 24h: commodity avg `0.8171` n `12`; crypto_alt avg `0.8661` n `228`; crypto_major avg `1.9783` n `8`; equity avg `1.3434` n `74`; fx avg `-0.31` n `6`; index avg `0.6232` n `23`; metal avg `-0.7363` n `18`; unknown avg `-2.4763` n `506`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal

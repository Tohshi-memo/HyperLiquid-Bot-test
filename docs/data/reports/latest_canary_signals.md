# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T10:37:16.830851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4318` n `12`; crypto_alt avg `0.1648` n `228`; crypto_major avg `0.1305` n `8`; equity avg `0.0384` n `66`; fx avg `-0.0128` n `6`; index avg `0.0101` n `23`; metal avg `0.1124` n `18`; unknown avg `0.4899` n `384`
- 1h: commodity avg `-0.4077` n `12`; crypto_alt avg `0.0752` n `228`; crypto_major avg `0.2272` n `8`; equity avg `0.2102` n `66`; fx avg `0.0015` n `6`; index avg `0.03` n `23`; metal avg `0.2128` n `18`; unknown avg `0.6547` n `384`
- 4h: commodity avg `-0.7626` n `12`; crypto_alt avg `0.4592` n `228`; crypto_major avg `0.5639` n `8`; equity avg `0.6599` n `66`; fx avg `-0.022` n `6`; index avg `0.3397` n `23`; metal avg `0.7016` n `18`; unknown avg `0.2319` n `384`
- 24h: commodity avg `-0.487` n `12`; crypto_alt avg `0.7651` n `228`; crypto_major avg `0.549` n `8`; equity avg `1.4196` n `66`; fx avg `-0.1526` n `6`; index avg `0.2118` n `23`; metal avg `-0.7243` n `18`; unknown avg `0.5713` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal

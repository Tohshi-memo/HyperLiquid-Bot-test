# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T04:52:14.787759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.49` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0487` n `12`; crypto_alt avg `-0.166` n `228`; crypto_major avg `-0.034` n `8`; equity avg `0.0351` n `67`; fx avg `0.0137` n `6`; index avg `0.0145` n `23`; metal avg `0.0039` n `18`; unknown avg `-0.3244` n `386`
- 1h: commodity avg `-0.0342` n `12`; crypto_alt avg `0.0516` n `228`; crypto_major avg `-0.0354` n `8`; equity avg `0.144` n `67`; fx avg `0.0193` n `6`; index avg `0.0901` n `23`; metal avg `0.1554` n `18`; unknown avg `-0.7051` n `386`
- 4h: commodity avg `-0.1541` n `12`; crypto_alt avg `0.8319` n `228`; crypto_major avg `0.1849` n `8`; equity avg `0.199` n `67`; fx avg `0.1059` n `6`; index avg `0.1195` n `23`; metal avg `0.0966` n `18`; unknown avg `-0.7628` n `386`
- 24h: commodity avg `-0.82` n `12`; crypto_alt avg `1.5439` n `228`; crypto_major avg `0.2297` n `8`; equity avg `1.3264` n `66`; fx avg `0.1214` n `6`; index avg `0.6068` n `23`; metal avg `0.5336` n `18`; unknown avg `2.1489` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0428`, n `668`, weak_sample_signal

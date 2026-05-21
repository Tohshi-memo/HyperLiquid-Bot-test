# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T11:37:16.480673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.68` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1068` n `12`; crypto_alt avg `-0.2332` n `228`; crypto_major avg `-0.1691` n `8`; equity avg `-0.0721` n `66`; fx avg `-0.0216` n `6`; index avg `-0.031` n `23`; metal avg `-0.3249` n `18`; unknown avg `-0.1542` n `386`
- 1h: commodity avg `0.215` n `12`; crypto_alt avg `-0.3775` n `228`; crypto_major avg `-0.524` n `8`; equity avg `-0.1404` n `66`; fx avg `-0.0066` n `6`; index avg `-0.0907` n `23`; metal avg `-0.2722` n `18`; unknown avg `-0.042` n `386`
- 4h: commodity avg `0.3537` n `12`; crypto_alt avg `-0.8649` n `228`; crypto_major avg `-0.6832` n `8`; equity avg `0.0038` n `66`; fx avg `0.04` n `6`; index avg `-0.0365` n `23`; metal avg `-0.149` n `18`; unknown avg `1.7868` n `385`
- 24h: commodity avg `-1.2482` n `12`; crypto_alt avg `1.618` n `228`; crypto_major avg `1.9984` n `8`; equity avg `1.0946` n `66`; fx avg `0.0362` n `6`; index avg `0.9085` n `23`; metal avg `-0.542` n `18`; unknown avg `7.5007` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal

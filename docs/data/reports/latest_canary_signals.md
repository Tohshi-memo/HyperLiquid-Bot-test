# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T20:43:28.342109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0892` n `12`; crypto_alt avg `0.0433` n `228`; crypto_major avg `-0.0349` n `8`; equity avg `0.0745` n `65`; fx avg `-0.0054` n `5`; index avg `-0.0027` n `23`; metal avg `0.0248` n `18`; unknown avg `-0.0233` n `375`
- 1h: commodity avg `-0.2006` n `12`; crypto_alt avg `-0.0336` n `228`; crypto_major avg `-0.0675` n `8`; equity avg `0.4744` n `65`; fx avg `-0.0117` n `5`; index avg `0.0548` n `23`; metal avg `-0.1969` n `18`; unknown avg `-0.289` n `375`
- 4h: commodity avg `-0.689` n `12`; crypto_alt avg `1.0968` n `228`; crypto_major avg `1.1531` n `8`; equity avg `1.3054` n `65`; fx avg `0.0532` n `5`; index avg `0.3195` n `23`; metal avg `0.1349` n `18`; unknown avg `-0.0807` n `375`
- 24h: commodity avg `-0.6188` n `12`; crypto_alt avg `3.1706` n `228`; crypto_major avg `1.4739` n `8`; equity avg `3.6398` n `65`; fx avg `0.2091` n `5`; index avg `1.489` n `23`; metal avg `0.7384` n `18`; unknown avg `0.6475` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal

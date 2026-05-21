# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T04:22:13.640632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `-0.1997` n `228`; crypto_major avg `-0.0844` n `8`; equity avg `0.0052` n `66`; fx avg `0.0056` n `6`; index avg `-0.0142` n `23`; metal avg `0.052` n `18`; unknown avg `-0.1208` n `384`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `-0.0084` n `228`; crypto_major avg `0.1075` n `8`; equity avg `0.0507` n `66`; fx avg `0.0107` n `6`; index avg `0.0577` n `23`; metal avg `-0.0172` n `18`; unknown avg `-0.3609` n `384`
- 4h: commodity avg `-0.2473` n `12`; crypto_alt avg `0.8338` n `228`; crypto_major avg `0.8919` n `8`; equity avg `0.7492` n `66`; fx avg `0.0608` n `6`; index avg `0.4766` n `23`; metal avg `-0.0891` n `18`; unknown avg `0.7836` n `384`
- 24h: commodity avg `-2.0462` n `12`; crypto_alt avg `3.7106` n `228`; crypto_major avg `3.95` n `8`; equity avg `2.4356` n `66`; fx avg `0.0244` n `6`; index avg `1.718` n `23`; metal avg `1.4838` n `18`; unknown avg `5.1753` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal

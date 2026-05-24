# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T20:52:15.519061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `-0.2157` n `228`; crypto_major avg `-0.2106` n `8`; equity avg `-0.0364` n `67`; fx avg `-0.0079` n `6`; index avg `-0.0586` n `23`; metal avg `-0.0479` n `18`; unknown avg `-0.1922` n `396`
- 1h: commodity avg `0.0685` n `12`; crypto_alt avg `-0.4877` n `228`; crypto_major avg `-0.4999` n `8`; equity avg `-0.0035` n `67`; fx avg `0.0319` n `6`; index avg `-0.1039` n `23`; metal avg `-0.1215` n `18`; unknown avg `-0.2691` n `396`
- 4h: commodity avg `0.235` n `12`; crypto_alt avg `-0.5016` n `228`; crypto_major avg `-0.5202` n `8`; equity avg `0.091` n `67`; fx avg `0.0362` n `6`; index avg `-0.0153` n `23`; metal avg `-0.2319` n `18`; unknown avg `-0.5345` n `396`
- 24h: commodity avg `0.628` n `12`; crypto_alt avg `-2.4625` n `228`; crypto_major avg `-0.4122` n `8`; equity avg `0.7289` n `67`; fx avg `0.1027` n `6`; index avg `-0.0049` n `23`; metal avg `-0.1933` n `18`; unknown avg `0.2433` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal

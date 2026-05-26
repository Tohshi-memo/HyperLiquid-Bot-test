# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T07:37:16.356099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2356` n `12`; crypto_alt avg `-0.1887` n `228`; crypto_major avg `-0.0547` n `8`; equity avg `-0.0763` n `67`; fx avg `0.0271` n `6`; index avg `-0.0661` n `23`; metal avg `-0.0284` n `18`; unknown avg `0.0272` n `417`
- 1h: commodity avg `0.6085` n `12`; crypto_alt avg `-0.6389` n `228`; crypto_major avg `-0.556` n `8`; equity avg `-0.3274` n `67`; fx avg `0.0002` n `6`; index avg `-0.1239` n `23`; metal avg `-0.2586` n `18`; unknown avg `0.1428` n `417`
- 4h: commodity avg `0.705` n `12`; crypto_alt avg `0.1883` n `228`; crypto_major avg `0.019` n `8`; equity avg `-0.2914` n `67`; fx avg `-0.0361` n `6`; index avg `-0.0895` n `23`; metal avg `-0.5012` n `18`; unknown avg `0.2619` n `397`
- 24h: commodity avg `0.696` n `12`; crypto_alt avg `-0.9628` n `228`; crypto_major avg `-1.4181` n `8`; equity avg `-0.7722` n `67`; fx avg `-0.0941` n `6`; index avg `-0.18` n `23`; metal avg `-0.6002` n `18`; unknown avg `0.2549` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal

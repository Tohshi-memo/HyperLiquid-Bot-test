# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T04:52:17.661439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.5624` n `228`; crypto_major avg `0.4982` n `8`; equity avg `0.1618` n `67`; fx avg `-0.0004` n `6`; index avg `0.0315` n `23`; metal avg `0.2321` n `18`; unknown avg `0.0409` n `418`
- 1h: commodity avg `-0.1262` n `12`; crypto_alt avg `-0.1213` n `228`; crypto_major avg `0.1111` n `8`; equity avg `-0.0924` n `67`; fx avg `-0.0078` n `6`; index avg `-0.0821` n `23`; metal avg `0.2255` n `18`; unknown avg `-0.1432` n `418`
- 4h: commodity avg `-0.5104` n `12`; crypto_alt avg `-1.198` n `228`; crypto_major avg `-0.3213` n `8`; equity avg `-0.2172` n `67`; fx avg `-0.0656` n `6`; index avg `-0.1415` n `23`; metal avg `-0.3287` n `18`; unknown avg `-0.4876` n `418`
- 24h: commodity avg `-0.3351` n `12`; crypto_alt avg `-1.2595` n `228`; crypto_major avg `-0.5073` n `8`; equity avg `0.5292` n `67`; fx avg `-0.0731` n `6`; index avg `0.8123` n `23`; metal avg `0.1693` n `18`; unknown avg `0.5735` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal

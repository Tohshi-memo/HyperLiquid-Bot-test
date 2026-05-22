# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T00:37:17.014433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.86` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1228` n `12`; crypto_alt avg `0.0186` n `228`; crypto_major avg `0.031` n `8`; equity avg `0.0431` n `67`; fx avg `0.0033` n `6`; index avg `0.0169` n `23`; metal avg `0.1009` n `18`; unknown avg `-0.1296` n `386`
- 1h: commodity avg `0.1663` n `12`; crypto_alt avg `-0.3162` n `228`; crypto_major avg `-0.3942` n `8`; equity avg `0.052` n `67`; fx avg `0.0436` n `6`; index avg `0.1956` n `23`; metal avg `0.0277` n `18`; unknown avg `-0.1303` n `386`
- 4h: commodity avg `-0.0933` n `12`; crypto_alt avg `-0.6118` n `228`; crypto_major avg `-0.5182` n `8`; equity avg `0.1731` n `67`; fx avg `0.0324` n `6`; index avg `0.3389` n `23`; metal avg `-0.0224` n `18`; unknown avg `-0.4944` n `386`
- 24h: commodity avg `-0.6874` n `12`; crypto_alt avg `1.4305` n `228`; crypto_major avg `0.7948` n `8`; equity avg `1.9202` n `66`; fx avg `0.0834` n `6`; index avg `0.9586` n `23`; metal avg `0.4918` n `18`; unknown avg `3.364` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0431`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0421`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T02:22:20.432317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.051` n `12`; crypto_alt avg `-0.1045` n `228`; crypto_major avg `-0.1112` n `8`; equity avg `-0.3522` n `74`; fx avg `0.0056` n `6`; index avg `-0.1569` n `23`; metal avg `-0.076` n `18`; unknown avg `-0.291` n `425`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `-0.5407` n `228`; crypto_major avg `-0.4283` n `8`; equity avg `-1.0716` n `74`; fx avg `-0.016` n `6`; index avg `-0.5902` n `23`; metal avg `-0.1902` n `18`; unknown avg `-0.0653` n `425`
- 4h: commodity avg `0.7202` n `12`; crypto_alt avg `-1.423` n `228`; crypto_major avg `-0.9478` n `8`; equity avg `-1.7637` n `74`; fx avg `-0.0348` n `6`; index avg `-0.5831` n `23`; metal avg `-0.3508` n `18`; unknown avg `0.5817` n `425`
- 24h: commodity avg `-1.2063` n `12`; crypto_alt avg `-6.0169` n `228`; crypto_major avg `-5.3085` n `8`; equity avg `-6.8774` n `74`; fx avg `-0.2186` n `6`; index avg `-4.1908` n `23`; metal avg `-4.0418` n `18`; unknown avg `-1.0715` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T14:22:18.666307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2298` n `12`; crypto_alt avg `0.061` n `228`; crypto_major avg `0.1122` n `8`; equity avg `0.0144` n `67`; fx avg `-0.0061` n `6`; index avg `0.0501` n `23`; metal avg `0.0196` n `18`; unknown avg `0.9249` n `396`
- 1h: commodity avg `-0.4699` n `12`; crypto_alt avg `0.2323` n `228`; crypto_major avg `0.1386` n `8`; equity avg `0.0833` n `67`; fx avg `-0.0073` n `6`; index avg `0.1092` n `23`; metal avg `0.034` n `18`; unknown avg `1.0057` n `396`
- 4h: commodity avg `-0.3026` n `12`; crypto_alt avg `1.0887` n `228`; crypto_major avg `0.7598` n `8`; equity avg `0.3256` n `67`; fx avg `-0.0085` n `6`; index avg `0.4773` n `23`; metal avg `0.0928` n `18`; unknown avg `1.0434` n `396`
- 24h: commodity avg `-0.2575` n `12`; crypto_alt avg `-4.0883` n `228`; crypto_major avg `-3.1166` n `8`; equity avg `-1.1389` n `67`; fx avg `0.0838` n `6`; index avg `0.0156` n `23`; metal avg `0.1848` n `18`; unknown avg `-1.7135` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal

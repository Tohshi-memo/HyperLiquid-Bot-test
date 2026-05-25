# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T04:37:14.123120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `0.2806` n `228`; crypto_major avg `0.2692` n `8`; equity avg `-0.0167` n `67`; fx avg `-0.0047` n `6`; index avg `-0.012` n `23`; metal avg `0.0014` n `18`; unknown avg `1.002` n `397`
- 1h: commodity avg `0.1789` n `12`; crypto_alt avg `0.3106` n `228`; crypto_major avg `0.3413` n `8`; equity avg `0.0647` n `67`; fx avg `-0.0011` n `6`; index avg `0.3153` n `23`; metal avg `0.0604` n `18`; unknown avg `0.7066` n `397`
- 4h: commodity avg `-0.4454` n `12`; crypto_alt avg `0.1907` n `228`; crypto_major avg `-0.2105` n `8`; equity avg `0.2889` n `67`; fx avg `-0.0592` n `6`; index avg `0.2632` n `23`; metal avg `-0.2204` n `18`; unknown avg `0.6667` n `396`
- 24h: commodity avg `0.0612` n `12`; crypto_alt avg `-0.7565` n `228`; crypto_major avg `0.1105` n `8`; equity avg `0.4455` n `67`; fx avg `-0.0661` n `6`; index avg `-0.0636` n `23`; metal avg `0.579` n `18`; unknown avg `0.7142` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal

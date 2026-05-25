# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T06:09:39.981278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1105` n `12`; crypto_alt avg `0.1588` n `228`; crypto_major avg `0.1268` n `8`; equity avg `-0.0762` n `67`; fx avg `-0.0002` n `6`; index avg `0.025` n `23`; metal avg `-0.0414` n `18`; unknown avg `0.0347` n `387`
- 1h: commodity avg `0.1619` n `12`; crypto_alt avg `0.2335` n `228`; crypto_major avg `0.0684` n `8`; equity avg `-0.0345` n `67`; fx avg `0.0431` n `6`; index avg `0.007` n `23`; metal avg `-0.3219` n `18`; unknown avg `0.0179` n `387`
- 4h: commodity avg `-0.4209` n `12`; crypto_alt avg `0.9391` n `228`; crypto_major avg `0.4004` n `8`; equity avg `0.2397` n `67`; fx avg `-0.0073` n `6`; index avg `0.1263` n `23`; metal avg `-0.3377` n `18`; unknown avg `0.1793` n `386`
- 24h: commodity avg `0.1756` n `12`; crypto_alt avg `0.3981` n `228`; crypto_major avg `0.4945` n `8`; equity avg `0.4339` n `67`; fx avg `-0.036` n `6`; index avg `-0.1374` n `23`; metal avg `0.1631` n `18`; unknown avg `-0.2845` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal

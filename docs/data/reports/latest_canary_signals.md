# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T06:37:24.456754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.26` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.8167` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0394` n `12`; crypto_alt avg `0.4546` n `228`; crypto_major avg `0.3021` n `8`; equity avg `0.0567` n `72`; fx avg `-0.0014` n `6`; index avg `0.0294` n `23`; metal avg `-0.1401` n `18`; unknown avg `-0.1403` n `420`
- 1h: commodity avg `0.0889` n `12`; crypto_alt avg `0.9923` n `228`; crypto_major avg `0.7274` n `8`; equity avg `0.1252` n `72`; fx avg `0.04` n `6`; index avg `0.0319` n `23`; metal avg `-0.2046` n `18`; unknown avg `-0.2888` n `410`
- 4h: commodity avg `0.1953` n `12`; crypto_alt avg `2.3141` n `228`; crypto_major avg `1.4453` n `8`; equity avg `0.4353` n `72`; fx avg `0.087` n `6`; index avg `-0.0631` n `23`; metal avg `-0.3714` n `18`; unknown avg `0.4678` n `410`
- 24h: commodity avg `1.1475` n `12`; crypto_alt avg `-1.2172` n `228`; crypto_major avg `-3.4669` n `8`; equity avg `0.9598` n `72`; fx avg `0.0516` n `6`; index avg `1.0921` n `23`; metal avg `-1.5592` n `18`; unknown avg `-0.5846` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal

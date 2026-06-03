# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T10:14:09.073561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2407` n `12`; crypto_alt avg `0.1983` n `228`; crypto_major avg `0.1015` n `8`; equity avg `0.1512` n `72`; fx avg `-0.0075` n `6`; index avg `0.0459` n `23`; metal avg `0.3659` n `18`; unknown avg `0.0076` n `420`
- 1h: commodity avg `0.0358` n `12`; crypto_alt avg `0.3071` n `228`; crypto_major avg `0.2713` n `8`; equity avg `0.0281` n `72`; fx avg `0.0051` n `6`; index avg `0.0456` n `23`; metal avg `0.1752` n `18`; unknown avg `-0.1487` n `420`
- 4h: commodity avg `0.6875` n `12`; crypto_alt avg `0.5986` n `228`; crypto_major avg `0.254` n `8`; equity avg `-0.2455` n `72`; fx avg `0.0392` n `6`; index avg `0.0134` n `23`; metal avg `-0.0138` n `18`; unknown avg `0.6018` n `420`
- 24h: commodity avg `1.8534` n `12`; crypto_alt avg `-0.3444` n `228`; crypto_major avg `-2.7042` n `8`; equity avg `0.5328` n `72`; fx avg `0.0558` n `6`; index avg `0.8828` n `23`; metal avg `-1.2825` n `18`; unknown avg `0.7675` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal

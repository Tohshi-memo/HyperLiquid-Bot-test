# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T01:37:31.475947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0433` n `12`; crypto_alt avg `0.2251` n `228`; crypto_major avg `0.122` n `8`; equity avg `-0.0172` n `74`; fx avg `0.0016` n `6`; index avg `-0.0069` n `23`; metal avg `-0.0286` n `18`; unknown avg `-0.3325` n `643`
- 1h: commodity avg `0.0752` n `12`; crypto_alt avg `0.6393` n `228`; crypto_major avg `0.2722` n `8`; equity avg `-0.1515` n `74`; fx avg `-0.0108` n `6`; index avg `-0.0669` n `23`; metal avg `0.0301` n `18`; unknown avg `-0.2074` n `643`
- 4h: commodity avg `-0.1268` n `12`; crypto_alt avg `0.5813` n `228`; crypto_major avg `-0.3082` n `8`; equity avg `0.0771` n `74`; fx avg `0.0557` n `6`; index avg `0.1567` n `23`; metal avg `0.0415` n `18`; unknown avg `-0.2576` n `643`
- 24h: commodity avg `-0.6831` n `12`; crypto_alt avg `0.7661` n `228`; crypto_major avg `0.5699` n `8`; equity avg `-0.4128` n `74`; fx avg `0.015` n `6`; index avg `0.6327` n `23`; metal avg `0.7556` n `18`; unknown avg `40.5663` n `515`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal

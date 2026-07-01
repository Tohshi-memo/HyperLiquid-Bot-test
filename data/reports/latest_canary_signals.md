# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T14:01:16.469997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `-0.0544` n `228`; crypto_major avg `-0.1746` n `8`; equity avg `0.0025` n `88`; fx avg `-0.0118` n `6`; index avg `0.0135` n `23`; metal avg `0.0276` n `20`; unknown avg `-0.0473` n `765`
- 1h: commodity avg `-0.124` n `12`; crypto_alt avg `0.831` n `228`; crypto_major avg `0.932` n `8`; equity avg `0.6859` n `88`; fx avg `0.0031` n `6`; index avg `-0.0004` n `23`; metal avg `0.8888` n `20`; unknown avg `0.4061` n `765`
- 4h: commodity avg `-0.0991` n `12`; crypto_alt avg `0.6467` n `228`; crypto_major avg `0.4676` n `8`; equity avg `-0.3123` n `88`; fx avg `-0.0425` n `6`; index avg `-0.0732` n `23`; metal avg `1.1332` n `20`; unknown avg `-0.0205` n `765`
- 24h: commodity avg `-0.6548` n `12`; crypto_alt avg `0.9805` n `228`; crypto_major avg `0.3871` n `8`; equity avg `0.0928` n `88`; fx avg `0.0877` n `6`; index avg `-0.2342` n `23`; metal avg `0.5162` n `20`; unknown avg `0.0144` n `743`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal

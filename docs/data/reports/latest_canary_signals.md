# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T10:37:29.838687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0221` n `13`; crypto_alt avg `0.3692` n `238`; crypto_major avg `0.5086` n `8`; equity avg `0.0327` n `156`; fx avg `-0.0018` n `6`; index avg `0.0053` n `27`; metal avg `0.0073` n `20`; unknown avg `0.7527` n `1261`
- 1h: commodity avg `0.0855` n `13`; crypto_alt avg `0.6415` n `238`; crypto_major avg `0.3929` n `8`; equity avg `-0.2932` n `156`; fx avg `0.0108` n `6`; index avg `-0.0287` n `27`; metal avg `-0.1054` n `20`; unknown avg `-0.0713` n `1255`
- 4h: commodity avg `0.3539` n `13`; crypto_alt avg `0.1761` n `238`; crypto_major avg `-0.8896` n `8`; equity avg `-1.0071` n `156`; fx avg `0.048` n `6`; index avg `-0.0669` n `27`; metal avg `-0.1199` n `20`; unknown avg `2.5297` n `1192`
- 24h: commodity avg `0.2406` n `13`; crypto_alt avg `-3.395` n `238`; crypto_major avg `-1.0408` n `8`; equity avg `-3.6463` n `155`; fx avg `0.1003` n `6`; index avg `-0.4167` n `27`; metal avg `-0.6797` n `20`; unknown avg `28.859` n `1032`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal

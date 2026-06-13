# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T03:07:28.664292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.2007` n `228`; crypto_major avg `0.135` n `8`; equity avg `0.0293` n `74`; fx avg `0.0001` n `6`; index avg `0.0115` n `23`; metal avg `-0.0184` n `18`; unknown avg `-0.0952` n `643`
- 1h: commodity avg `-0.134` n `12`; crypto_alt avg `-0.1834` n `228`; crypto_major avg `-0.1983` n `8`; equity avg `0.0345` n `74`; fx avg `0.008` n `6`; index avg `0.0486` n `23`; metal avg `-0.0432` n `18`; unknown avg `0.1338` n `643`
- 4h: commodity avg `0.0262` n `12`; crypto_alt avg `0.9969` n `228`; crypto_major avg `0.1139` n `8`; equity avg `0.1418` n `74`; fx avg `0.0297` n `6`; index avg `0.2268` n `23`; metal avg `0.0305` n `18`; unknown avg `-0.4317` n `643`
- 24h: commodity avg `-0.9789` n `12`; crypto_alt avg `0.2148` n `228`; crypto_major avg `-0.149` n `8`; equity avg `-0.5807` n `74`; fx avg `0.0034` n `6`; index avg `0.7317` n `23`; metal avg `0.3367` n `18`; unknown avg `39.9023` n `515`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal

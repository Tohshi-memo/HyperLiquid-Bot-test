# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T16:52:28.980700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1115` n `12`; crypto_alt avg `0.1427` n `228`; crypto_major avg `0.06` n `8`; equity avg `0.2196` n `74`; fx avg `-0.0026` n `6`; index avg `0.0913` n `23`; metal avg `0.0577` n `18`; unknown avg `-0.0776` n `643`
- 1h: commodity avg `0.1745` n `12`; crypto_alt avg `0.086` n `228`; crypto_major avg `0.3369` n `8`; equity avg `0.488` n `74`; fx avg `-0.014` n `6`; index avg `0.165` n `23`; metal avg `0.2131` n `18`; unknown avg `0.0177` n `643`
- 4h: commodity avg `-0.0749` n `12`; crypto_alt avg `-0.2305` n `228`; crypto_major avg `0.5921` n `8`; equity avg `0.1085` n `74`; fx avg `-0.0004` n `6`; index avg `0.4879` n `23`; metal avg `0.5575` n `18`; unknown avg `26.6437` n `643`
- 24h: commodity avg `-2.1044` n `12`; crypto_alt avg `2.1032` n `228`; crypto_major avg `3.1507` n `8`; equity avg `2.8123` n `74`; fx avg `0.0851` n `6`; index avg `2.0176` n `23`; metal avg `3.2375` n `18`; unknown avg `43.2453` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal

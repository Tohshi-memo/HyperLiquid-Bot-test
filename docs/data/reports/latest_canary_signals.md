# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T20:52:27.061162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0492` n `228`; crypto_major avg `-0.0751` n `8`; equity avg `-0.0054` n `74`; fx avg `0.0222` n `6`; index avg `0.0005` n `23`; metal avg `0.1297` n `18`; unknown avg `-0.2208` n `644`
- 1h: commodity avg `0.0383` n `12`; crypto_alt avg `-0.392` n `228`; crypto_major avg `-0.1804` n `8`; equity avg `-0.001` n `74`; fx avg `0.013` n `6`; index avg `0.1082` n `23`; metal avg `0.2445` n `18`; unknown avg `0.0109` n `644`
- 4h: commodity avg `-0.1702` n `12`; crypto_alt avg `-0.0362` n `228`; crypto_major avg `0.0961` n `8`; equity avg `0.3022` n `74`; fx avg `0.0444` n `6`; index avg `0.0877` n `23`; metal avg `0.1227` n `18`; unknown avg `-0.3925` n `644`
- 24h: commodity avg `-0.6384` n `12`; crypto_alt avg `2.0954` n `228`; crypto_major avg `0.6822` n `8`; equity avg `0.4998` n `74`; fx avg `0.0507` n `6`; index avg `0.5718` n `23`; metal avg `0.2652` n `18`; unknown avg `-1.795` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal

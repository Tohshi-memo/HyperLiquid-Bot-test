# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T17:37:30.605599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `-0.0546` n `234`; crypto_major avg `-0.0215` n `8`; equity avg `-0.0991` n `138`; fx avg `-0.0007` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0161` n `20`; unknown avg `0.3607` n `919`
- 1h: commodity avg `0.0943` n `12`; crypto_alt avg `0.4228` n `234`; crypto_major avg `0.4988` n `8`; equity avg `-0.0207` n `138`; fx avg `0.0142` n `6`; index avg `0.005` n `26`; metal avg `-0.0295` n `20`; unknown avg `1.7143` n `917`
- 4h: commodity avg `0.3307` n `12`; crypto_alt avg `1.5376` n `234`; crypto_major avg `1.0661` n `8`; equity avg `0.2361` n `138`; fx avg `-0.0301` n `6`; index avg `0.0383` n `26`; metal avg `-0.0457` n `20`; unknown avg `2.8827` n `889`
- 24h: commodity avg `0.034` n `12`; crypto_alt avg `5.72` n `234`; crypto_major avg `3.3826` n `8`; equity avg `1.9387` n `138`; fx avg `0.0573` n `6`; index avg `0.2699` n `26`; metal avg `0.2074` n `20`; unknown avg `0.7808` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T17:37:29.460757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.28` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.026` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.611` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `-0.0318` n `228`; crypto_major avg `0.1347` n `8`; equity avg `-0.1184` n `88`; fx avg `0.0019` n `6`; index avg `-0.0384` n `25`; metal avg `0.0298` n `20`; unknown avg `0.8041` n `763`
- 1h: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.2714` n `228`; crypto_major avg `0.0489` n `8`; equity avg `-0.3484` n `88`; fx avg `0.0023` n `6`; index avg `-0.0661` n `25`; metal avg `-0.0815` n `20`; unknown avg `0.5497` n `763`
- 4h: commodity avg `-0.1933` n `12`; crypto_alt avg `1.2639` n `228`; crypto_major avg `1.8327` n `8`; equity avg `0.5025` n `88`; fx avg `-0.0265` n `6`; index avg `-0.0646` n `25`; metal avg `0.2217` n `20`; unknown avg `1.7235` n `763`
- 24h: commodity avg `-0.5517` n `12`; crypto_alt avg `1.9882` n `228`; crypto_major avg `2.218` n `8`; equity avg `-0.5515` n `88`; fx avg `-0.0079` n `6`; index avg `-0.4515` n `25`; metal avg `0.3628` n `20`; unknown avg `1.244` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal

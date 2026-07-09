# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T16:07:26.644194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `0.0276` n `229`; crypto_major avg `-0.0337` n `8`; equity avg `-0.0035` n `91`; fx avg `0.0012` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0491` n `20`; unknown avg `-0.0173` n `765`
- 1h: commodity avg `-0.1399` n `12`; crypto_alt avg `-0.1808` n `229`; crypto_major avg `-0.3625` n `8`; equity avg `0.2167` n `91`; fx avg `0.0031` n `6`; index avg `0.0427` n `25`; metal avg `-0.0176` n `20`; unknown avg `0.0326` n `765`
- 4h: commodity avg `-0.8941` n `12`; crypto_alt avg `-0.0683` n `229`; crypto_major avg `0.0429` n `8`; equity avg `0.9084` n `91`; fx avg `-0.0313` n `6`; index avg `0.1979` n `25`; metal avg `0.2584` n `20`; unknown avg `0.2081` n `765`
- 24h: commodity avg `-1.3324` n `12`; crypto_alt avg `1.4286` n `229`; crypto_major avg `0.9542` n `8`; equity avg `3.5217` n `91`; fx avg `0.055` n `6`; index avg `0.5987` n `25`; metal avg `1.3157` n `20`; unknown avg `1.1833` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal

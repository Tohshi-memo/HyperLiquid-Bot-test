# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T09:22:28.650182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.66` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.8631` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8088` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6131` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1274` n `12`; crypto_alt avg `-0.4357` n `228`; crypto_major avg `-0.2611` n `8`; equity avg `-0.0032` n `69`; fx avg `-0.0002` n `6`; index avg `-0.0205` n `23`; metal avg `-0.0482` n `18`; unknown avg `-0.0888` n `422`
- 1h: commodity avg `-0.0917` n `12`; crypto_alt avg `-0.5659` n `228`; crypto_major avg `-0.4523` n `8`; equity avg `-0.1881` n `69`; fx avg `-0.0172` n `6`; index avg `-0.0221` n `23`; metal avg `-0.2998` n `18`; unknown avg `-0.1587` n `422`
- 4h: commodity avg `-0.17` n `12`; crypto_alt avg `-1.3871` n `228`; crypto_major avg `-1.4388` n `8`; equity avg `0.1743` n `69`; fx avg `0.0418` n `6`; index avg `0.37` n `23`; metal avg `0.4243` n `18`; unknown avg `-0.7624` n `412`
- 24h: commodity avg `-1.3992` n `12`; crypto_alt avg `-0.8086` n `228`; crypto_major avg `-2.1757` n `8`; equity avg `0.3814` n `69`; fx avg `0.1144` n `6`; index avg `-0.0233` n `23`; metal avg `0.8069` n `18`; unknown avg `0.675` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal

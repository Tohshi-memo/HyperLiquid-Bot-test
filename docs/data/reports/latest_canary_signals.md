# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T06:22:37.110933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `-0.4123` n `238`; crypto_major avg `-0.3457` n `8`; equity avg `-0.1924` n `155`; fx avg `-0.0007` n `6`; index avg `-0.0331` n `27`; metal avg `0.0117` n `20`; unknown avg `-0.1841` n `1236`
- 1h: commodity avg `0.0073` n `13`; crypto_alt avg `-0.7945` n `238`; crypto_major avg `-0.5815` n `8`; equity avg `-0.452` n `155`; fx avg `-0.011` n `6`; index avg `-0.0684` n `27`; metal avg `-0.1967` n `20`; unknown avg `0.8076` n `1212`
- 4h: commodity avg `-0.0409` n `13`; crypto_alt avg `-0.2512` n `238`; crypto_major avg `0.1833` n `8`; equity avg `0.3881` n `155`; fx avg `-0.006` n `6`; index avg `0.1609` n `27`; metal avg `-0.2439` n `20`; unknown avg `1.8666` n `1176`
- 24h: commodity avg `-0.1792` n `13`; crypto_alt avg `-2.3927` n `238`; crypto_major avg `-1.5099` n `8`; equity avg `-1.1036` n `154`; fx avg `0.0461` n `6`; index avg `-0.0073` n `27`; metal avg `-0.2985` n `20`; unknown avg `31.1669` n `970`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal

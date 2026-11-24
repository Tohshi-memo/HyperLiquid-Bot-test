# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T17:22:27.694419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0905` n `13`; crypto_alt avg `0.1465` n `239`; crypto_major avg `-0.036` n `8`; equity avg `-0.0081` n `168`; fx avg `0.0007` n `6`; index avg `0.0144` n `27`; metal avg `-0.0289` n `20`; unknown avg `0.1842` n `1263`
- 1h: commodity avg `0.1788` n `13`; crypto_alt avg `0.3779` n `239`; crypto_major avg `0.0706` n `8`; equity avg `0.5444` n `168`; fx avg `-0.0002` n `6`; index avg `0.0946` n `27`; metal avg `-0.0042` n `20`; unknown avg `313.6754` n `1261`
- 4h: commodity avg `0.3726` n `13`; crypto_alt avg `-0.3604` n `239`; crypto_major avg `-0.8889` n `8`; equity avg `-1.4826` n `168`; fx avg `0.0357` n `6`; index avg `-0.012` n `27`; metal avg `-0.639` n `20`; unknown avg `298.2932` n `1245`
- 24h: commodity avg `0.4608` n `13`; crypto_alt avg `-4.447` n `239`; crypto_major avg `-4.5206` n `8`; equity avg `-4.5129` n `167`; fx avg `0.2503` n `6`; index avg `-0.2923` n `27`; metal avg `-1.272` n `20`; unknown avg `174.8811` n `1139`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal

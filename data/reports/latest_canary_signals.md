# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T22:52:24.016810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0557` n `13`; crypto_alt avg `-0.0859` n `238`; crypto_major avg `-0.0331` n `8`; equity avg `0.0489` n `155`; fx avg `0.0008` n `6`; index avg `0.0131` n `27`; metal avg `0.0039` n `20`; unknown avg `1.9238` n `1224`
- 1h: commodity avg `-0.0092` n `13`; crypto_alt avg `-0.5304` n `238`; crypto_major avg `-0.2559` n `8`; equity avg `-0.2116` n `155`; fx avg `-0.0052` n `6`; index avg `-0.0441` n `27`; metal avg `-0.0392` n `20`; unknown avg `1.7731` n `1208`
- 4h: commodity avg `-0.1864` n `13`; crypto_alt avg `0.6158` n `238`; crypto_major avg `0.3726` n `8`; equity avg `-0.8618` n `155`; fx avg `-0.0201` n `6`; index avg `-0.1325` n `27`; metal avg `0.082` n `20`; unknown avg `4.4587` n `1104`
- 24h: commodity avg `0.1927` n `13`; crypto_alt avg `0.7594` n `238`; crypto_major avg `0.5881` n `8`; equity avg `0.8159` n `154`; fx avg `0.2446` n `6`; index avg `0.127` n `27`; metal avg `-0.1837` n `20`; unknown avg `27.1437` n `1050`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal

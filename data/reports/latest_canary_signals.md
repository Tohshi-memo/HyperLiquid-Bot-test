# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T08:07:29.124095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.079` n `13`; crypto_alt avg `0.0588` n `238`; crypto_major avg `0.1835` n `8`; equity avg `-0.0377` n `155`; fx avg `-0.0072` n `6`; index avg `-0.0076` n `27`; metal avg `0.0718` n `20`; unknown avg `173.3221` n `1216`
- 1h: commodity avg `-0.0277` n `13`; crypto_alt avg `-0.2765` n `238`; crypto_major avg `-0.0808` n `8`; equity avg `-0.304` n `155`; fx avg `0.0227` n `6`; index avg `-0.0828` n `27`; metal avg `-0.0549` n `20`; unknown avg `168.4298` n `1216`
- 4h: commodity avg `-0.0194` n `13`; crypto_alt avg `-0.1351` n `238`; crypto_major avg `0.3837` n `8`; equity avg `-0.0109` n `155`; fx avg `0.0167` n `6`; index avg `0.0682` n `27`; metal avg `-0.0689` n `20`; unknown avg `3.6912` n `1180`
- 24h: commodity avg `-0.0948` n `13`; crypto_alt avg `-2.8694` n `238`; crypto_major avg `-1.77` n `8`; equity avg `-1.7696` n `154`; fx avg `0.0539` n `6`; index avg `-0.1293` n `27`; metal avg `-0.3539` n `20`; unknown avg `31.5824` n `968`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal

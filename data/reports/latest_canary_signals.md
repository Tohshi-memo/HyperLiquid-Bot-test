# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T09:07:30.097994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0904` n `12`; crypto_alt avg `-0.05` n `230`; crypto_major avg `-0.048` n `8`; equity avg `-0.1126` n `120`; fx avg `-0.0019` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0093` n `20`; unknown avg `-0.0314` n `789`
- 1h: commodity avg `0.0917` n `12`; crypto_alt avg `0.0705` n `230`; crypto_major avg `0.2414` n `8`; equity avg `-0.234` n `120`; fx avg `0.0164` n `6`; index avg `-0.0115` n `25`; metal avg `-0.0289` n `20`; unknown avg `-0.0332` n `789`
- 4h: commodity avg `0.09` n `12`; crypto_alt avg `0.2803` n `230`; crypto_major avg `0.2379` n `8`; equity avg `1.0952` n `120`; fx avg `-0.0309` n `6`; index avg `0.2205` n `25`; metal avg `0.1023` n `20`; unknown avg `-0.027` n `757`
- 24h: commodity avg `0.3933` n `12`; crypto_alt avg `0.3736` n `230`; crypto_major avg `0.3458` n `8`; equity avg `-1.3288` n `120`; fx avg `-0.1981` n `6`; index avg `-0.1304` n `25`; metal avg `-0.437` n `20`; unknown avg `-0.2695` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal

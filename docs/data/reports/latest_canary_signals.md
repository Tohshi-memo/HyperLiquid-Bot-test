# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T00:52:16.407584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0859` n `12`; crypto_alt avg `0.0273` n `228`; crypto_major avg `0.0533` n `8`; equity avg `-0.1618` n `66`; fx avg `-0.0059` n `6`; index avg `-0.1172` n `23`; metal avg `-0.1897` n `18`; unknown avg `-0.0373` n `383`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `0.5245` n `228`; crypto_major avg `0.4958` n `8`; equity avg `0.0082` n `66`; fx avg `0.0621` n `6`; index avg `-0.0177` n `23`; metal avg `-0.3756` n `18`; unknown avg `0.0906` n `383`
- 4h: commodity avg `0.0805` n `12`; crypto_alt avg `1.6021` n `228`; crypto_major avg `1.2848` n `8`; equity avg `0.4692` n `66`; fx avg `0.079` n `6`; index avg `0.1495` n `23`; metal avg `0.159` n `18`; unknown avg `0.0358` n `383`
- 24h: commodity avg `0.1523` n `12`; crypto_alt avg `1.7912` n `228`; crypto_major avg `0.6634` n `8`; equity avg `0.4675` n `66`; fx avg `0.2232` n `6`; index avg `0.2521` n `23`; metal avg `2.1268` n `18`; unknown avg `0.5176` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal

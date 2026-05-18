# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T21:52:16.485571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.065` n `12`; crypto_alt avg `0.0299` n `228`; crypto_major avg `-0.0262` n `8`; equity avg `0.0259` n `66`; fx avg `0.0091` n `6`; index avg `0.0711` n `23`; metal avg `0.0036` n `18`; unknown avg `-0.0475` n `383`
- 1h: commodity avg `0.127` n `12`; crypto_alt avg `0.8898` n `228`; crypto_major avg `0.9274` n `8`; equity avg `0.2766` n `66`; fx avg `-0.0089` n `6`; index avg `0.2774` n `23`; metal avg `0.0684` n `18`; unknown avg `0.223` n `383`
- 4h: commodity avg `-0.257` n `12`; crypto_alt avg `1.2791` n `228`; crypto_major avg `1.2472` n `8`; equity avg `0.5351` n `66`; fx avg `-0.0549` n `6`; index avg `0.4509` n `23`; metal avg `0.4282` n `18`; unknown avg `0.472` n `383`
- 24h: commodity avg `0.9918` n `12`; crypto_alt avg `-1.5926` n `228`; crypto_major avg `-1.7743` n `8`; equity avg `-0.8009` n `66`; fx avg `0.1836` n `6`; index avg `-0.2269` n `23`; metal avg `1.1263` n `18`; unknown avg `0.1248` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal

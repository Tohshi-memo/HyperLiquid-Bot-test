# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T11:37:29.614838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0299` n `12`; crypto_alt avg `0.2625` n `228`; crypto_major avg `0.2566` n `8`; equity avg `0.0769` n `74`; fx avg `0.016` n `6`; index avg `0.0349` n `23`; metal avg `0.008` n `18`; unknown avg `-0.1123` n `645`
- 1h: commodity avg `0.0826` n `12`; crypto_alt avg `-0.2509` n `228`; crypto_major avg `-0.1486` n `8`; equity avg `0.0092` n `74`; fx avg `0.0047` n `6`; index avg `0.0434` n `23`; metal avg `-0.0829` n `18`; unknown avg `0.0894` n `645`
- 4h: commodity avg `0.0905` n `12`; crypto_alt avg `0.1173` n `228`; crypto_major avg `0.3216` n `8`; equity avg `0.3818` n `74`; fx avg `0.0036` n `6`; index avg `0.1362` n `23`; metal avg `-0.045` n `18`; unknown avg `0.3636` n `629`
- 24h: commodity avg `-0.5055` n `12`; crypto_alt avg `-0.1075` n `228`; crypto_major avg `0.8298` n `8`; equity avg `1.0374` n `74`; fx avg `-0.007` n `6`; index avg `0.2765` n `23`; metal avg `0.3358` n `18`; unknown avg `-0.9387` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal

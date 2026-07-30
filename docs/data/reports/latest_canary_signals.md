# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T11:52:23.660606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `0.1246` n `230`; crypto_major avg `0.1829` n `8`; equity avg `0.2138` n `102`; fx avg `0.0084` n `6`; index avg `0.0349` n `25`; metal avg `0.0156` n `20`; unknown avg `-0.0093` n `779`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `0.2325` n `230`; crypto_major avg `0.1674` n `8`; equity avg `0.6298` n `102`; fx avg `-0.0138` n `6`; index avg `0.0906` n `25`; metal avg `0.0234` n `20`; unknown avg `-0.0171` n `779`
- 4h: commodity avg `-0.3413` n `12`; crypto_alt avg `0.277` n `230`; crypto_major avg `0.754` n `8`; equity avg `2.0533` n `102`; fx avg `-0.0431` n `6`; index avg `0.3338` n `25`; metal avg `0.4243` n `20`; unknown avg `0.0845` n `771`
- 24h: commodity avg `0.3588` n `12`; crypto_alt avg `0.0017` n `230`; crypto_major avg `0.1328` n `8`; equity avg `-1.7317` n `102`; fx avg `-0.0668` n `6`; index avg `-0.272` n `25`; metal avg `0.4553` n `20`; unknown avg `-0.1673` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal

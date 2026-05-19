# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T04:37:16.676469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.0202` n `228`; crypto_major avg `0.0014` n `8`; equity avg `0.0023` n `66`; fx avg `0.0018` n `6`; index avg `0.0027` n `23`; metal avg `-0.0097` n `18`; unknown avg `0.0122` n `383`
- 1h: commodity avg `0.0268` n `12`; crypto_alt avg `0.0925` n `228`; crypto_major avg `-0.0209` n `8`; equity avg `-0.281` n `66`; fx avg `0.0226` n `6`; index avg `-0.2498` n `23`; metal avg `-0.1511` n `18`; unknown avg `0.0985` n `383`
- 4h: commodity avg `0.1114` n `12`; crypto_alt avg `-0.3674` n `228`; crypto_major avg `-0.5222` n `8`; equity avg `-0.7764` n `66`; fx avg `0.0809` n `6`; index avg `-0.5786` n `23`; metal avg `-1.2593` n `18`; unknown avg `-0.5204` n `383`
- 24h: commodity avg `0.1312` n `12`; crypto_alt avg `1.0502` n `228`; crypto_major avg `0.4098` n `8`; equity avg `-0.7751` n `66`; fx avg `0.2605` n `6`; index avg `-0.4501` n `23`; metal avg `0.2992` n `18`; unknown avg `0.5804` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T16:37:28.268641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0833` n `13`; crypto_alt avg `-0.512` n `239`; crypto_major avg `-0.454` n `8`; equity avg `-0.6814` n `162`; fx avg `-0.0126` n `6`; index avg `-0.0606` n `27`; metal avg `-0.0839` n `20`; unknown avg `0.4924` n `1259`
- 1h: commodity avg `0.0776` n `13`; crypto_alt avg `0.8713` n `239`; crypto_major avg `0.5307` n `8`; equity avg `1.1482` n `162`; fx avg `0.0066` n `6`; index avg `0.1028` n `27`; metal avg `0.0843` n `20`; unknown avg `6.4445` n `1243`
- 4h: commodity avg `0.3085` n `13`; crypto_alt avg `-0.1823` n `239`; crypto_major avg `-0.7011` n `8`; equity avg `0.7016` n `162`; fx avg `-0.01` n `6`; index avg `0.1191` n `27`; metal avg `-0.3711` n `20`; unknown avg `0.9376` n `1241`
- 24h: commodity avg `-0.1115` n `13`; crypto_alt avg `-3.6272` n `239`; crypto_major avg `-3.6121` n `8`; equity avg `-2.6806` n `162`; fx avg `-0.1273` n `6`; index avg `-0.1172` n `27`; metal avg `-0.9918` n `20`; unknown avg `3.1826` n `1149`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal

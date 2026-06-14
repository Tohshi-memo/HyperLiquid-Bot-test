# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T00:07:30.927551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0447` n `12`; crypto_alt avg `-0.0036` n `228`; crypto_major avg `-0.0063` n `8`; equity avg `-0.0093` n `74`; fx avg `0.0024` n `6`; index avg `-0.0062` n `23`; metal avg `0.0065` n `18`; unknown avg `-0.2932` n `645`
- 1h: commodity avg `-0.2284` n `12`; crypto_alt avg `-0.251` n `228`; crypto_major avg `-0.0317` n `8`; equity avg `-0.1596` n `74`; fx avg `-0.0149` n `6`; index avg `-0.0157` n `23`; metal avg `-0.0117` n `18`; unknown avg `0.4543` n `645`
- 4h: commodity avg `-0.1677` n `12`; crypto_alt avg `0.0232` n `228`; crypto_major avg `0.4488` n `8`; equity avg `0.0676` n `74`; fx avg `-0.0249` n `6`; index avg `-0.0246` n `23`; metal avg `-0.0003` n `18`; unknown avg `6.294` n `644`
- 24h: commodity avg `-0.5824` n `12`; crypto_alt avg `2.1214` n `228`; crypto_major avg `1.493` n `8`; equity avg `0.2992` n `74`; fx avg `-0.0183` n `6`; index avg `0.3398` n `23`; metal avg `0.2492` n `18`; unknown avg `1.0296` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal

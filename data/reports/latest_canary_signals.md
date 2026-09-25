# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T16:37:31.097387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0992` n `12`; crypto_alt avg `0.2851` n `234`; crypto_major avg `0.1609` n `8`; equity avg `0.0974` n `141`; fx avg `0.0291` n `6`; index avg `0.0232` n `26`; metal avg `0.0011` n `20`; unknown avg `6.6641` n `960`
- 1h: commodity avg `-0.2933` n `12`; crypto_alt avg `0.7358` n `234`; crypto_major avg `0.4287` n `8`; equity avg `0.391` n `141`; fx avg `-0.0082` n `6`; index avg `0.1119` n `26`; metal avg `0.0705` n `20`; unknown avg `4.0216` n `930`
- 4h: commodity avg `-0.2943` n `12`; crypto_alt avg `-0.1098` n `234`; crypto_major avg `-0.8446` n `8`; equity avg `-0.4983` n `141`; fx avg `-0.062` n `6`; index avg `0.0391` n `26`; metal avg `-0.0374` n `20`; unknown avg `11.537` n `894`
- 24h: commodity avg `-0.5055` n `12`; crypto_alt avg `1.5248` n `234`; crypto_major avg `0.4284` n `8`; equity avg `0.2612` n `141`; fx avg `-0.2272` n `6`; index avg `0.1715` n `26`; metal avg `0.1065` n `20`; unknown avg `1603.4764` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal

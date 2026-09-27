# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T13:22:26.905883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `-0.0589` n `234`; crypto_major avg `-0.0128` n `8`; equity avg `0.0125` n `141`; fx avg `-0.0018` n `6`; index avg `0.0037` n `26`; metal avg `0.0028` n `20`; unknown avg `0.4427` n `962`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.822` n `234`; crypto_major avg `-0.5441` n `8`; equity avg `-0.0535` n `141`; fx avg `0.0061` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0133` n `20`; unknown avg `0.6369` n `960`
- 4h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.5638` n `234`; crypto_major avg `-0.1773` n `8`; equity avg `-0.0081` n `141`; fx avg `-0.0064` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0142` n `20`; unknown avg `2.4462` n `953`
- 24h: commodity avg `0.0713` n `12`; crypto_alt avg `0.3761` n `234`; crypto_major avg `0.5661` n `8`; equity avg `0.3217` n `141`; fx avg `-0.0293` n `6`; index avg `0.0299` n `26`; metal avg `-0.0171` n `20`; unknown avg `77.2693` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal

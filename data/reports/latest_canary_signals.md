# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T06:07:21.924744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.69` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0441` n `12`; crypto_alt avg `-0.0339` n `228`; crypto_major avg `-0.0064` n `8`; equity avg `-0.0111` n `69`; fx avg `0.0014` n `6`; index avg `-0.0239` n `23`; metal avg `0.1507` n `18`; unknown avg `-0.0368` n `412`
- 1h: commodity avg `-0.1104` n `12`; crypto_alt avg `-0.3562` n `228`; crypto_major avg `-0.3961` n `8`; equity avg `0.1321` n `69`; fx avg `0.0024` n `6`; index avg `0.1465` n `23`; metal avg `0.5293` n `18`; unknown avg `0.7951` n `412`
- 4h: commodity avg `-0.2862` n `12`; crypto_alt avg `0.5753` n `228`; crypto_major avg `0.1196` n `8`; equity avg `1.2089` n `69`; fx avg `0.0262` n `6`; index avg `0.4949` n `23`; metal avg `1.3737` n `18`; unknown avg `0.315` n `412`
- 24h: commodity avg `-0.8607` n `12`; crypto_alt avg `-0.7379` n `228`; crypto_major avg `-1.5643` n `8`; equity avg `-0.1581` n `69`; fx avg `0.1064` n `6`; index avg `-0.2936` n `23`; metal avg `0.7763` n `18`; unknown avg `3.0928` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal

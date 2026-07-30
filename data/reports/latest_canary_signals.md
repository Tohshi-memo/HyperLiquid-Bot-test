# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T14:27:49.916565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-4.7713` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-2.5123` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.023` n `12`; crypto_alt avg `0.1319` n `230`; crypto_major avg `0.2439` n `8`; equity avg `0.8454` n `102`; fx avg `-0.0531` n `6`; index avg `0.1225` n `25`; metal avg `-0.0778` n `20`; unknown avg `0.0301` n `779`
- 1h: commodity avg `0.1454` n `12`; crypto_alt avg `0.4902` n `230`; crypto_major avg `0.4553` n `8`; equity avg `2.9676` n `102`; fx avg `-0.318` n `6`; index avg `0.281` n `25`; metal avg `0.0672` n `20`; unknown avg `0.1299` n `779`
- 4h: commodity avg `-0.1123` n `12`; crypto_alt avg `0.3679` n `230`; crypto_major avg `0.3852` n `8`; equity avg `5.1565` n `102`; fx avg `-0.3499` n `6`; index avg `0.5733` n `25`; metal avg `0.0814` n `20`; unknown avg `0.0357` n `779`
- 24h: commodity avg `-0.0671` n `12`; crypto_alt avg `0.6276` n `230`; crypto_major avg `0.7242` n `8`; equity avg `3.8547` n `102`; fx avg `-0.3903` n `6`; index avg `0.349` n `25`; metal avg `0.6623` n `20`; unknown avg `-0.1416` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal

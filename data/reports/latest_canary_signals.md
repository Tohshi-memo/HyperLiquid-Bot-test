# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T16:37:22.443554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1845` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `-0.0392` n `228`; crypto_major avg `-0.0647` n `8`; equity avg `-0.5261` n `66`; fx avg `0.0109` n `5`; index avg `-0.158` n `23`; metal avg `-0.0738` n `18`; unknown avg `1.0003` n `384`
- 1h: commodity avg `0.2412` n `12`; crypto_alt avg `0.4282` n `228`; crypto_major avg `0.09` n `8`; equity avg `-0.4851` n `66`; fx avg `0.0032` n `5`; index avg `-0.0897` n `23`; metal avg `0.063` n `18`; unknown avg `0.8348` n `384`
- 4h: commodity avg `0.7956` n `12`; crypto_alt avg `-1.0654` n `228`; crypto_major avg `-1.3889` n `8`; equity avg `-2.0571` n `66`; fx avg `0.0009` n `5`; index avg `-0.6793` n `23`; metal avg `-0.101` n `18`; unknown avg `1.1622` n `383`
- 24h: commodity avg `1.0399` n `12`; crypto_alt avg `-2.7451` n `228`; crypto_major avg `-2.1294` n `8`; equity avg `-1.1807` n `66`; fx avg `0.0657` n `5`; index avg `-0.5372` n `23`; metal avg `0.4686` n `18`; unknown avg `-0.4349` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal

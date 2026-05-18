# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T03:07:13.260520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.3832` n `228`; crypto_major avg `0.3298` n `8`; equity avg `0.0763` n `66`; fx avg `0.0035` n `5`; index avg `0.0967` n `23`; metal avg `-0.0853` n `18`; unknown avg `0.2665` n `383`
- 1h: commodity avg `-0.1108` n `12`; crypto_alt avg `0.2638` n `228`; crypto_major avg `-0.1092` n `8`; equity avg `0.2333` n `66`; fx avg `-0.0072` n `5`; index avg `0.0664` n `23`; metal avg `0.1276` n `18`; unknown avg `-0.1243` n `383`
- 4h: commodity avg `0.7832` n `12`; crypto_alt avg `-0.7413` n `228`; crypto_major avg `-1.0616` n `8`; equity avg `-0.1939` n `66`; fx avg `0.0969` n `5`; index avg `-0.2907` n `23`; metal avg `-1.0832` n `18`; unknown avg `-0.4517` n `383`
- 24h: commodity avg `2.681` n `12`; crypto_alt avg `-10.5589` n `228`; crypto_major avg `-3.1294` n `8`; equity avg `-3.0037` n `65`; fx avg `-0.0759` n `5`; index avg `-1.823` n `23`; metal avg `-6.3924` n `18`; unknown avg `550.2818` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal

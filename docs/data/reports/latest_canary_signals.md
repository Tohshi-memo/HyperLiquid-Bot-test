# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T08:22:27.960160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `0.0026` n `228`; crypto_major avg `0.0281` n `8`; equity avg `0.0514` n `79`; fx avg `0.0162` n `6`; index avg `0.0246` n `23`; metal avg `-0.0099` n `18`; unknown avg `0.0159` n `701`
- 1h: commodity avg `0.1774` n `12`; crypto_alt avg `-0.153` n `228`; crypto_major avg `0.0755` n `8`; equity avg `-0.2026` n `79`; fx avg `-0.0257` n `6`; index avg `-0.0205` n `23`; metal avg `-0.2408` n `18`; unknown avg `-0.0803` n `693`
- 4h: commodity avg `0.1922` n `12`; crypto_alt avg `0.3661` n `228`; crypto_major avg `0.8291` n `8`; equity avg `0.3102` n `79`; fx avg `0.0037` n `6`; index avg `0.0475` n `23`; metal avg `0.2269` n `18`; unknown avg `0.1074` n `661`
- 24h: commodity avg `-0.0482` n `12`; crypto_alt avg `0.1087` n `228`; crypto_major avg `0.349` n `8`; equity avg `-0.3393` n `79`; fx avg `0.0149` n `6`; index avg `0.009` n `23`; metal avg `0.2917` n `18`; unknown avg `0.0601` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal

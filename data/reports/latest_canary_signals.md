# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T15:07:17.292249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2197` n `12`; crypto_alt avg `0.2238` n `228`; crypto_major avg `0.1172` n `8`; equity avg `0.0177` n `67`; fx avg `-0.0143` n `6`; index avg `-0.0132` n `23`; metal avg `0.2365` n `18`; unknown avg `0.0824` n `405`
- 1h: commodity avg `0.0177` n `12`; crypto_alt avg `0.4665` n `228`; crypto_major avg `0.1489` n `8`; equity avg `0.0732` n `67`; fx avg `-0.0108` n `6`; index avg `-0.0461` n `23`; metal avg `0.2753` n `18`; unknown avg `-0.1812` n `405`
- 4h: commodity avg `0.3811` n `12`; crypto_alt avg `0.6917` n `228`; crypto_major avg `0.4137` n `8`; equity avg `0.1486` n `67`; fx avg `-0.0153` n `6`; index avg `0.053` n `23`; metal avg `0.3029` n `18`; unknown avg `-0.0166` n `397`
- 24h: commodity avg `-0.7263` n `12`; crypto_alt avg `2.5192` n `228`; crypto_major avg `1.214` n `8`; equity avg `0.9607` n `67`; fx avg `-0.007` n `6`; index avg `0.3924` n `23`; metal avg `1.5923` n `18`; unknown avg `1.008` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal

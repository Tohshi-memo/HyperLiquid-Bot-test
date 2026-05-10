# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T10:52:13.065320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.0736` n `228`; crypto_major avg `0.0677` n `8`; equity avg `-0.0467` n `65`; fx avg `0.0008` n `5`; index avg `0.0139` n `23`; metal avg `0.0083` n `18`; unknown avg `0.3606` n `376`
- 1h: commodity avg `0.0682` n `12`; crypto_alt avg `-0.1112` n `228`; crypto_major avg `-0.1312` n `8`; equity avg `-0.0177` n `65`; fx avg `0.0008` n `5`; index avg `0.028` n `23`; metal avg `0.0233` n `18`; unknown avg `0.2886` n `376`
- 4h: commodity avg `-0.0311` n `12`; crypto_alt avg `0.5235` n `228`; crypto_major avg `0.1442` n `8`; equity avg `-0.0555` n `65`; fx avg `0.0104` n `5`; index avg `0.0238` n `23`; metal avg `0.0256` n `18`; unknown avg `0.4516` n `376`
- 24h: commodity avg `0.1649` n `12`; crypto_alt avg `-0.1534` n `228`; crypto_major avg `-0.042` n `8`; equity avg `0.8836` n `65`; fx avg `-0.0191` n `5`; index avg `0.3115` n `23`; metal avg `0.4376` n `18`; unknown avg `0.2176` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T01:22:20.242248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0742` n `12`; crypto_alt avg `0.1174` n `228`; crypto_major avg `0.0787` n `8`; equity avg `0.0348` n `69`; fx avg `0.0012` n `6`; index avg `0.0169` n `23`; metal avg `0.0179` n `18`; unknown avg `0.1721` n `421`
- 1h: commodity avg `0.11` n `12`; crypto_alt avg `0.2072` n `228`; crypto_major avg `0.2907` n `8`; equity avg `0.1118` n `69`; fx avg `-0.0017` n `6`; index avg `0.0394` n `23`; metal avg `0.0176` n `18`; unknown avg `0.2269` n `421`
- 4h: commodity avg `0.1959` n `12`; crypto_alt avg `-0.346` n `228`; crypto_major avg `0.3192` n `8`; equity avg `0.1955` n `69`; fx avg `-0.008` n `6`; index avg `-0.0217` n `23`; metal avg `-0.0084` n `18`; unknown avg `-0.4195` n `421`
- 24h: commodity avg `-0.0659` n `12`; crypto_alt avg `0.562` n `228`; crypto_major avg `2.4707` n `8`; equity avg `1.0189` n `69`; fx avg `0.0316` n `6`; index avg `0.0696` n `23`; metal avg `0.0244` n `18`; unknown avg `0.4407` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal

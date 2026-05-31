# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T12:07:23.280325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.0672` n `228`; crypto_major avg `-0.078` n `8`; equity avg `-0.0302` n `69`; fx avg `0.01` n `6`; index avg `0.0329` n `23`; metal avg `0.0099` n `18`; unknown avg `-0.0956` n `421`
- 1h: commodity avg `0.0311` n `12`; crypto_alt avg `-0.1456` n `228`; crypto_major avg `-0.0553` n `8`; equity avg `-0.0365` n `69`; fx avg `0.0134` n `6`; index avg `-0.0761` n `23`; metal avg `0.0076` n `18`; unknown avg `0.7228` n `421`
- 4h: commodity avg `0.1266` n `12`; crypto_alt avg `-0.0911` n `228`; crypto_major avg `-0.3286` n `8`; equity avg `-0.1526` n `69`; fx avg `-0.0092` n `6`; index avg `-0.1703` n `23`; metal avg `-0.0244` n `18`; unknown avg `-0.2411` n `421`
- 24h: commodity avg `0.1714` n `12`; crypto_alt avg `0.0438` n `228`; crypto_major avg `1.0372` n `8`; equity avg `0.9361` n `69`; fx avg `0.007` n `6`; index avg `-0.141` n `23`; metal avg `-0.0558` n `18`; unknown avg `0.2959` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal

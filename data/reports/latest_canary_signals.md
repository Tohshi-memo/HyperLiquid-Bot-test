# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T13:22:26.567699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.49` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.09` n `12`; crypto_alt avg `0.1526` n `228`; crypto_major avg `0.0622` n `8`; equity avg `0.114` n `69`; fx avg `0.0011` n `6`; index avg `-0.0131` n `23`; metal avg `-0.3452` n `18`; unknown avg `-0.1135` n `422`
- 1h: commodity avg `-0.0054` n `12`; crypto_alt avg `0.5801` n `228`; crypto_major avg `0.0736` n `8`; equity avg `-0.1073` n `69`; fx avg `0.0073` n `6`; index avg `-0.0423` n `23`; metal avg `-0.3953` n `18`; unknown avg `0.1995` n `422`
- 4h: commodity avg `0.0564` n `12`; crypto_alt avg `1.1431` n `228`; crypto_major avg `0.2884` n `8`; equity avg `0.0903` n `69`; fx avg `0.03` n `6`; index avg `0.037` n `23`; metal avg `-0.4183` n `18`; unknown avg `0.1625` n `422`
- 24h: commodity avg `-0.8698` n `12`; crypto_alt avg `0.9156` n `228`; crypto_major avg `-1.4413` n `8`; equity avg `1.3022` n `69`; fx avg `0.1636` n `6`; index avg `0.3579` n `23`; metal avg `1.1936` n `18`; unknown avg `0.0214` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal

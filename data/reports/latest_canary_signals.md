# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T10:37:26.962318+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.2513` n `228`; crypto_major avg `-0.094` n `8`; equity avg `0.1167` n `69`; fx avg `-0.0029` n `6`; index avg `0.0461` n `23`; metal avg `0.1285` n `18`; unknown avg `-0.0468` n `422`
- 1h: commodity avg `-0.0912` n `12`; crypto_alt avg `-0.1412` n `228`; crypto_major avg `-0.2431` n `8`; equity avg `0.1338` n `69`; fx avg `0.0153` n `6`; index avg `0.1032` n `23`; metal avg `0.2317` n `18`; unknown avg `0.3026` n `422`
- 4h: commodity avg `0.0176` n `12`; crypto_alt avg `-0.4438` n `228`; crypto_major avg `-0.2324` n `8`; equity avg `-0.1119` n `69`; fx avg `0.0457` n `6`; index avg `-0.0202` n `23`; metal avg `0.2454` n `18`; unknown avg `0.4327` n `422`
- 24h: commodity avg `1.1369` n `12`; crypto_alt avg `-0.4581` n `228`; crypto_major avg `-0.6715` n `8`; equity avg `-0.0081` n `69`; fx avg `-0.0063` n `6`; index avg `0.5431` n `23`; metal avg `0.3617` n `18`; unknown avg `2.3165` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.287`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal

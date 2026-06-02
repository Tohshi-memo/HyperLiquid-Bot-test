# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T13:07:23.855171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `0.1444` n `228`; crypto_major avg `-0.0749` n `8`; equity avg `-0.1536` n `69`; fx avg `0.0107` n `6`; index avg `-0.049` n `23`; metal avg `0.0015` n `18`; unknown avg `-0.0155` n `422`
- 1h: commodity avg `-0.1764` n `12`; crypto_alt avg `0.4467` n `228`; crypto_major avg `-0.047` n `8`; equity avg `-0.0929` n `69`; fx avg `0.0063` n `6`; index avg `0.0126` n `23`; metal avg `0.0691` n `18`; unknown avg `0.9079` n `422`
- 4h: commodity avg `-0.1627` n `12`; crypto_alt avg `0.5481` n `228`; crypto_major avg `-0.0338` n `8`; equity avg `-0.0218` n `69`; fx avg `0.0287` n `6`; index avg `0.0297` n `23`; metal avg `-0.1219` n `18`; unknown avg `0.838` n `422`
- 24h: commodity avg `-0.3576` n `12`; crypto_alt avg `0.9843` n `228`; crypto_major avg `-1.5379` n `8`; equity avg `0.7735` n `69`; fx avg `0.1702` n `6`; index avg `0.2122` n `23`; metal avg `0.8856` n `18`; unknown avg `0.1024` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal

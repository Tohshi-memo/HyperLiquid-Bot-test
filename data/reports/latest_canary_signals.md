# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T09:52:18.097950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0543` n `12`; crypto_alt avg `0.0274` n `228`; crypto_major avg `-0.0047` n `8`; equity avg `0.0085` n `69`; fx avg `0.0` n `6`; index avg `-0.0085` n `23`; metal avg `-0.011` n `18`; unknown avg `0.1967` n `421`
- 1h: commodity avg `-0.0571` n `12`; crypto_alt avg `0.2717` n `228`; crypto_major avg `-0.019` n `8`; equity avg `-0.0062` n `69`; fx avg `-0.0012` n `6`; index avg `-0.0255` n `23`; metal avg `-0.0212` n `18`; unknown avg `-0.199` n `421`
- 4h: commodity avg `0.0606` n `12`; crypto_alt avg `-0.2986` n `228`; crypto_major avg `-0.6247` n `8`; equity avg `0.2928` n `69`; fx avg `0.0006` n `6`; index avg `-0.1086` n `23`; metal avg `-0.0408` n `18`; unknown avg `0.1194` n `401`
- 24h: commodity avg `0.2314` n `12`; crypto_alt avg `0.2472` n `228`; crypto_major avg `1.4548` n `8`; equity avg `1.1532` n `69`; fx avg `0.0205` n `6`; index avg `-0.0799` n `23`; metal avg `-0.0777` n `18`; unknown avg `0.9328` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal

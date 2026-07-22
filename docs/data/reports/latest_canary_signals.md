# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T20:22:30.623554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `0.1587` n `230`; crypto_major avg `0.1915` n `8`; equity avg `0.6196` n `98`; fx avg `0.0068` n `6`; index avg `0.0868` n `25`; metal avg `0.0498` n `20`; unknown avg `0.1455` n `773`
- 1h: commodity avg `-0.085` n `12`; crypto_alt avg `0.0803` n `230`; crypto_major avg `0.0095` n `8`; equity avg `0.2436` n `98`; fx avg `0.0024` n `6`; index avg `0.0452` n `25`; metal avg `0.0362` n `20`; unknown avg `0.1096` n `773`
- 4h: commodity avg `0.13` n `12`; crypto_alt avg `-0.2172` n `230`; crypto_major avg `0.0241` n `8`; equity avg `-0.3281` n `98`; fx avg `0.0153` n `6`; index avg `-0.0362` n `25`; metal avg `-0.1043` n `20`; unknown avg `0.1303` n `773`
- 24h: commodity avg `0.4806` n `12`; crypto_alt avg `-0.3863` n `230`; crypto_major avg `-0.5059` n `8`; equity avg `-0.6271` n `98`; fx avg `-0.0551` n `6`; index avg `-0.0742` n `25`; metal avg `0.3012` n `20`; unknown avg `1.5006` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0897`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T13:22:34.901412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0938` n `12`; crypto_alt avg `-0.0655` n `230`; crypto_major avg `-0.078` n `8`; equity avg `-0.1994` n `100`; fx avg `-0.0111` n `6`; index avg `-0.0392` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.0971` n `772`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `-0.6234` n `230`; crypto_major avg `-0.8282` n `8`; equity avg `-0.8327` n `99`; fx avg `0.0038` n `6`; index avg `-0.1753` n `25`; metal avg `-0.2299` n `20`; unknown avg `-0.0003` n `772`
- 4h: commodity avg `0.0914` n `12`; crypto_alt avg `-0.6718` n `230`; crypto_major avg `-0.8844` n `8`; equity avg `-1.7692` n `99`; fx avg `-0.0105` n `6`; index avg `-0.3364` n `25`; metal avg `-0.4293` n `20`; unknown avg `0.1109` n `772`
- 24h: commodity avg `0.9259` n `12`; crypto_alt avg `-0.7608` n `230`; crypto_major avg `-0.5958` n `8`; equity avg `-0.7325` n `99`; fx avg `-0.0949` n `6`; index avg `-0.1442` n `25`; metal avg `-0.7808` n `20`; unknown avg `9.5565` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal

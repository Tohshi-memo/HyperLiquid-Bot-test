# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T14:37:35.087641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `0.0888` n `230`; crypto_major avg `0.1327` n `8`; equity avg `-0.0638` n `100`; fx avg `-0.0043` n `6`; index avg `0.0282` n `25`; metal avg `0.0209` n `20`; unknown avg `0.0744` n `772`
- 1h: commodity avg `0.1346` n `12`; crypto_alt avg `0.2111` n `230`; crypto_major avg `0.1566` n `8`; equity avg `0.2833` n `100`; fx avg `0.0026` n `6`; index avg `-0.0543` n `25`; metal avg `-0.0501` n `20`; unknown avg `0.0219` n `772`
- 4h: commodity avg `0.1863` n `12`; crypto_alt avg `-0.2533` n `230`; crypto_major avg `-0.8643` n `8`; equity avg `-0.8687` n `99`; fx avg `-0.0044` n `6`; index avg `-0.284` n `25`; metal avg `-0.3202` n `20`; unknown avg `0.095` n `772`
- 24h: commodity avg `0.9402` n `12`; crypto_alt avg `-0.6834` n `230`; crypto_major avg `-0.9165` n `8`; equity avg `-0.8709` n `99`; fx avg `-0.0824` n `6`; index avg `-0.2153` n `25`; metal avg `-0.8509` n `20`; unknown avg `-0.103` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0641`, n `666`, weak_sample_signal

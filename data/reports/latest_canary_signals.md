# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T12:52:29.638130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0071` n `230`; crypto_major avg `-0.0263` n `8`; equity avg `0.0306` n `96`; fx avg `0.0` n `6`; index avg `0.0011` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0043` n `770`
- 1h: commodity avg `0.0382` n `12`; crypto_alt avg `-0.0045` n `230`; crypto_major avg `-0.0842` n `8`; equity avg `0.0116` n `96`; fx avg `0.0048` n `6`; index avg `-0.0108` n `25`; metal avg `-0.0165` n `20`; unknown avg `-0.0301` n `770`
- 4h: commodity avg `0.0304` n `12`; crypto_alt avg `-0.2899` n `230`; crypto_major avg `-0.2876` n `8`; equity avg `-0.1826` n `96`; fx avg `-0.0023` n `6`; index avg `-0.0136` n `25`; metal avg `-0.0419` n `20`; unknown avg `-0.0638` n `770`
- 24h: commodity avg `0.207` n `12`; crypto_alt avg `0.2511` n `230`; crypto_major avg `0.8062` n `8`; equity avg `0.2442` n `96`; fx avg `-0.0091` n `6`; index avg `-0.0281` n `25`; metal avg `-0.0999` n `20`; unknown avg `0.1064` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1161`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1149`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.097`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0864`, n `666`, weak_sample_signal

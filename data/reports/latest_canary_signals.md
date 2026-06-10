# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T10:52:29.775643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1038` n `12`; crypto_alt avg `0.0341` n `228`; crypto_major avg `0.0131` n `8`; equity avg `0.0695` n `74`; fx avg `0.0031` n `6`; index avg `-0.114` n `23`; metal avg `0.2049` n `18`; unknown avg `0.0944` n `547`
- 1h: commodity avg `-0.0475` n `12`; crypto_alt avg `0.2261` n `228`; crypto_major avg `0.2165` n `8`; equity avg `0.1222` n `74`; fx avg `-0.0202` n `6`; index avg `-0.0706` n `23`; metal avg `0.3332` n `18`; unknown avg `-0.0261` n `547`
- 4h: commodity avg `0.4043` n `12`; crypto_alt avg `-0.1228` n `228`; crypto_major avg `-0.0533` n `8`; equity avg `-0.7351` n `74`; fx avg `-0.0084` n `6`; index avg `-0.4849` n `23`; metal avg `-0.39` n `18`; unknown avg `0.2001` n `547`
- 24h: commodity avg `-0.262` n `12`; crypto_alt avg `-1.3043` n `228`; crypto_major avg `-3.469` n `8`; equity avg `-4.1377` n `74`; fx avg `-0.03` n `6`; index avg `-2.3866` n `23`; metal avg `-3.2546` n `18`; unknown avg `0.3569` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T17:52:32.157075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `-0.0323` n `230`; crypto_major avg `0.074` n `8`; equity avg `0.016` n `113`; fx avg `-0.0013` n `6`; index avg `0.0004` n `25`; metal avg `0.0153` n `20`; unknown avg `0.0479` n `785`
- 1h: commodity avg `0.1072` n `12`; crypto_alt avg `-0.0149` n `230`; crypto_major avg `0.2728` n `8`; equity avg `-0.0373` n `113`; fx avg `0.0009` n `6`; index avg `-0.0125` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.0141` n `785`
- 4h: commodity avg `0.2977` n `12`; crypto_alt avg `-1.1706` n `230`; crypto_major avg `-0.4029` n `8`; equity avg `0.2267` n `113`; fx avg `0.0298` n `6`; index avg `-0.0335` n `25`; metal avg `-0.0902` n `20`; unknown avg `0.0044` n `785`
- 24h: commodity avg `0.2117` n `12`; crypto_alt avg `-2.0204` n `230`; crypto_major avg `-0.0988` n `8`; equity avg `0.0695` n `113`; fx avg `-0.0648` n `6`; index avg `0.0766` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.2824` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal

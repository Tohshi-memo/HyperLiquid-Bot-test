# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T19:12:11.283737+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `0.4063` n `230`; crypto_major avg `0.3562` n `8`; equity avg `0.0283` n `121`; fx avg `0.0045` n `6`; index avg `0.0013` n `25`; metal avg `0.0004` n `20`; unknown avg `0.1937` n `794`
- 1h: commodity avg `-0.007` n `12`; crypto_alt avg `-0.1497` n `230`; crypto_major avg `0.0957` n `8`; equity avg `0.0111` n `121`; fx avg `0.0163` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.443` n `794`
- 4h: commodity avg `0.0339` n `12`; crypto_alt avg `0.9328` n `230`; crypto_major avg `1.5053` n `8`; equity avg `0.0764` n `121`; fx avg `0.0339` n `6`; index avg `0.0031` n `25`; metal avg `0.0122` n `20`; unknown avg `1.378` n `794`
- 24h: commodity avg `-0.0377` n `12`; crypto_alt avg `1.8466` n `230`; crypto_major avg `4.28` n `8`; equity avg `-0.3623` n `121`; fx avg `0.0571` n `6`; index avg `-0.0531` n `25`; metal avg `-0.1138` n `20`; unknown avg `1.9857` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal

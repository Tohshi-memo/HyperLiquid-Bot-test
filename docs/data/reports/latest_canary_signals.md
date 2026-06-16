# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T16:07:45.104812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0839` n `12`; crypto_alt avg `0.0457` n `228`; crypto_major avg `0.0208` n `8`; equity avg `0.1909` n `77`; fx avg `0.0124` n `6`; index avg `0.1984` n `23`; metal avg `0.201` n `18`; unknown avg `-0.0218` n `687`
- 1h: commodity avg `-0.4124` n `12`; crypto_alt avg `0.3215` n `228`; crypto_major avg `0.1068` n `8`; equity avg `-0.0524` n `77`; fx avg `0.029` n `6`; index avg `-0.0629` n `23`; metal avg `0.2356` n `18`; unknown avg `0.63` n `687`
- 4h: commodity avg `-0.1634` n `12`; crypto_alt avg `-1.3648` n `228`; crypto_major avg `-1.2168` n `8`; equity avg `-1.266` n `77`; fx avg `0.0654` n `6`; index avg `-0.6983` n `23`; metal avg `-0.1921` n `18`; unknown avg `0.8446` n `687`
- 24h: commodity avg `-0.6743` n `12`; crypto_alt avg `-2.4333` n `228`; crypto_major avg `-1.083` n `8`; equity avg `-0.9468` n `77`; fx avg `-0.0081` n `6`; index avg `-0.7118` n `23`; metal avg `-0.0063` n `18`; unknown avg `0.5133` n `623`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal

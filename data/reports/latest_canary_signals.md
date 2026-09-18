# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T22:37:24.680410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `-0.3704` n `234`; crypto_major avg `-0.3377` n `8`; equity avg `-0.0519` n `140`; fx avg `-0.0039` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.2461` n `942`
- 1h: commodity avg `0.0049` n `12`; crypto_alt avg `-0.3874` n `234`; crypto_major avg `-0.2527` n `8`; equity avg `-0.0095` n `140`; fx avg `-0.0178` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0085` n `20`; unknown avg `15.9704` n `922`
- 4h: commodity avg `-0.0829` n `12`; crypto_alt avg `0.675` n `234`; crypto_major avg `0.083` n `8`; equity avg `0.6299` n `140`; fx avg `0.0384` n `6`; index avg `0.1083` n `26`; metal avg `-0.0841` n `20`; unknown avg `0.4361` n `872`
- 24h: commodity avg `-0.0845` n `12`; crypto_alt avg `6.8173` n `234`; crypto_major avg `6.7438` n `8`; equity avg `1.372` n `140`; fx avg `0.2305` n `6`; index avg `0.0603` n `26`; metal avg `0.3526` n `20`; unknown avg `4.085` n `757`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal

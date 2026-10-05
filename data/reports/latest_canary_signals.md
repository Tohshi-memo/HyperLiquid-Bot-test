# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T16:12:37.555775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0342` n `13`; crypto_alt avg `-0.0008` n `235`; crypto_major avg `-0.0029` n `8`; equity avg `-0.0608` n `144`; fx avg `-0.0123` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0442` n `20`; unknown avg `0.1119` n `1071`
- 1h: commodity avg `-0.1989` n `13`; crypto_alt avg `-0.2347` n `235`; crypto_major avg `-0.2859` n `8`; equity avg `0.0218` n `144`; fx avg `-0.0274` n `6`; index avg `0.0124` n `26`; metal avg `-0.0509` n `20`; unknown avg `-0.1006` n `1071`
- 4h: commodity avg `-0.0601` n `13`; crypto_alt avg `-1.1593` n `235`; crypto_major avg `-0.7957` n `8`; equity avg `0.1829` n `144`; fx avg `-0.0571` n `6`; index avg `0.0967` n `26`; metal avg `-0.1635` n `20`; unknown avg `0.6277` n `989`
- 24h: commodity avg `-0.2491` n `13`; crypto_alt avg `0.0305` n `235`; crypto_major avg `0.1984` n `8`; equity avg `0.2671` n `144`; fx avg `-0.1084` n `6`; index avg `0.0812` n `26`; metal avg `0.1451` n `20`; unknown avg `-0.2892` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2028`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T15:07:31.572733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0594` n `12`; crypto_alt avg `-0.5141` n `232`; crypto_major avg `-0.611` n `8`; equity avg `-0.0566` n `131`; fx avg `-0.0005` n `6`; index avg `-0.0488` n `26`; metal avg `-0.0258` n `20`; unknown avg `-0.169` n `790`
- 1h: commodity avg `0.0543` n `12`; crypto_alt avg `-0.5182` n `232`; crypto_major avg `-0.7253` n `8`; equity avg `0.155` n `131`; fx avg `-0.0078` n `6`; index avg `0.0172` n `26`; metal avg `-0.0344` n `20`; unknown avg `-0.4202` n `790`
- 4h: commodity avg `-0.0441` n `12`; crypto_alt avg `0.0323` n `232`; crypto_major avg `-0.4237` n `8`; equity avg `-0.4324` n `130`; fx avg `-0.0215` n `6`; index avg `0.0071` n `26`; metal avg `-0.0531` n `20`; unknown avg `-0.2369` n `790`
- 24h: commodity avg `0.364` n `12`; crypto_alt avg `0.831` n `232`; crypto_major avg `-0.4857` n `8`; equity avg `-1.0288` n `130`; fx avg `0.0338` n `6`; index avg `-0.1813` n `26`; metal avg `-0.5589` n `20`; unknown avg `-0.0863` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0414`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0357`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0321`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0305`, n `668`, weak_sample_signal

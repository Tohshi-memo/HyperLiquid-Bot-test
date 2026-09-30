# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T09:07:29.691956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `0.1738` n `234`; crypto_major avg `0.1651` n `8`; equity avg `-0.037` n `142`; fx avg `0.0169` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0173` n `20`; unknown avg `0.2526` n `961`
- 1h: commodity avg `0.221` n `12`; crypto_alt avg `0.7312` n `234`; crypto_major avg `0.2688` n `8`; equity avg `-0.1693` n `142`; fx avg `0.0401` n `6`; index avg `-0.0537` n `26`; metal avg `-0.0745` n `20`; unknown avg `-0.0597` n `961`
- 4h: commodity avg `0.129` n `12`; crypto_alt avg `0.5796` n `234`; crypto_major avg `0.1097` n `8`; equity avg `0.0004` n `142`; fx avg `0.0407` n `6`; index avg `0.0085` n `26`; metal avg `0.0933` n `20`; unknown avg `0.4076` n `915`
- 24h: commodity avg `-0.4243` n `12`; crypto_alt avg `0.4455` n `234`; crypto_major avg `-0.6373` n `8`; equity avg `0.2549` n `142`; fx avg `-0.0242` n `6`; index avg `0.0693` n `26`; metal avg `0.2588` n `20`; unknown avg `2917.3887` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T18:37:26.531315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `-0.0233` n `233`; crypto_major avg `0.0027` n `8`; equity avg `0.0202` n `136`; fx avg `0.0078` n `6`; index avg `-0.0023` n `27`; metal avg `0.003` n `20`; unknown avg `0.7304` n `840`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.1412` n `233`; crypto_major avg `0.0898` n `8`; equity avg `0.0714` n `136`; fx avg `0.0007` n `6`; index avg `0.0054` n `27`; metal avg `-0.0043` n `20`; unknown avg `2.6451` n `838`
- 4h: commodity avg `0.1166` n `12`; crypto_alt avg `0.1003` n `233`; crypto_major avg `0.3959` n `8`; equity avg `0.2293` n `136`; fx avg `0.001` n `6`; index avg `-0.0126` n `27`; metal avg `-0.0002` n `20`; unknown avg `1.7273` n `774`
- 24h: commodity avg `0.2407` n `12`; crypto_alt avg `0.1013` n `233`; crypto_major avg `-0.6218` n `8`; equity avg `-1.3549` n `136`; fx avg `0.0169` n `6`; index avg `-0.2623` n `26`; metal avg `-0.0746` n `20`; unknown avg `1.3926` n `720`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal

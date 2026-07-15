# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T08:22:27.768605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `12`; crypto_alt avg `0.1211` n `230`; crypto_major avg `0.0875` n `8`; equity avg `-0.1554` n `93`; fx avg `0.0119` n `6`; index avg `-0.0169` n `25`; metal avg `-0.0084` n `20`; unknown avg `0.025` n `767`
- 1h: commodity avg `0.0205` n `12`; crypto_alt avg `-0.0048` n `230`; crypto_major avg `-0.0988` n `8`; equity avg `-0.3887` n `93`; fx avg `0.0141` n `6`; index avg `-0.0627` n `25`; metal avg `-0.0382` n `20`; unknown avg `-0.009` n `765`
- 4h: commodity avg `0.0663` n `12`; crypto_alt avg `-0.2801` n `230`; crypto_major avg `-0.1768` n `8`; equity avg `-0.6848` n `93`; fx avg `0.0046` n `6`; index avg `-0.1283` n `25`; metal avg `-0.0504` n `20`; unknown avg `-0.0696` n `747`
- 24h: commodity avg `0.0752` n `12`; crypto_alt avg `1.3592` n `230`; crypto_major avg `2.9831` n `8`; equity avg `1.0559` n `92`; fx avg `0.0756` n `6`; index avg `0.3929` n `25`; metal avg `0.2758` n `20`; unknown avg `0.2193` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal

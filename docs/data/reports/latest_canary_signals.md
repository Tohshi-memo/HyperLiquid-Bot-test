# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T07:22:35.046611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `13`; crypto_alt avg `0.1403` n `235`; crypto_major avg `0.0068` n `8`; equity avg `0.0634` n `149`; fx avg `0.0226` n `6`; index avg `0.025` n `26`; metal avg `0.0597` n `20`; unknown avg `0.076` n `1066`
- 1h: commodity avg `-0.0477` n `13`; crypto_alt avg `0.3382` n `235`; crypto_major avg `0.1393` n `8`; equity avg `-0.0027` n `149`; fx avg `0.0201` n `6`; index avg `-0.0052` n `26`; metal avg `0.0232` n `20`; unknown avg `0.1022` n `1008`
- 4h: commodity avg `-0.2724` n `13`; crypto_alt avg `0.1535` n `235`; crypto_major avg `-0.2525` n `8`; equity avg `0.0975` n `149`; fx avg `0.0219` n `6`; index avg `0.0436` n `26`; metal avg `-0.0261` n `20`; unknown avg `0.0031` n `986`
- 24h: commodity avg `-0.36` n `13`; crypto_alt avg `-1.295` n `235`; crypto_major avg `-0.9253` n `8`; equity avg `0.227` n `149`; fx avg `0.063` n `6`; index avg `0.1572` n `26`; metal avg `-0.1029` n `20`; unknown avg `-0.2136` n `830`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal

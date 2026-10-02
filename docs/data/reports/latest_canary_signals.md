# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T16:07:34.657984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.64` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7443` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4106` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `0.2528` n `235`; crypto_major avg `0.0678` n `8`; equity avg `0.0809` n `143`; fx avg `0.0096` n `6`; index avg `0.0086` n `26`; metal avg `0.0109` n `20`; unknown avg `0.0438` n `976`
- 1h: commodity avg `0.2238` n `13`; crypto_alt avg `0.5281` n `235`; crypto_major avg `0.0409` n `8`; equity avg `-0.1127` n `143`; fx avg `-0.0143` n `6`; index avg `-0.0116` n `26`; metal avg `-0.1505` n `20`; unknown avg `6.8004` n `976`
- 4h: commodity avg `0.2536` n `13`; crypto_alt avg `0.0532` n `235`; crypto_major avg `-1.2587` n `8`; equity avg `0.4856` n `142`; fx avg `0.0591` n `6`; index avg `0.1519` n `26`; metal avg `-0.3854` n `20`; unknown avg `0.9756` n `934`
- 24h: commodity avg `-0.3294` n `13`; crypto_alt avg `2.3482` n `235`; crypto_major avg `1.1583` n `8`; equity avg `1.7542` n `142`; fx avg `-0.1389` n `6`; index avg `0.4992` n `26`; metal avg `-0.3035` n `20`; unknown avg `101.7198` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T12:15:21.154113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `0.0315` n `230`; crypto_major avg `0.0218` n `8`; equity avg `0.0273` n `102`; fx avg `0.0022` n `6`; index avg `0.0032` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0081` n `782`
- 1h: commodity avg `0.0615` n `12`; crypto_alt avg `0.0325` n `230`; crypto_major avg `-0.1321` n `8`; equity avg `-0.1767` n `102`; fx avg `-0.0052` n `6`; index avg `-0.0388` n `25`; metal avg `-0.0194` n `20`; unknown avg `-0.0312` n `782`
- 4h: commodity avg `0.2581` n `12`; crypto_alt avg `-0.2421` n `230`; crypto_major avg `-0.5481` n `8`; equity avg `-0.3732` n `102`; fx avg `0.004` n `6`; index avg `-0.0845` n `25`; metal avg `-0.0338` n `20`; unknown avg `-0.0207` n `782`
- 24h: commodity avg `-0.9722` n `12`; crypto_alt avg `0.1269` n `230`; crypto_major avg `0.0181` n `8`; equity avg `0.6904` n `102`; fx avg `-0.0746` n `6`; index avg `0.2063` n `25`; metal avg `0.2244` n `20`; unknown avg `0.2284` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal

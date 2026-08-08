# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T15:41:26.253594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.118` n `230`; crypto_major avg `-0.0408` n `8`; equity avg `-0.0637` n `112`; fx avg `-0.0005` n `6`; index avg `0.0159` n `25`; metal avg `0.0002` n `20`; unknown avg `0.0157` n `784`
- 1h: commodity avg `-0.0532` n `12`; crypto_alt avg `0.1728` n `230`; crypto_major avg `-0.1014` n `8`; equity avg `0.0072` n `112`; fx avg `0.0017` n `6`; index avg `0.0232` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.2644` n `784`
- 4h: commodity avg `-0.0247` n `12`; crypto_alt avg `0.7395` n `230`; crypto_major avg `0.6112` n `8`; equity avg `0.173` n `112`; fx avg `-0.0008` n `6`; index avg `0.0411` n `25`; metal avg `-0.0238` n `20`; unknown avg `-0.2065` n `784`
- 24h: commodity avg `-0.2175` n `12`; crypto_alt avg `1.0074` n `230`; crypto_major avg `0.8547` n `8`; equity avg `0.4587` n `112`; fx avg `-0.0007` n `6`; index avg `0.0386` n `25`; metal avg `0.067` n `20`; unknown avg `-0.1005` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal

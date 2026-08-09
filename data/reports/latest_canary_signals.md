# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T11:07:24.471562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0404` n `12`; crypto_alt avg `-0.0004` n `230`; crypto_major avg `-0.0002` n `8`; equity avg `-0.0035` n `112`; fx avg `-0.0052` n `6`; index avg `-0.0018` n `25`; metal avg `0.0091` n `20`; unknown avg `-0.0167` n `785`
- 1h: commodity avg `-0.0365` n `12`; crypto_alt avg `-0.0094` n `230`; crypto_major avg `0.0612` n `8`; equity avg `0.0255` n `112`; fx avg `-0.0003` n `6`; index avg `0.0017` n `25`; metal avg `0.0097` n `20`; unknown avg `0.0167` n `785`
- 4h: commodity avg `0.0607` n `12`; crypto_alt avg `-0.0532` n `230`; crypto_major avg `-0.0122` n `8`; equity avg `-0.1174` n `112`; fx avg `-0.0038` n `6`; index avg `-0.0076` n `25`; metal avg `0.0277` n `20`; unknown avg `-0.0509` n `785`
- 24h: commodity avg `0.2018` n `12`; crypto_alt avg `1.1714` n `230`; crypto_major avg `0.2942` n `8`; equity avg `0.4046` n `112`; fx avg `-0.0067` n `6`; index avg `0.0516` n `25`; metal avg `0.0308` n `20`; unknown avg `0.2602` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal

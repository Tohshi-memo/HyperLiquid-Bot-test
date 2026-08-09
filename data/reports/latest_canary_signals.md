# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T17:07:23.688490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.0737` n `230`; crypto_major avg `0.0045` n `8`; equity avg `0.0081` n `112`; fx avg `0.0006` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0077` n `20`; unknown avg `-0.0054` n `785`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `0.202` n `230`; crypto_major avg `-0.0689` n `8`; equity avg `0.0321` n `112`; fx avg `0.0028` n `6`; index avg `0.0046` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.0205` n `785`
- 4h: commodity avg `-0.052` n `12`; crypto_alt avg `0.8112` n `230`; crypto_major avg `0.5517` n `8`; equity avg `0.0975` n `112`; fx avg `0.0203` n `6`; index avg `0.0195` n `25`; metal avg `0.0326` n `20`; unknown avg `0.0184` n `785`
- 24h: commodity avg `-0.0126` n `12`; crypto_alt avg `1.1843` n `230`; crypto_major avg `0.1759` n `8`; equity avg `0.2942` n `112`; fx avg `0.0079` n `6`; index avg `0.0321` n `25`; metal avg `0.057` n `20`; unknown avg `0.3946` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal

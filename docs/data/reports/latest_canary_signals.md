# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T22:52:25.576390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.0398` n `230`; crypto_major avg `-0.0834` n `8`; equity avg `-0.0002` n `112`; fx avg `0.0011` n `6`; index avg `0.0026` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.1041` n `784`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `-0.1287` n `230`; crypto_major avg `-0.2465` n `8`; equity avg `0.0061` n `112`; fx avg `0.0046` n `6`; index avg `0.0026` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.0134` n `784`
- 4h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.029` n `230`; crypto_major avg `-0.1762` n `8`; equity avg `0.1568` n `112`; fx avg `0.0015` n `6`; index avg `0.0148` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.2137` n `784`
- 24h: commodity avg `0.18` n `12`; crypto_alt avg `1.8312` n `230`; crypto_major avg `1.2141` n `8`; equity avg `0.6298` n `112`; fx avg `-0.0117` n `6`; index avg `0.0311` n `25`; metal avg `0.0024` n `20`; unknown avg `0.1833` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal

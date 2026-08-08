# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T22:13:09.910418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0373` n `12`; crypto_alt avg `-0.067` n `230`; crypto_major avg `-0.1331` n `8`; equity avg `-0.0186` n `112`; fx avg `0.0031` n `6`; index avg `-0.0018` n `25`; metal avg `0.0039` n `20`; unknown avg `0.0203` n `784`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `-0.0078` n `230`; crypto_major avg `-0.1493` n `8`; equity avg `-0.0055` n `112`; fx avg `0.0038` n `6`; index avg `-0.0161` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.0902` n `784`
- 4h: commodity avg `0.0731` n `12`; crypto_alt avg `0.0164` n `230`; crypto_major avg `-0.2242` n `8`; equity avg `0.1178` n `112`; fx avg `0.0062` n `6`; index avg `0.0079` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.2734` n `784`
- 24h: commodity avg `0.2247` n `12`; crypto_alt avg `1.8653` n `230`; crypto_major avg `1.2672` n `8`; equity avg `0.6465` n `112`; fx avg `-0.0164` n `6`; index avg `0.0324` n `25`; metal avg `0.0429` n `20`; unknown avg `0.1917` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0435`, n `668`, weak_sample_signal

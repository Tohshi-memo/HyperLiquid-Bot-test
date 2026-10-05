# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T01:37:27.010390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0412` n `13`; crypto_alt avg `-0.3231` n `235`; crypto_major avg `-0.2313` n `8`; equity avg `-0.0031` n `144`; fx avg `0.0166` n `6`; index avg `0.0157` n `26`; metal avg `0.007` n `20`; unknown avg `0.2672` n `1078`
- 1h: commodity avg `-0.0501` n `13`; crypto_alt avg `0.0371` n `235`; crypto_major avg `0.2796` n `8`; equity avg `0.1919` n `144`; fx avg `-0.0803` n `6`; index avg `0.0435` n `26`; metal avg `0.0202` n `20`; unknown avg `0.1028` n `1070`
- 4h: commodity avg `-0.2519` n `13`; crypto_alt avg `0.4566` n `235`; crypto_major avg `0.1371` n `8`; equity avg `0.4592` n `144`; fx avg `-0.0946` n `6`; index avg `0.0583` n `26`; metal avg `0.1946` n `20`; unknown avg `2.2665` n `1012`
- 24h: commodity avg `-0.343` n `13`; crypto_alt avg `1.2479` n `235`; crypto_major avg `1.6286` n `8`; equity avg `0.6894` n `144`; fx avg `-0.066` n `6`; index avg `0.0636` n `26`; metal avg `0.1954` n `20`; unknown avg `0.7904` n `950`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal

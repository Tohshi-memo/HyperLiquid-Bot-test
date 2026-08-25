# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T17:22:24.115199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `-0.085` n `231`; crypto_major avg `0.0488` n `8`; equity avg `0.0531` n `122`; fx avg `0.0081` n `6`; index avg `-0.0022` n `25`; metal avg `0.0269` n `20`; unknown avg `-0.0521` n `795`
- 1h: commodity avg `0.0208` n `12`; crypto_alt avg `-0.2127` n `231`; crypto_major avg `-0.1215` n `8`; equity avg `-0.138` n `122`; fx avg `0.0083` n `6`; index avg `-0.0256` n `25`; metal avg `0.0192` n `20`; unknown avg `-0.224` n `795`
- 4h: commodity avg `0.0617` n `12`; crypto_alt avg `0.2484` n `231`; crypto_major avg `0.6648` n `8`; equity avg `0.3266` n `122`; fx avg `-0.0191` n `6`; index avg `-0.0511` n `25`; metal avg `0.3388` n `20`; unknown avg `-0.0243` n `795`
- 24h: commodity avg `-0.5707` n `12`; crypto_alt avg `-0.4994` n `231`; crypto_major avg `0.7616` n `8`; equity avg `1.5941` n `122`; fx avg `0.05` n `6`; index avg `0.1842` n `25`; metal avg `-0.0744` n `20`; unknown avg `-0.7467` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal

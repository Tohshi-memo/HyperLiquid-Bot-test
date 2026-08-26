# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T01:07:27.469788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `0.2549` n `231`; crypto_major avg `0.3017` n `8`; equity avg `0.0432` n `122`; fx avg `-0.0028` n `6`; index avg `0.0072` n `25`; metal avg `0.0312` n `20`; unknown avg `0.2958` n `796`
- 1h: commodity avg `-0.0511` n `12`; crypto_alt avg `0.8715` n `231`; crypto_major avg `0.7407` n `8`; equity avg `-0.1914` n `122`; fx avg `-0.0152` n `6`; index avg `-0.0186` n `25`; metal avg `-0.0394` n `20`; unknown avg `0.327` n `796`
- 4h: commodity avg `-0.0757` n `12`; crypto_alt avg `1.5115` n `231`; crypto_major avg `1.1465` n `8`; equity avg `-0.3387` n `122`; fx avg `0.019` n `6`; index avg `-0.1301` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.4359` n `795`
- 24h: commodity avg `-0.7678` n `12`; crypto_alt avg `-2.464` n `231`; crypto_major avg `-2.1859` n `8`; equity avg `1.5368` n `122`; fx avg `0.0532` n `6`; index avg `0.1678` n `25`; metal avg `-0.2525` n `20`; unknown avg `-0.4362` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T08:22:25.520707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0427` n `12`; crypto_alt avg `0.3948` n `231`; crypto_major avg `0.3977` n `8`; equity avg `0.2019` n `122`; fx avg `0.0056` n `6`; index avg `0.0139` n `25`; metal avg `0.0173` n `20`; unknown avg `0.0073` n `794`
- 1h: commodity avg `0.0292` n `12`; crypto_alt avg `-0.5984` n `231`; crypto_major avg `-0.5904` n `8`; equity avg `-0.0304` n `122`; fx avg `0.015` n `6`; index avg `0.0045` n `25`; metal avg `-0.1314` n `20`; unknown avg `-0.1285` n `794`
- 4h: commodity avg `-0.1788` n `12`; crypto_alt avg `-0.6667` n `231`; crypto_major avg `-0.5238` n `8`; equity avg `0.4082` n `122`; fx avg `0.045` n `6`; index avg `0.067` n `25`; metal avg `-0.033` n `20`; unknown avg `-0.2876` n `778`
- 24h: commodity avg `-0.2681` n `12`; crypto_alt avg `1.6425` n `231`; crypto_major avg `2.9264` n `8`; equity avg `0.2698` n `122`; fx avg `0.0348` n `6`; index avg `0.0321` n `25`; metal avg `-0.2044` n `20`; unknown avg `0.7229` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal

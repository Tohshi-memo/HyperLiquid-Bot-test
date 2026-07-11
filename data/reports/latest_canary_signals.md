# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T05:37:34.955584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `0.1403` n `230`; crypto_major avg `0.0779` n `8`; equity avg `0.0217` n `92`; fx avg `0.0131` n `6`; index avg `-0.0071` n `25`; metal avg `0.0039` n `20`; unknown avg `0.6059` n `765`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.0724` n `229`; crypto_major avg `0.037` n `8`; equity avg `0.0473` n `92`; fx avg `0.0313` n `6`; index avg `-0.003` n `25`; metal avg `-0.0073` n `20`; unknown avg `0.7478` n `765`
- 4h: commodity avg `-0.0532` n `12`; crypto_alt avg `-0.1153` n `229`; crypto_major avg `-0.0879` n `8`; equity avg `0.0147` n `92`; fx avg `0.0353` n `6`; index avg `0.008` n `25`; metal avg `0.0107` n `20`; unknown avg `-0.059` n `763`
- 24h: commodity avg `-0.4092` n `12`; crypto_alt avg `0.2948` n `229`; crypto_major avg `-0.2859` n `8`; equity avg `-0.4841` n `92`; fx avg `-0.1371` n `6`; index avg `0.0736` n `25`; metal avg `0.0689` n `20`; unknown avg `4.1767` n `730`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal

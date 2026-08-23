# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T15:37:25.240935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `0.2042` n `231`; crypto_major avg `0.1468` n `8`; equity avg `-0.0048` n `122`; fx avg `0.0011` n `6`; index avg `-0.0102` n `25`; metal avg `0.004` n `20`; unknown avg `0.0305` n `793`
- 1h: commodity avg `0.0006` n `12`; crypto_alt avg `1.2414` n `231`; crypto_major avg `0.4933` n `8`; equity avg `0.1436` n `122`; fx avg `0.0067` n `6`; index avg `0.0136` n `25`; metal avg `0.0317` n `20`; unknown avg `0.2918` n `793`
- 4h: commodity avg `-0.0057` n `12`; crypto_alt avg `1.7098` n `231`; crypto_major avg `0.0202` n `8`; equity avg `0.1621` n `122`; fx avg `-0.0006` n `6`; index avg `0.034` n `25`; metal avg `0.026` n `20`; unknown avg `2.858` n `793`
- 24h: commodity avg `0.066` n `12`; crypto_alt avg `2.6537` n `231`; crypto_major avg `1.6746` n `8`; equity avg `0.6646` n `122`; fx avg `0.0482` n `6`; index avg `0.0711` n `25`; metal avg `0.0638` n `20`; unknown avg `8.1598` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T17:22:29.452275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2098` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0239` n `12`; crypto_alt avg `-0.0314` n `230`; crypto_major avg `-0.0947` n `8`; equity avg `0.1388` n `112`; fx avg `-0.0048` n `6`; index avg `0.004` n `25`; metal avg `-0.0067` n `20`; unknown avg `-0.0795` n `782`
- 1h: commodity avg `-0.0563` n `12`; crypto_alt avg `-0.352` n `230`; crypto_major avg `-0.8299` n `8`; equity avg `-0.1786` n `112`; fx avg `-0.0119` n `6`; index avg `-0.0154` n `25`; metal avg `-0.0574` n `20`; unknown avg `0.1933` n `782`
- 4h: commodity avg `0.1893` n `12`; crypto_alt avg `-0.529` n `230`; crypto_major avg `-1.3054` n `8`; equity avg `-0.5276` n `112`; fx avg `-0.0024` n `6`; index avg `-0.0956` n `25`; metal avg `-0.1596` n `20`; unknown avg `0.498` n `782`
- 24h: commodity avg `0.3622` n `12`; crypto_alt avg `-0.5896` n `230`; crypto_major avg `-0.8346` n `8`; equity avg `0.6977` n `112`; fx avg `-0.1482` n `6`; index avg `-0.0303` n `25`; metal avg `0.2386` n `20`; unknown avg `-0.1049` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T02:52:34.023350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0361` n `230`; crypto_major avg `0.1362` n `8`; equity avg `0.2002` n `112`; fx avg `0.005` n `6`; index avg `0.0311` n `25`; metal avg `-0.0008` n `20`; unknown avg `1.1172` n `782`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `0.0096` n `230`; crypto_major avg `-0.0617` n `8`; equity avg `0.6076` n `112`; fx avg `0.0195` n `6`; index avg `0.0556` n `25`; metal avg `0.0242` n `20`; unknown avg `2.3196` n `782`
- 4h: commodity avg `-0.0174` n `12`; crypto_alt avg `0.3204` n `230`; crypto_major avg `-0.0595` n `8`; equity avg `0.1624` n `112`; fx avg `-0.0475` n `6`; index avg `-0.1322` n `25`; metal avg `0.1269` n `20`; unknown avg `0.071` n `782`
- 24h: commodity avg `0.4998` n `12`; crypto_alt avg `0.7096` n `230`; crypto_major avg `-0.4719` n `8`; equity avg `0.7123` n `109`; fx avg `0.0021` n `6`; index avg `-0.1491` n `25`; metal avg `-0.1857` n `20`; unknown avg `113.2062` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal

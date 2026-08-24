# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T23:22:25.513397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `0.0242` n `231`; crypto_major avg `0.1684` n `8`; equity avg `-0.0393` n `122`; fx avg `0.0038` n `6`; index avg `-0.0007` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.0438` n `794`
- 1h: commodity avg `0.0333` n `12`; crypto_alt avg `-0.2402` n `231`; crypto_major avg `0.0067` n `8`; equity avg `-0.0571` n `122`; fx avg `-0.006` n `6`; index avg `0.0015` n `25`; metal avg `0.1089` n `20`; unknown avg `0.0172` n `794`
- 4h: commodity avg `-0.0931` n `12`; crypto_alt avg `0.2799` n `231`; crypto_major avg `0.7133` n `8`; equity avg `-0.2685` n `122`; fx avg `-0.0044` n `6`; index avg `-0.0459` n `25`; metal avg `0.1786` n `20`; unknown avg `-0.4549` n `794`
- 24h: commodity avg `-0.09` n `12`; crypto_alt avg `-1.6109` n `231`; crypto_major avg `-0.8207` n `8`; equity avg `-2.9653` n `122`; fx avg `-0.0625` n `6`; index avg `-0.3626` n `25`; metal avg `0.2914` n `20`; unknown avg `0.804` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal

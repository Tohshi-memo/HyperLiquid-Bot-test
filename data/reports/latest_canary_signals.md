# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T09:07:29.609546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0769` n `12`; crypto_alt avg `-0.0027` n `230`; crypto_major avg `0.1307` n `8`; equity avg `0.0223` n `112`; fx avg `-0.0092` n `6`; index avg `0.0285` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0122` n `782`
- 1h: commodity avg `-0.0557` n `12`; crypto_alt avg `0.0515` n `230`; crypto_major avg `0.4722` n `8`; equity avg `0.2287` n `112`; fx avg `-0.0215` n `6`; index avg `0.0139` n `25`; metal avg `0.0786` n `20`; unknown avg `0.0261` n `782`
- 4h: commodity avg `-0.1336` n `12`; crypto_alt avg `0.3976` n `230`; crypto_major avg `0.7913` n `8`; equity avg `0.8749` n `112`; fx avg `-0.0342` n `6`; index avg `0.1229` n `25`; metal avg `0.464` n `20`; unknown avg `0.0473` n `766`
- 24h: commodity avg `0.4692` n `12`; crypto_alt avg `0.1887` n `230`; crypto_major avg `-0.483` n `8`; equity avg `2.0366` n `109`; fx avg `-0.0854` n `6`; index avg `0.0948` n `25`; metal avg `0.3047` n `20`; unknown avg `110.7894` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal

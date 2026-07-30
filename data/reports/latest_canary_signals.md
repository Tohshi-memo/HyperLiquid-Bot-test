# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T05:37:32.322117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0844` n `12`; crypto_alt avg `0.1937` n `230`; crypto_major avg `0.2155` n `8`; equity avg `0.054` n `102`; fx avg `0.0074` n `6`; index avg `-0.0133` n `25`; metal avg `-0.0373` n `20`; unknown avg `1.0811` n `779`
- 1h: commodity avg `0.297` n `12`; crypto_alt avg `0.0395` n `230`; crypto_major avg `0.0403` n `8`; equity avg `-0.1327` n `102`; fx avg `0.0035` n `6`; index avg `-0.0795` n `25`; metal avg `-0.0934` n `20`; unknown avg `-0.2167` n `779`
- 4h: commodity avg `0.3183` n `12`; crypto_alt avg `-0.1714` n `230`; crypto_major avg `-0.3299` n `8`; equity avg `-1.7465` n `102`; fx avg `-0.0811` n `6`; index avg `-0.3393` n `25`; metal avg `-0.4484` n `20`; unknown avg `0.081` n `779`
- 24h: commodity avg `0.8648` n `12`; crypto_alt avg `-0.3244` n `230`; crypto_major avg `-0.4071` n `8`; equity avg `-2.7519` n `102`; fx avg `0.0505` n `6`; index avg `-0.2291` n `25`; metal avg `-0.0904` n `20`; unknown avg `-0.5747` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal

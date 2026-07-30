# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T04:22:30.095969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.1813` n `230`; crypto_major avg `-0.2124` n `8`; equity avg `-0.1868` n `102`; fx avg `-0.0171` n `6`; index avg `-0.0321` n `25`; metal avg `-0.0519` n `20`; unknown avg `-0.1607` n `779`
- 1h: commodity avg `0.0649` n `12`; crypto_alt avg `-0.262` n `230`; crypto_major avg `-0.3705` n `8`; equity avg `-0.0976` n `102`; fx avg `-0.0422` n `6`; index avg `0.0031` n `25`; metal avg `-0.0557` n `20`; unknown avg `0.1315` n `779`
- 4h: commodity avg `0.0653` n `12`; crypto_alt avg `0.1218` n `230`; crypto_major avg `-0.3007` n `8`; equity avg `-0.725` n `102`; fx avg `0.0012` n `6`; index avg `-0.0598` n `25`; metal avg `-0.2492` n `20`; unknown avg `0.1852` n `778`
- 24h: commodity avg `0.4633` n `12`; crypto_alt avg `0.0851` n `230`; crypto_major avg `0.0133` n `8`; equity avg `-1.3027` n `102`; fx avg `0.0708` n `6`; index avg `0.0481` n `25`; metal avg `0.1321` n `20`; unknown avg `-0.4933` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal

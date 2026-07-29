# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T06:52:28.314630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0467` n `12`; crypto_alt avg `-0.084` n `230`; crypto_major avg `-0.0667` n `8`; equity avg `0.184` n `102`; fx avg `0.0049` n `6`; index avg `0.107` n `25`; metal avg `0.0162` n `20`; unknown avg `-0.0038` n `777`
- 1h: commodity avg `-0.0225` n `12`; crypto_alt avg `0.1011` n `230`; crypto_major avg `0.3413` n `8`; equity avg `0.4853` n `102`; fx avg `-0.0036` n `6`; index avg `0.2413` n `25`; metal avg `0.0789` n `20`; unknown avg `-0.0634` n `761`
- 4h: commodity avg `-0.0294` n `12`; crypto_alt avg `-0.5424` n `230`; crypto_major avg `0.5347` n `8`; equity avg `0.4995` n `102`; fx avg `-0.0604` n `6`; index avg `0.2236` n `25`; metal avg `0.0842` n `20`; unknown avg `-0.0768` n `761`
- 24h: commodity avg `-0.0059` n `12`; crypto_alt avg `-1.4962` n `230`; crypto_major avg `0.967` n `8`; equity avg `-1.3714` n `102`; fx avg `-0.1109` n `6`; index avg `-0.146` n `25`; metal avg `0.0119` n `20`; unknown avg `-0.2676` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T01:22:28.636168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0542` n `12`; crypto_alt avg `-0.0174` n `230`; crypto_major avg `-0.0867` n `8`; equity avg `-0.0802` n `102`; fx avg `0.0036` n `6`; index avg `-0.0394` n `25`; metal avg `-0.0482` n `20`; unknown avg `-0.0721` n `779`
- 1h: commodity avg `0.113` n `12`; crypto_alt avg `0.0082` n `230`; crypto_major avg `-0.2026` n `8`; equity avg `0.3532` n `102`; fx avg `0.0393` n `6`; index avg `0.0549` n `25`; metal avg `0.047` n `20`; unknown avg `4.5704` n `778`
- 4h: commodity avg `-0.1572` n `12`; crypto_alt avg `1.1549` n `230`; crypto_major avg `0.7874` n `8`; equity avg `1.8879` n `102`; fx avg `-0.0123` n `6`; index avg `0.3209` n `25`; metal avg `0.1894` n `20`; unknown avg `1.0265` n `778`
- 24h: commodity avg `0.4818` n `12`; crypto_alt avg `-1.7347` n `230`; crypto_major avg `-0.4548` n `8`; equity avg `-2.5768` n `102`; fx avg `0.0062` n `6`; index avg `-0.4229` n `25`; metal avg `0.4044` n `20`; unknown avg `-0.461` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal

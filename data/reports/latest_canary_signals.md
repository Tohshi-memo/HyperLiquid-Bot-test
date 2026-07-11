# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T09:52:28.578583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.0831` n `230`; crypto_major avg `-0.0951` n `8`; equity avg `-0.0195` n `92`; fx avg `0.0063` n `6`; index avg `-0.0007` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.0221` n `765`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `0.0539` n `230`; crypto_major avg `-0.0716` n `8`; equity avg `0.0421` n `92`; fx avg `0.0015` n `6`; index avg `0.0075` n `25`; metal avg `0.0039` n `20`; unknown avg `0.0318` n `761`
- 4h: commodity avg `0.075` n `12`; crypto_alt avg `0.1936` n `230`; crypto_major avg `0.0588` n `8`; equity avg `0.1691` n `92`; fx avg `-0.0064` n `6`; index avg `0.0319` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.0249` n `729`
- 24h: commodity avg `-0.1796` n `12`; crypto_alt avg `0.1077` n `229`; crypto_major avg `-0.7358` n `8`; equity avg `0.043` n `92`; fx avg `-0.0713` n `6`; index avg `0.1516` n `25`; metal avg `0.1762` n `20`; unknown avg `2.9589` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal

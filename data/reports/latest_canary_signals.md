# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T11:37:33.844520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.053` n `12`; crypto_alt avg `0.0041` n `230`; crypto_major avg `0.0383` n `8`; equity avg `-0.2511` n `120`; fx avg `-0.0035` n `6`; index avg `-0.0272` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.0105` n `792`
- 1h: commodity avg `-0.0182` n `12`; crypto_alt avg `0.2603` n `230`; crypto_major avg `0.2561` n `8`; equity avg `-0.1841` n `120`; fx avg `0.0012` n `6`; index avg `-0.0248` n `25`; metal avg `0.0281` n `20`; unknown avg `0.3023` n `791`
- 4h: commodity avg `0.1601` n `12`; crypto_alt avg `0.277` n `230`; crypto_major avg `0.2721` n `8`; equity avg `-0.427` n `120`; fx avg `-0.0808` n `6`; index avg `-0.0034` n `25`; metal avg `0.078` n `20`; unknown avg `0.1138` n `789`
- 24h: commodity avg `0.4113` n `12`; crypto_alt avg `0.3041` n `230`; crypto_major avg `0.2565` n `8`; equity avg `-2.0549` n `120`; fx avg `-0.2014` n `6`; index avg `-0.2407` n `25`; metal avg `-0.3881` n `20`; unknown avg `-0.2475` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal

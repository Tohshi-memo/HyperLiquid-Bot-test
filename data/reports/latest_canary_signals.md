# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T02:22:31.217172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.1679` n `234`; crypto_major avg `-0.0469` n `8`; equity avg `0.0519` n `141`; fx avg `-0.0162` n `6`; index avg `0.0086` n `26`; metal avg `0.004` n `20`; unknown avg `0.0118` n `946`
- 1h: commodity avg `-0.0591` n `12`; crypto_alt avg `-0.1702` n `234`; crypto_major avg `0.2155` n `8`; equity avg `0.0355` n `141`; fx avg `-0.0558` n `6`; index avg `0.0205` n `26`; metal avg `-0.0275` n `20`; unknown avg `-0.0832` n `944`
- 4h: commodity avg `-0.2621` n `12`; crypto_alt avg `0.4969` n `234`; crypto_major avg `0.763` n `8`; equity avg `0.4318` n `141`; fx avg `-0.0888` n `6`; index avg `0.0871` n `26`; metal avg `0.0799` n `20`; unknown avg `2.0284` n `938`
- 24h: commodity avg `0.4646` n `12`; crypto_alt avg `3.3547` n `234`; crypto_major avg `1.5781` n `8`; equity avg `0.3497` n `141`; fx avg `-0.0943` n `6`; index avg `0.0199` n `26`; metal avg `0.0156` n `20`; unknown avg `22.7244` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal

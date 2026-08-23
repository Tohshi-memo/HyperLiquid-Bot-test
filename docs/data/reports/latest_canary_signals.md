# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T13:06:43.268785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.1874` n `230`; crypto_major avg `0.1888` n `8`; equity avg `-0.0011` n `121`; fx avg `-0.0007` n `6`; index avg `-0.0072` n `25`; metal avg `0.0149` n `20`; unknown avg `-0.0088` n `795`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `0.5336` n `230`; crypto_major avg `0.4801` n `8`; equity avg `0.0532` n `121`; fx avg `-0.0025` n `6`; index avg `-0.0026` n `25`; metal avg `0.024` n `20`; unknown avg `0.9001` n `795`
- 4h: commodity avg `0.0129` n `12`; crypto_alt avg `2.0153` n `230`; crypto_major avg `1.1076` n `8`; equity avg `0.2517` n `121`; fx avg `-0.0117` n `6`; index avg `0.0313` n `25`; metal avg `0.0518` n `20`; unknown avg `2.2413` n `794`
- 24h: commodity avg `-0.0229` n `12`; crypto_alt avg `0.7374` n `230`; crypto_major avg `0.7241` n `8`; equity avg `0.4581` n `121`; fx avg `0.0343` n `6`; index avg `0.0408` n `25`; metal avg `0.0664` n `20`; unknown avg `5.6973` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal

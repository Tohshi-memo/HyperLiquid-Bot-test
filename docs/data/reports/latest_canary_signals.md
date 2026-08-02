# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T00:07:35.280601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0887` n `12`; crypto_alt avg `0.2252` n `230`; crypto_major avg `0.1653` n `8`; equity avg `0.1191` n `102`; fx avg `0.0659` n `6`; index avg `0.0319` n `25`; metal avg `-0.0104` n `20`; unknown avg `-0.0478` n `782`
- 1h: commodity avg `-0.0569` n `12`; crypto_alt avg `0.1212` n `230`; crypto_major avg `0.1132` n `8`; equity avg `0.124` n `102`; fx avg `-0.0181` n `6`; index avg `0.0441` n `25`; metal avg `-0.0129` n `20`; unknown avg `-0.1273` n `782`
- 4h: commodity avg `-0.2786` n `12`; crypto_alt avg `0.3163` n `230`; crypto_major avg `0.5552` n `8`; equity avg `0.4167` n `102`; fx avg `-0.0182` n `6`; index avg `0.0682` n `25`; metal avg `0.0302` n `20`; unknown avg `0.0513` n `782`
- 24h: commodity avg `-0.2444` n `12`; crypto_alt avg `-0.4756` n `230`; crypto_major avg `-0.6509` n `8`; equity avg `-0.1922` n `102`; fx avg `-0.0531` n `6`; index avg `0.0121` n `25`; metal avg `0.0569` n `20`; unknown avg `-0.0487` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal

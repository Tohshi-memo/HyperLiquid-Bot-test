# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T15:22:32.234330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1426` n `12`; crypto_alt avg `0.15` n `233`; crypto_major avg `0.0563` n `8`; equity avg `0.1425` n `136`; fx avg `-0.0001` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0338` n `20`; unknown avg `0.0887` n `894`
- 1h: commodity avg `-0.083` n `12`; crypto_alt avg `-0.1399` n `233`; crypto_major avg `-0.0915` n `8`; equity avg `-0.0751` n `136`; fx avg `-0.0129` n `6`; index avg `-0.0456` n `27`; metal avg `0.0609` n `20`; unknown avg `-0.1364` n `878`
- 4h: commodity avg `0.0377` n `12`; crypto_alt avg `-0.3411` n `233`; crypto_major avg `-0.0349` n `8`; equity avg `0.265` n `136`; fx avg `0.005` n `6`; index avg `-0.0744` n `27`; metal avg `-0.079` n `20`; unknown avg `0.5051` n `872`
- 24h: commodity avg `0.5421` n `12`; crypto_alt avg `-0.458` n `233`; crypto_major avg `1.4294` n `8`; equity avg `-0.6773` n `136`; fx avg `0.0472` n `6`; index avg `-0.2982` n `27`; metal avg `-0.4802` n `20`; unknown avg `0.9701` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal

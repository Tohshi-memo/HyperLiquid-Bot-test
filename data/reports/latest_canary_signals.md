# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T20:07:25.101355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0581` n `12`; crypto_alt avg `0.0067` n `230`; crypto_major avg `-0.0185` n `8`; equity avg `-0.0105` n `96`; fx avg `0.0011` n `6`; index avg `0.0011` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.0135` n `770`
- 1h: commodity avg `-0.0444` n `12`; crypto_alt avg `0.0311` n `230`; crypto_major avg `-0.025` n `8`; equity avg `-0.0283` n `96`; fx avg `0.0052` n `6`; index avg `0.0015` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.0798` n `770`
- 4h: commodity avg `0.2357` n `12`; crypto_alt avg `0.2297` n `230`; crypto_major avg `0.5254` n `8`; equity avg `0.0296` n `96`; fx avg `-0.0296` n `6`; index avg `-0.0286` n `25`; metal avg `-0.0299` n `20`; unknown avg `0.0999` n `770`
- 24h: commodity avg `0.4353` n `12`; crypto_alt avg `-0.4366` n `230`; crypto_major avg `0.3558` n `8`; equity avg `-0.2259` n `96`; fx avg `-0.1292` n `6`; index avg `0.036` n `25`; metal avg `-0.0222` n `20`; unknown avg `-0.0207` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal

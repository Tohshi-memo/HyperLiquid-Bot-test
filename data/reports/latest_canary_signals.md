# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T14:37:26.401324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0374` n `230`; crypto_major avg `0.0847` n `8`; equity avg `0.0207` n `96`; fx avg `-0.0077` n `6`; index avg `0.0073` n `25`; metal avg `-0.024` n `20`; unknown avg `0.002` n `770`
- 1h: commodity avg `-0.0347` n `12`; crypto_alt avg `0.2289` n `230`; crypto_major avg `0.3123` n `8`; equity avg `0.0116` n `96`; fx avg `0.0014` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0284` n `20`; unknown avg `0.0471` n `770`
- 4h: commodity avg `-0.0543` n `12`; crypto_alt avg `-0.0661` n `230`; crypto_major avg `0.1797` n `8`; equity avg `-0.0901` n `96`; fx avg `-0.0006` n `6`; index avg `-0.0369` n `25`; metal avg `-0.0512` n `20`; unknown avg `-0.0236` n `769`
- 24h: commodity avg `0.4197` n `12`; crypto_alt avg `-0.6098` n `230`; crypto_major avg `0.4373` n `8`; equity avg `-0.3725` n `96`; fx avg `0.024` n `6`; index avg `0.0265` n `25`; metal avg `0.19` n `20`; unknown avg `0.0168` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal

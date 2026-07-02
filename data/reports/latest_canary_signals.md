# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T05:37:25.821291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0364` n `12`; crypto_alt avg `-0.1297` n `228`; crypto_major avg `-0.141` n `8`; equity avg `-0.2341` n `88`; fx avg `0.0108` n `6`; index avg `-0.0767` n `25`; metal avg `-0.0298` n `20`; unknown avg `0.67` n `763`
- 1h: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.044` n `228`; crypto_major avg `-0.039` n `8`; equity avg `-0.0292` n `88`; fx avg `0.0136` n `6`; index avg `-0.0115` n `25`; metal avg `-0.0912` n `20`; unknown avg `0.503` n `763`
- 4h: commodity avg `0.0024` n `12`; crypto_alt avg `0.4557` n `228`; crypto_major avg `0.4408` n `8`; equity avg `-0.5913` n `88`; fx avg `0.0083` n `6`; index avg `-0.1828` n `25`; metal avg `0.0536` n `20`; unknown avg `0.6309` n `759`
- 24h: commodity avg `-0.6204` n `12`; crypto_alt avg `1.6725` n `228`; crypto_major avg `1.1524` n `8`; equity avg `-1.64` n `88`; fx avg `0.044` n `6`; index avg `-0.4364` n `25`; metal avg `1.0236` n `20`; unknown avg `24.9807` n `735`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T03:07:30.452269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `0.022` n `228`; crypto_major avg `0.1114` n `8`; equity avg `-0.0802` n `88`; fx avg `0.0008` n `6`; index avg `-0.0101` n `25`; metal avg `0.0232` n `20`; unknown avg `-0.0726` n `763`
- 1h: commodity avg `-0.0544` n `12`; crypto_alt avg `0.1938` n `228`; crypto_major avg `0.3592` n `8`; equity avg `-0.2539` n `88`; fx avg `-0.0063` n `6`; index avg `-0.0666` n `25`; metal avg `0.1787` n `20`; unknown avg `-0.1086` n `763`
- 4h: commodity avg `-0.1034` n `12`; crypto_alt avg `0.5065` n `228`; crypto_major avg `0.2684` n `8`; equity avg `-0.0769` n `88`; fx avg `0.0024` n `6`; index avg `0.0289` n `25`; metal avg `0.3648` n `20`; unknown avg `-0.4817` n `761`
- 24h: commodity avg `-0.6614` n `12`; crypto_alt avg `1.8031` n `228`; crypto_major avg `0.9607` n `8`; equity avg `-1.2531` n `88`; fx avg `-0.0301` n `6`; index avg `-0.3016` n `25`; metal avg `0.9989` n `20`; unknown avg `25.1966` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal

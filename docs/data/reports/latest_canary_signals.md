# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T06:37:27.283148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0496` n `12`; crypto_alt avg `-0.022` n `228`; crypto_major avg `0.0434` n `8`; equity avg `-0.0006` n `88`; fx avg `-0.0022` n `6`; index avg `0.0077` n `25`; metal avg `-0.0607` n `20`; unknown avg `1.7584` n `763`
- 1h: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.2252` n `228`; crypto_major avg `-0.0867` n `8`; equity avg `-0.5778` n `88`; fx avg `-0.0083` n `6`; index avg `-0.1113` n `25`; metal avg `0.1535` n `20`; unknown avg `1.8349` n `741`
- 4h: commodity avg `-0.0309` n `12`; crypto_alt avg `0.0648` n `228`; crypto_major avg `0.2193` n `8`; equity avg `-1.1249` n `88`; fx avg `0.0005` n `6`; index avg `-0.275` n `25`; metal avg `0.1026` n `20`; unknown avg `1.4379` n `739`
- 24h: commodity avg `-0.5146` n `12`; crypto_alt avg `2.1413` n `228`; crypto_major avg `1.969` n `8`; equity avg `-1.987` n `88`; fx avg `-0.0222` n `6`; index avg `-0.5096` n `25`; metal avg `1.3279` n `20`; unknown avg `25.4842` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal

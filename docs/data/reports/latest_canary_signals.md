# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T11:52:28.162107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0454` n `13`; crypto_alt avg `-0.0143` n `239`; crypto_major avg `-0.0289` n `8`; equity avg `0.0587` n `164`; fx avg `-0.0146` n `6`; index avg `0.022` n `27`; metal avg `-0.0372` n `20`; unknown avg `0.7369` n `1266`
- 1h: commodity avg `-0.0972` n `13`; crypto_alt avg `0.322` n `239`; crypto_major avg `0.2969` n `8`; equity avg `0.3187` n `164`; fx avg `-0.0456` n `6`; index avg `0.0318` n `27`; metal avg `-0.0853` n `20`; unknown avg `0.2869` n `1264`
- 4h: commodity avg `-0.062` n `13`; crypto_alt avg `0.4362` n `239`; crypto_major avg `0.4434` n `8`; equity avg `0.898` n `164`; fx avg `0.0281` n `6`; index avg `0.1607` n `27`; metal avg `-0.0422` n `20`; unknown avg `319.5485` n `1232`
- 24h: commodity avg `-0.0698` n `13`; crypto_alt avg `0.3847` n `239`; crypto_major avg `0.2773` n `8`; equity avg `1.0923` n `164`; fx avg `0.0303` n `6`; index avg `0.3295` n `27`; metal avg `-0.1917` n `20`; unknown avg `2.8287` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal

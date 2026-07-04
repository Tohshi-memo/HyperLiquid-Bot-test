# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T01:22:24.771334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0454` n `12`; crypto_alt avg `0.1764` n `229`; crypto_major avg `0.0445` n `8`; equity avg `0.0254` n `88`; fx avg `-0.0229` n `6`; index avg `0.0005` n `25`; metal avg `-0.0189` n `20`; unknown avg `4.1969` n `765`
- 1h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.391` n `229`; crypto_major avg `-0.2662` n `8`; equity avg `0.016` n `88`; fx avg `-0.0179` n `6`; index avg `-0.0331` n `25`; metal avg `-0.0357` n `20`; unknown avg `0.2607` n `765`
- 4h: commodity avg `0.0439` n `12`; crypto_alt avg `-0.5321` n `229`; crypto_major avg `-0.2432` n `8`; equity avg `0.0209` n `88`; fx avg `-0.0184` n `6`; index avg `-0.0617` n `25`; metal avg `-0.0505` n `20`; unknown avg `0.2435` n `765`
- 24h: commodity avg `0.1523` n `12`; crypto_alt avg `2.1594` n `229`; crypto_major avg `2.6357` n `8`; equity avg `1.2174` n `88`; fx avg `-0.097` n `6`; index avg `0.2375` n `25`; metal avg `-0.1683` n `20`; unknown avg `2.8548` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal

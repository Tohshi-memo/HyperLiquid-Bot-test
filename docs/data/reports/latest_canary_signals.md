# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T09:22:33.885371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0518` n `12`; crypto_alt avg `-0.1729` n `229`; crypto_major avg `-0.1476` n `8`; equity avg `-0.2448` n `91`; fx avg `-0.0007` n `6`; index avg `-0.014` n `25`; metal avg `0.0127` n `20`; unknown avg `-0.1476` n `763`
- 1h: commodity avg `0.2591` n `12`; crypto_alt avg `-0.6456` n `229`; crypto_major avg `-0.4585` n `8`; equity avg `-1.6145` n `91`; fx avg `0.0249` n `6`; index avg `-0.2848` n `25`; metal avg `-0.5946` n `20`; unknown avg `-0.1288` n `763`
- 4h: commodity avg `0.6172` n `12`; crypto_alt avg `-1.4786` n `229`; crypto_major avg `-1.2957` n `8`; equity avg `-2.2399` n `91`; fx avg `0.0306` n `6`; index avg `-0.4889` n `25`; metal avg `-1.038` n `20`; unknown avg `-0.5332` n `743`
- 24h: commodity avg `1.4138` n `12`; crypto_alt avg `-3.9037` n `229`; crypto_major avg `-3.367` n `8`; equity avg `-3.6151` n `91`; fx avg `-0.142` n `6`; index avg `-0.7719` n `25`; metal avg `-1.1125` n `20`; unknown avg `-0.9026` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T02:22:29.546640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5258` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3086` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.0191` n `228`; crypto_major avg `0.031` n `8`; equity avg `-0.0893` n `88`; fx avg `-0.0096` n `6`; index avg `-0.0268` n `25`; metal avg `0.0618` n `20`; unknown avg `0.0004` n `763`
- 1h: commodity avg `0.0556` n `12`; crypto_alt avg `0.3775` n `228`; crypto_major avg `0.4121` n `8`; equity avg `0.0687` n `88`; fx avg `-0.016` n `6`; index avg `0.0836` n `25`; metal avg `0.036` n `20`; unknown avg `-0.2476` n `761`
- 4h: commodity avg `-0.0732` n `12`; crypto_alt avg `-0.6655` n `228`; crypto_major avg `-1.2664` n `8`; equity avg `-0.0544` n `88`; fx avg `-0.0008` n `6`; index avg `0.0422` n `25`; metal avg `0.2594` n `20`; unknown avg `22.2512` n `761`
- 24h: commodity avg `-0.6159` n `12`; crypto_alt avg `1.9796` n `228`; crypto_major avg `0.962` n `8`; equity avg `-0.813` n `88`; fx avg `-0.0292` n `6`; index avg `-0.2155` n `25`; metal avg `0.9207` n `20`; unknown avg `25.2265` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal

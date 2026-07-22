# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T12:07:32.514923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.119` n `230`; crypto_major avg `-0.2342` n `8`; equity avg `-0.1833` n `98`; fx avg `0.0054` n `6`; index avg `-0.0345` n `25`; metal avg `0.0493` n `20`; unknown avg `0.0203` n `773`
- 1h: commodity avg `0.0893` n `12`; crypto_alt avg `-0.2403` n `230`; crypto_major avg `-0.3857` n `8`; equity avg `-0.5909` n `98`; fx avg `0.0067` n `6`; index avg `-0.0996` n `25`; metal avg `0.0746` n `20`; unknown avg `0.5261` n `773`
- 4h: commodity avg `0.092` n `12`; crypto_alt avg `0.1201` n `230`; crypto_major avg `-0.0237` n `8`; equity avg `-0.3846` n `98`; fx avg `-0.0012` n `6`; index avg `-0.0674` n `25`; metal avg `0.1028` n `20`; unknown avg `0.5534` n `773`
- 24h: commodity avg `0.7269` n `12`; crypto_alt avg `-0.7586` n `230`; crypto_major avg `-1.5832` n `8`; equity avg `0.0455` n `98`; fx avg `-0.0098` n `6`; index avg `-0.1129` n `25`; metal avg `0.3895` n `20`; unknown avg `0.6104` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1044`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0877`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.076`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `666`, weak_sample_signal

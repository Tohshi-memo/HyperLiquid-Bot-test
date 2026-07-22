# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T08:07:31.428639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0942` n `12`; crypto_alt avg `0.3276` n `230`; crypto_major avg `0.2966` n `8`; equity avg `0.134` n `98`; fx avg `0.0038` n `6`; index avg `0.0352` n `25`; metal avg `0.0468` n `20`; unknown avg `0.0654` n `773`
- 1h: commodity avg `0.0957` n `12`; crypto_alt avg `0.3147` n `230`; crypto_major avg `0.144` n `8`; equity avg `0.0743` n `98`; fx avg `-0.0089` n `6`; index avg `0.0068` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.0208` n `772`
- 4h: commodity avg `0.3297` n `12`; crypto_alt avg `-0.4707` n `230`; crypto_major avg `-0.9176` n `8`; equity avg `-1.0731` n `98`; fx avg `-0.0597` n `6`; index avg `-0.2693` n `25`; metal avg `-0.2038` n `20`; unknown avg `-0.2166` n `739`
- 24h: commodity avg `1.0102` n `12`; crypto_alt avg `-0.8806` n `230`; crypto_major avg `-1.5132` n `8`; equity avg `0.5541` n `98`; fx avg `-0.0321` n `6`; index avg `0.0046` n `25`; metal avg `0.2593` n `20`; unknown avg `0.0136` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1046`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0839`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0717`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `666`, weak_sample_signal

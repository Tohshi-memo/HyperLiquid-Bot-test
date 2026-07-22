# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T06:52:26.852731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `-0.1217` n `230`; crypto_major avg `-0.0358` n `8`; equity avg `0.0048` n `98`; fx avg `0.0051` n `6`; index avg `-0.0077` n `25`; metal avg `0.0092` n `20`; unknown avg `-0.0445` n `772`
- 1h: commodity avg `0.2032` n `12`; crypto_alt avg `-0.29` n `230`; crypto_major avg `-0.2569` n `8`; equity avg `-0.231` n `98`; fx avg `-0.0413` n `6`; index avg `-0.0991` n `25`; metal avg `-0.1689` n `20`; unknown avg `-0.0525` n `740`
- 4h: commodity avg `0.1496` n `12`; crypto_alt avg `-0.9467` n `230`; crypto_major avg `-1.1649` n `8`; equity avg `-1.2255` n `98`; fx avg `-0.0268` n `6`; index avg `-0.2872` n `25`; metal avg `-0.1238` n `20`; unknown avg `-0.2132` n `739`
- 24h: commodity avg `0.7318` n `12`; crypto_alt avg `-1.2245` n `230`; crypto_major avg `-1.5879` n `8`; equity avg `0.8324` n `98`; fx avg `0.0019` n `6`; index avg `0.0141` n `25`; metal avg `0.2819` n `20`; unknown avg `0.0443` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0984`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0817`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0714`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0691`, n `666`, weak_sample_signal

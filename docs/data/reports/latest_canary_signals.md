# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T09:52:32.275342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1044` n `12`; crypto_alt avg `0.0085` n `230`; crypto_major avg `0.0038` n `8`; equity avg `-0.0783` n `98`; fx avg `0.0079` n `6`; index avg `-0.014` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.0132` n `773`
- 1h: commodity avg `0.137` n `12`; crypto_alt avg `0.1036` n `230`; crypto_major avg `-0.0462` n `8`; equity avg `0.0123` n `98`; fx avg `0.0199` n `6`; index avg `-0.0068` n `25`; metal avg `0.0868` n `20`; unknown avg `-0.0139` n `773`
- 4h: commodity avg `0.5203` n `12`; crypto_alt avg `-0.0136` n `230`; crypto_major avg `-0.1463` n `8`; equity avg `-0.2904` n `98`; fx avg `-0.0268` n `6`; index avg `-0.1135` n `25`; metal avg `-0.141` n `20`; unknown avg `0.0066` n `740`
- 24h: commodity avg `0.7793` n `12`; crypto_alt avg `-0.885` n `230`; crypto_major avg `-1.7373` n `8`; equity avg `0.2918` n `98`; fx avg `-0.0042` n `6`; index avg `-0.0477` n `25`; metal avg `0.3068` n `20`; unknown avg `0.0723` n `739`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1044`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0783`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0693`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0672`, n `666`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T07:37:30.736867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1095` n `12`; crypto_alt avg `-0.107` n `230`; crypto_major avg `-0.1953` n `8`; equity avg `-0.1489` n `98`; fx avg `-0.0153` n `6`; index avg `-0.0416` n `25`; metal avg `-0.0347` n `20`; unknown avg `0.0508` n `772`
- 1h: commodity avg `0.2179` n `12`; crypto_alt avg `-0.2686` n `230`; crypto_major avg `-0.2809` n `8`; equity avg `-0.1224` n `98`; fx avg `0.0089` n `6`; index avg `-0.0328` n `25`; metal avg `0.0321` n `20`; unknown avg `-0.0369` n `772`
- 4h: commodity avg `0.3595` n `12`; crypto_alt avg `-0.8731` n `230`; crypto_major avg `-1.1599` n `8`; equity avg `-1.1869` n `98`; fx avg `-0.0531` n `6`; index avg `-0.2749` n `25`; metal avg `-0.1744` n `20`; unknown avg `-0.1837` n `739`
- 24h: commodity avg `0.8841` n `12`; crypto_alt avg `-1.3088` n `230`; crypto_major avg `-1.8312` n `8`; equity avg `0.6586` n `98`; fx avg `-0.0022` n `6`; index avg `-0.0088` n `25`; metal avg `0.2417` n `20`; unknown avg `0.0382` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1021`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0831`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0706`, n `666`, weak_sample_signal

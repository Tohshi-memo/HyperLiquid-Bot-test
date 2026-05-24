# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T20:07:24.498116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `12`; crypto_alt avg `-0.242` n `228`; crypto_major avg `-0.2557` n `8`; equity avg `-0.0216` n `67`; fx avg `0.0168` n `6`; index avg `-0.0002` n `23`; metal avg `-0.0329` n `18`; unknown avg `-0.0202` n `396`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.3472` n `228`; crypto_major avg `-0.3192` n `8`; equity avg `0.0567` n `67`; fx avg `0.0275` n `6`; index avg `0.0378` n `23`; metal avg `-0.0902` n `18`; unknown avg `-0.0164` n `396`
- 4h: commodity avg `0.3134` n `12`; crypto_alt avg `-0.3874` n `228`; crypto_major avg `-0.3321` n `8`; equity avg `0.1503` n `67`; fx avg `0.0291` n `6`; index avg `0.1007` n `23`; metal avg `-0.1423` n `18`; unknown avg `-0.3353` n `396`
- 24h: commodity avg `-0.3004` n `12`; crypto_alt avg `-0.7657` n `228`; crypto_major avg `1.2472` n `8`; equity avg `1.1328` n `67`; fx avg `0.1255` n `6`; index avg `0.2301` n `23`; metal avg `0.3414` n `18`; unknown avg `0.405` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal

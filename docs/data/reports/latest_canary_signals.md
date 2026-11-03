# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T00:37:29.550050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `13`; crypto_alt avg `-0.0568` n `239`; crypto_major avg `0.1192` n `8`; equity avg `0.0921` n `157`; fx avg `0.0068` n `6`; index avg `0.0069` n `27`; metal avg `0.0442` n `20`; unknown avg `0.3429` n `1264`
- 1h: commodity avg `-0.0098` n `13`; crypto_alt avg `0.2595` n `239`; crypto_major avg `0.4183` n `8`; equity avg `-0.0115` n `157`; fx avg `-0.0215` n `6`; index avg `-0.0404` n `27`; metal avg `0.1311` n `20`; unknown avg `2.7312` n `1252`
- 4h: commodity avg `0.0333` n `13`; crypto_alt avg `0.6454` n `239`; crypto_major avg `0.7458` n `8`; equity avg `0.6808` n `157`; fx avg `-0.0374` n `6`; index avg `0.0764` n `27`; metal avg `0.1454` n `20`; unknown avg `215.8636` n `1162`
- 24h: commodity avg `-1.42` n `13`; crypto_alt avg `-2.1558` n `238`; crypto_major avg `-1.0372` n `8`; equity avg `-2.9254` n `157`; fx avg `0.144` n `6`; index avg `-0.1236` n `27`; metal avg `0.2469` n `20`; unknown avg `12.7303` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal

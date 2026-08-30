# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T20:37:27.571608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0491` n `12`; crypto_alt avg `-0.1733` n `231`; crypto_major avg `-0.1455` n `8`; equity avg `-0.0418` n `128`; fx avg `-0.0012` n `6`; index avg `-0.0259` n `26`; metal avg `0.004` n `20`; unknown avg `-0.0587` n `793`
- 1h: commodity avg `0.277` n `12`; crypto_alt avg `-0.2342` n `231`; crypto_major avg `-0.2618` n `8`; equity avg `-0.0958` n `128`; fx avg `-0.0018` n `6`; index avg `-0.0178` n `26`; metal avg `-0.0429` n `20`; unknown avg `-0.0358` n `791`
- 4h: commodity avg `0.4601` n `12`; crypto_alt avg `-0.3344` n `231`; crypto_major avg `-0.7198` n `8`; equity avg `-0.1262` n `128`; fx avg `-0.0044` n `6`; index avg `-0.0362` n `26`; metal avg `-0.0602` n `20`; unknown avg `0.1726` n `791`
- 24h: commodity avg `0.4938` n `12`; crypto_alt avg `1.3295` n `231`; crypto_major avg `0.5895` n `8`; equity avg `0.0717` n `128`; fx avg `0.0242` n `6`; index avg `0.0217` n `26`; metal avg `0.0533` n `20`; unknown avg `0.106` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal

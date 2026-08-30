# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T15:52:28.721773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `12`; crypto_alt avg `-0.205` n `231`; crypto_major avg `-0.1205` n `8`; equity avg `0.004` n `128`; fx avg `-0.001` n `6`; index avg `0.0103` n `26`; metal avg `0.0118` n `20`; unknown avg `0.056` n `793`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.3645` n `231`; crypto_major avg `-0.1636` n `8`; equity avg `-0.0035` n `128`; fx avg `0.0046` n `6`; index avg `-0.0011` n `26`; metal avg `0.005` n `20`; unknown avg `0.4969` n `793`
- 4h: commodity avg `0.0206` n `12`; crypto_alt avg `0.1921` n `231`; crypto_major avg `0.5676` n `8`; equity avg `-0.0117` n `128`; fx avg `0.0013` n `6`; index avg `0.0199` n `26`; metal avg `0.0683` n `20`; unknown avg `0.3801` n `793`
- 24h: commodity avg `0.0355` n `12`; crypto_alt avg `0.7501` n `231`; crypto_major avg `0.713` n `8`; equity avg `0.2929` n `128`; fx avg `0.0172` n `6`; index avg `0.0819` n `26`; metal avg `0.1048` n `20`; unknown avg `-0.254` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T11:37:26.530455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0561` n `12`; crypto_alt avg `-0.1554` n `231`; crypto_major avg `-0.2126` n `8`; equity avg `-0.0746` n `127`; fx avg `-0.0015` n `6`; index avg `-0.0088` n `26`; metal avg `0.0178` n `20`; unknown avg `-0.0327` n `792`
- 1h: commodity avg `-0.148` n `12`; crypto_alt avg `0.3557` n `231`; crypto_major avg `0.2606` n `8`; equity avg `0.0213` n `127`; fx avg `0.0231` n `6`; index avg `-0.0007` n `26`; metal avg `0.005` n `20`; unknown avg `-0.0225` n `792`
- 4h: commodity avg `-0.0374` n `12`; crypto_alt avg `0.2591` n `231`; crypto_major avg `-0.255` n `8`; equity avg `-0.1205` n `127`; fx avg `0.066` n `6`; index avg `-0.0208` n `26`; metal avg `0.1035` n `20`; unknown avg `-0.0096` n `792`
- 24h: commodity avg `0.0458` n `12`; crypto_alt avg `-0.0923` n `231`; crypto_major avg `0.2839` n `8`; equity avg `-0.8458` n `127`; fx avg `-0.0103` n `6`; index avg `-0.0138` n `26`; metal avg `0.6763` n `20`; unknown avg `0.3301` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal

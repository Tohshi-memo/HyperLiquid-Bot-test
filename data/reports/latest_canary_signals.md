# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T04:52:26.835053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `-0.2389` n `228`; crypto_major avg `-0.267` n `8`; equity avg `-0.0383` n `78`; fx avg `0.0016` n `6`; index avg `-0.0111` n `23`; metal avg `0.0001` n `18`; unknown avg `0.3768` n `702`
- 1h: commodity avg `0.0242` n `12`; crypto_alt avg `-0.1981` n `228`; crypto_major avg `-0.2372` n `8`; equity avg `-0.0068` n `78`; fx avg `-0.0001` n `6`; index avg `-0.0112` n `23`; metal avg `-0.0033` n `18`; unknown avg `2.4372` n `702`
- 4h: commodity avg `0.0056` n `12`; crypto_alt avg `-0.0167` n `228`; crypto_major avg `-0.1551` n `8`; equity avg `0.1577` n `78`; fx avg `-0.0101` n `6`; index avg `0.0157` n `23`; metal avg `0.031` n `18`; unknown avg `0.3032` n `701`
- 24h: commodity avg `0.2558` n `12`; crypto_alt avg `1.1799` n `228`; crypto_major avg `0.873` n `8`; equity avg `0.3177` n `78`; fx avg `0.0763` n `6`; index avg `-0.0076` n `23`; metal avg `-0.0293` n `18`; unknown avg `1.6178` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal

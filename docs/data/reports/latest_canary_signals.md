# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T06:07:31.544020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0253` n `13`; crypto_alt avg `0.2166` n `235`; crypto_major avg `0.2626` n `8`; equity avg `0.046` n `144`; fx avg `-0.0349` n `6`; index avg `0.0088` n `26`; metal avg `0.0652` n `20`; unknown avg `2.4598` n `1061`
- 1h: commodity avg `-0.0357` n `13`; crypto_alt avg `0.3637` n `235`; crypto_major avg `0.3237` n `8`; equity avg `-0.0032` n `144`; fx avg `-0.0388` n `6`; index avg `0.0054` n `26`; metal avg `0.0791` n `20`; unknown avg `2.5417` n `1061`
- 4h: commodity avg `-0.0351` n `13`; crypto_alt avg `-0.3648` n `235`; crypto_major avg `-0.4828` n `8`; equity avg `-0.2661` n `144`; fx avg `-0.0737` n `6`; index avg `-0.083` n `26`; metal avg `-0.0873` n `20`; unknown avg `1.1694` n `970`
- 24h: commodity avg `-0.3764` n `13`; crypto_alt avg `0.5002` n `235`; crypto_major avg `1.0681` n `8`; equity avg `0.2599` n `144`; fx avg `-0.0839` n `6`; index avg `-0.0463` n `26`; metal avg `0.1213` n `20`; unknown avg `0.077` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal

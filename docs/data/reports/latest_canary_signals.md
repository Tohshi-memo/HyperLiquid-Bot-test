# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T03:52:26.460963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `-0.0467` n `235`; crypto_major avg `-0.1537` n `8`; equity avg `-0.0385` n `144`; fx avg `-0.0129` n `6`; index avg `-0.0052` n `26`; metal avg `0.0072` n `20`; unknown avg `0.4583` n `1061`
- 1h: commodity avg `-0.0371` n `13`; crypto_alt avg `-0.5791` n `235`; crypto_major avg `-0.4352` n `8`; equity avg `-0.0862` n `144`; fx avg `-0.0626` n `6`; index avg `-0.0284` n `26`; metal avg `0.0105` n `20`; unknown avg `0.3218` n `1014`
- 4h: commodity avg `-0.0882` n `13`; crypto_alt avg `-0.0828` n `235`; crypto_major avg `-0.2595` n `8`; equity avg `0.0366` n `144`; fx avg `-0.134` n `6`; index avg `-0.018` n `26`; metal avg `0.0602` n `20`; unknown avg `0.4863` n `996`
- 24h: commodity avg `-0.3191` n `13`; crypto_alt avg `0.9594` n `235`; crypto_major avg `1.1811` n `8`; equity avg `0.3819` n `144`; fx avg `-0.1262` n `6`; index avg `-0.0208` n `26`; metal avg `0.1076` n `20`; unknown avg `0.2441` n `906`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal

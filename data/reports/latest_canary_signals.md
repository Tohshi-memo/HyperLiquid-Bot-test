# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T01:52:38.859679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0793` n `12`; crypto_alt avg `0.0257` n `230`; crypto_major avg `0.1157` n `8`; equity avg `0.0532` n `96`; fx avg `0.0054` n `6`; index avg `0.0023` n `25`; metal avg `0.0085` n `20`; unknown avg `0.0057` n `770`
- 1h: commodity avg `-0.0598` n `12`; crypto_alt avg `-0.0432` n `230`; crypto_major avg `0.0329` n `8`; equity avg `0.0472` n `96`; fx avg `0.0073` n `6`; index avg `-0.0084` n `25`; metal avg `0.0209` n `20`; unknown avg `-0.2283` n `770`
- 4h: commodity avg `-0.0208` n `12`; crypto_alt avg `0.0871` n `230`; crypto_major avg `0.1891` n `8`; equity avg `0.1801` n `96`; fx avg `0.0397` n `6`; index avg `-0.0051` n `25`; metal avg `0.0359` n `20`; unknown avg `-0.5191` n `770`
- 24h: commodity avg `0.2789` n `12`; crypto_alt avg `-0.1858` n `230`; crypto_major avg `0.7031` n `8`; equity avg `-0.1823` n `96`; fx avg `-0.0298` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0448` n `20`; unknown avg `0.0509` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal

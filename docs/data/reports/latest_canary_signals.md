# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T07:07:27.461145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0431` n `12`; crypto_alt avg `-0.0156` n `230`; crypto_major avg `-0.0578` n `8`; equity avg `0.0806` n `100`; fx avg `-0.0161` n `6`; index avg `0.0108` n `25`; metal avg `0.0672` n `20`; unknown avg `-0.032` n `775`
- 1h: commodity avg `-0.175` n `12`; crypto_alt avg `-0.3274` n `230`; crypto_major avg `-0.2344` n `8`; equity avg `0.2488` n `100`; fx avg `0.0293` n `6`; index avg `-0.0008` n `25`; metal avg `0.0745` n `20`; unknown avg `-0.0737` n `775`
- 4h: commodity avg `-0.3797` n `12`; crypto_alt avg `-0.0105` n `230`; crypto_major avg `0.5108` n `8`; equity avg `0.7162` n `100`; fx avg `0.0248` n `6`; index avg `0.124` n `25`; metal avg `0.1644` n `20`; unknown avg `-0.0219` n `759`
- 24h: commodity avg `-0.8166` n `12`; crypto_alt avg `0.7443` n `230`; crypto_major avg `1.3784` n `8`; equity avg `1.3658` n `100`; fx avg `0.0962` n `6`; index avg `0.1821` n `25`; metal avg `0.4895` n `20`; unknown avg `-0.0959` n `759`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal

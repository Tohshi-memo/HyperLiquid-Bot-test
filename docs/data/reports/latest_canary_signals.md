# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T12:52:27.872805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `0.0936` n `235`; crypto_major avg `-0.0988` n `8`; equity avg `-0.0125` n `144`; fx avg `0.0019` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0058` n `20`; unknown avg `0.0932` n `1078`
- 1h: commodity avg `0.0226` n `13`; crypto_alt avg `0.041` n `235`; crypto_major avg `-0.0207` n `8`; equity avg `0.0126` n `144`; fx avg `0.0013` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.1714` n `1070`
- 4h: commodity avg `0.0469` n `13`; crypto_alt avg `-0.2293` n `235`; crypto_major avg `0.0786` n `8`; equity avg `0.0305` n `144`; fx avg `0.031` n `6`; index avg `0.0075` n `26`; metal avg `-0.0138` n `20`; unknown avg `-0.0068` n `1070`
- 24h: commodity avg `0.2254` n `13`; crypto_alt avg `1.883` n `235`; crypto_major avg `1.1209` n `8`; equity avg `0.2571` n `144`; fx avg `0.0096` n `6`; index avg `0.0381` n `26`; metal avg `0.0039` n `20`; unknown avg `-0.1032` n `901`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal

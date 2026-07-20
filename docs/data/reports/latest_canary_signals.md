# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T04:07:25.458095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.2141` n `230`; crypto_major avg `-0.2238` n `8`; equity avg `-0.103` n `98`; fx avg `-0.0014` n `6`; index avg `-0.0581` n `25`; metal avg `-0.0523` n `20`; unknown avg `0.1326` n `769`
- 1h: commodity avg `0.0641` n `12`; crypto_alt avg `-0.2718` n `230`; crypto_major avg `-0.1945` n `8`; equity avg `0.1319` n `98`; fx avg `-0.0099` n `6`; index avg `0.0155` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.2114` n `769`
- 4h: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.2468` n `230`; crypto_major avg `-0.3018` n `8`; equity avg `-0.4882` n `98`; fx avg `-0.0768` n `6`; index avg `-0.0949` n `25`; metal avg `0.2232` n `20`; unknown avg `0.8026` n `769`
- 24h: commodity avg `-0.0374` n `12`; crypto_alt avg `0.0499` n `230`; crypto_major avg `0.2137` n `8`; equity avg `0.2474` n `97`; fx avg `-0.0187` n `6`; index avg `0.0166` n `25`; metal avg `0.1054` n `20`; unknown avg `0.0001` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1027`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.099`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0908`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0872`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0829`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0784`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal

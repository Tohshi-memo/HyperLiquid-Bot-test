# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T06:52:16.978784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.253` n `12`; crypto_alt avg `0.1314` n `228`; crypto_major avg `0.1326` n `8`; equity avg `0.106` n `67`; fx avg `0.0067` n `6`; index avg `0.0006` n `23`; metal avg `0.0924` n `18`; unknown avg `0.951` n `418`
- 1h: commodity avg `-0.156` n `12`; crypto_alt avg `0.4251` n `228`; crypto_major avg `0.4049` n `8`; equity avg `0.1108` n `67`; fx avg `0.0156` n `6`; index avg `-0.0756` n `23`; metal avg `-0.2818` n `18`; unknown avg `0.278` n `400`
- 4h: commodity avg `-0.4348` n `12`; crypto_alt avg `0.5043` n `228`; crypto_major avg `0.6355` n `8`; equity avg `-0.2745` n `67`; fx avg `0.0365` n `6`; index avg `-0.3087` n `23`; metal avg `-0.863` n `18`; unknown avg `1.2804` n `400`
- 24h: commodity avg `-0.5247` n `12`; crypto_alt avg `-0.9579` n `228`; crypto_major avg `-0.1832` n `8`; equity avg `0.4307` n `67`; fx avg `0.0036` n `6`; index avg `0.6994` n `23`; metal avg `-0.8195` n `18`; unknown avg `1.6196` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal

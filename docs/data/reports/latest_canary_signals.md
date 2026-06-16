# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T07:37:29.126121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1331` n `12`; crypto_alt avg `0.3799` n `228`; crypto_major avg `0.1412` n `8`; equity avg `0.0178` n `77`; fx avg `-0.0022` n `6`; index avg `0.0213` n `23`; metal avg `0.0185` n `18`; unknown avg `0.1255` n `687`
- 1h: commodity avg `-0.3457` n `12`; crypto_alt avg `0.1909` n `228`; crypto_major avg `0.0777` n `8`; equity avg `0.0365` n `77`; fx avg `0.0086` n `6`; index avg `0.0186` n `23`; metal avg `0.2458` n `18`; unknown avg `0.0935` n `687`
- 4h: commodity avg `-0.263` n `12`; crypto_alt avg `0.7593` n `228`; crypto_major avg `0.9524` n `8`; equity avg `0.2788` n `77`; fx avg `-0.0186` n `6`; index avg `-0.0432` n `23`; metal avg `0.1354` n `18`; unknown avg `0.9454` n `647`
- 24h: commodity avg `0.4986` n `12`; crypto_alt avg `0.9988` n `228`; crypto_major avg `2.9297` n `8`; equity avg `1.3523` n `76`; fx avg `-0.114` n `6`; index avg `0.4242` n `23`; metal avg `0.1027` n `18`; unknown avg `1.5448` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T19:01:15.576387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `13`; crypto_alt avg `0.0584` n `234`; crypto_major avg `0.0798` n `8`; equity avg `0.0096` n `142`; fx avg `-0.0048` n `6`; index avg `0.0003` n `26`; metal avg `-0.0042` n `20`; unknown avg `4.5612` n `973`
- 1h: commodity avg `-0.1058` n `13`; crypto_alt avg `0.0014` n `234`; crypto_major avg `0.0849` n `8`; equity avg `0.3562` n `142`; fx avg `-0.0061` n `6`; index avg `0.0808` n `26`; metal avg `0.0802` n `20`; unknown avg `0.3054` n `973`
- 4h: commodity avg `0.0` n `13`; crypto_alt avg `1.163` n `234`; crypto_major avg `0.5828` n `8`; equity avg `1.2567` n `142`; fx avg `-0.0586` n `6`; index avg `0.2477` n `26`; metal avg `0.1419` n `20`; unknown avg `2.1223` n `957`
- 24h: commodity avg `-0.0273` n `13`; crypto_alt avg `-0.0109` n `234`; crypto_major avg `0.078` n `8`; equity avg `0.8647` n `142`; fx avg `-0.0886` n `6`; index avg `0.1414` n `26`; metal avg `-0.04` n `20`; unknown avg `-0.0408` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal

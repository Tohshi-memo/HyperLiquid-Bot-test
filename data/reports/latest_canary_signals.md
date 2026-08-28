# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T01:22:23.707813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.4726` n `231`; crypto_major avg `0.4883` n `8`; equity avg `0.0646` n `127`; fx avg `-0.0038` n `6`; index avg `0.0066` n `26`; metal avg `0.0269` n `20`; unknown avg `-0.1005` n `792`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `0.6969` n `231`; crypto_major avg `0.5751` n `8`; equity avg `0.1793` n `127`; fx avg `-0.0289` n `6`; index avg `0.0334` n `26`; metal avg `0.0585` n `20`; unknown avg `-0.3386` n `792`
- 4h: commodity avg `-0.0007` n `12`; crypto_alt avg `0.8904` n `231`; crypto_major avg `0.6712` n `8`; equity avg `0.0787` n `127`; fx avg `-0.0255` n `6`; index avg `0.0424` n `26`; metal avg `0.0219` n `20`; unknown avg `-0.2151` n `792`
- 24h: commodity avg `0.2539` n `12`; crypto_alt avg `2.4629` n `231`; crypto_major avg `3.2979` n `8`; equity avg `0.414` n `127`; fx avg `0.017` n `6`; index avg `0.1036` n `26`; metal avg `0.0035` n `20`; unknown avg `0.8978` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal

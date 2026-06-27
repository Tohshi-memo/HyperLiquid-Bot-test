# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T23:37:25.319054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0072` n `228`; crypto_major avg `-0.0855` n `8`; equity avg `-0.0095` n `88`; fx avg `-0.0033` n `6`; index avg `-0.0004` n `23`; metal avg `0.0079` n `20`; unknown avg `-0.1773` n `764`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.2598` n `228`; crypto_major avg `-0.4374` n `8`; equity avg `-0.0906` n `88`; fx avg `0.0017` n `6`; index avg `-0.009` n `23`; metal avg `-0.0003` n `20`; unknown avg `-0.4769` n `764`
- 4h: commodity avg `0.1399` n `12`; crypto_alt avg `0.0447` n `228`; crypto_major avg `-0.295` n `8`; equity avg `-0.0029` n `88`; fx avg `0.0075` n `6`; index avg `-0.0413` n `23`; metal avg `0.0076` n `20`; unknown avg `-0.7611` n `764`
- 24h: commodity avg `0.1579` n `12`; crypto_alt avg `-0.8904` n `228`; crypto_major avg `-1.3326` n `8`; equity avg `0.1982` n `88`; fx avg `0.0394` n `6`; index avg `-0.0689` n `23`; metal avg `-0.0645` n `20`; unknown avg `-1.0397` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal

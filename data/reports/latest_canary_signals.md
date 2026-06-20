# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T16:59:02.843343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `0.3698` n `228`; crypto_major avg `0.1117` n `8`; equity avg `-0.0024` n `78`; fx avg `0.0255` n `6`; index avg `0.0076` n `23`; metal avg `-0.014` n `18`; unknown avg `0.0215` n `701`
- 1h: commodity avg `0.0599` n `12`; crypto_alt avg `-0.0105` n `228`; crypto_major avg `-0.3251` n `8`; equity avg `-0.0469` n `78`; fx avg `0.0307` n `6`; index avg `-0.008` n `23`; metal avg `-0.0508` n `18`; unknown avg `0.135` n `701`
- 4h: commodity avg `0.2349` n `12`; crypto_alt avg `0.6048` n `228`; crypto_major avg `0.0387` n `8`; equity avg `-0.0016` n `78`; fx avg `0.0397` n `6`; index avg `-0.0137` n `23`; metal avg `-0.0317` n `18`; unknown avg `0.047` n `701`
- 24h: commodity avg `0.2668` n `12`; crypto_alt avg `0.8189` n `228`; crypto_major avg `1.335` n `8`; equity avg `0.3911` n `78`; fx avg `0.0886` n `6`; index avg `0.0135` n `23`; metal avg `0.1629` n `18`; unknown avg `-0.0665` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal

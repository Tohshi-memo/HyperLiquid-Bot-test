# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T01:07:15.382902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1587` n `12`; crypto_alt avg `0.1074` n `228`; crypto_major avg `0.0622` n `8`; equity avg `0.0605` n `66`; fx avg `0.0277` n `6`; index avg `0.025` n `23`; metal avg `-0.0091` n `18`; unknown avg `-0.0597` n `384`
- 1h: commodity avg `-0.1302` n `12`; crypto_alt avg `0.8172` n `228`; crypto_major avg `0.7248` n `8`; equity avg `0.5434` n `66`; fx avg `0.0249` n `6`; index avg `0.2616` n `23`; metal avg `0.095` n `18`; unknown avg `0.3554` n `384`
- 4h: commodity avg `-0.3339` n `12`; crypto_alt avg `0.4711` n `228`; crypto_major avg `1.2953` n `8`; equity avg `0.2731` n `66`; fx avg `0.0602` n `6`; index avg `0.0662` n `23`; metal avg `0.018` n `18`; unknown avg `1.8006` n `384`
- 24h: commodity avg `-2.3935` n `12`; crypto_alt avg `3.9076` n `228`; crypto_major avg `3.8025` n `8`; equity avg `2.3091` n `66`; fx avg `-0.0178` n `6`; index avg `1.366` n `23`; metal avg `1.4557` n `18`; unknown avg `3.4157` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal

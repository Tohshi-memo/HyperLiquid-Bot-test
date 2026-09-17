# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T05:07:31.248839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `-0.0482` n `234`; crypto_major avg `-0.0349` n `8`; equity avg `-0.0135` n `137`; fx avg `0.0063` n `6`; index avg `-0.0159` n `27`; metal avg `-0.0127` n `20`; unknown avg `0.4746` n `919`
- 1h: commodity avg `-0.0089` n `12`; crypto_alt avg `0.3574` n `234`; crypto_major avg `0.0437` n `8`; equity avg `-0.0132` n `137`; fx avg `0.0219` n `6`; index avg `-0.0207` n `27`; metal avg `-0.0034` n `20`; unknown avg `0.2994` n `913`
- 4h: commodity avg `0.1794` n `12`; crypto_alt avg `0.7168` n `234`; crypto_major avg `0.4382` n `8`; equity avg `0.1577` n `137`; fx avg `0.0261` n `6`; index avg `-0.0142` n `27`; metal avg `0.0303` n `20`; unknown avg `0.259` n `911`
- 24h: commodity avg `-0.4083` n `12`; crypto_alt avg `2.4176` n `234`; crypto_major avg `1.4617` n `8`; equity avg `1.2801` n `137`; fx avg `0.046` n `6`; index avg `0.1161` n `27`; metal avg `-0.2002` n `20`; unknown avg `0.4345` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal

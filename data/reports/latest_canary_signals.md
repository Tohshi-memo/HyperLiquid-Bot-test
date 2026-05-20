# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T07:37:15.413207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.0074` n `228`; crypto_major avg `0.0135` n `8`; equity avg `-0.1113` n `66`; fx avg `0.0058` n `6`; index avg `-0.0187` n `23`; metal avg `-0.0669` n `18`; unknown avg `0.077` n `384`
- 1h: commodity avg `-0.0925` n `12`; crypto_alt avg `0.3103` n `228`; crypto_major avg `0.146` n `8`; equity avg `0.2088` n `66`; fx avg `0.0025` n `6`; index avg `0.0637` n `23`; metal avg `0.3095` n `18`; unknown avg `0.1601` n `384`
- 4h: commodity avg `-0.215` n `12`; crypto_alt avg `1.1291` n `228`; crypto_major avg `0.8294` n `8`; equity avg `0.5899` n `66`; fx avg `-0.0338` n `6`; index avg `0.2662` n `23`; metal avg `0.736` n `18`; unknown avg `0.3159` n `374`
- 24h: commodity avg `0.0725` n `12`; crypto_alt avg `-0.1351` n `228`; crypto_major avg `-0.258` n `8`; equity avg `0.3215` n `66`; fx avg `-0.1765` n `6`; index avg `-0.4635` n `23`; metal avg `-1.1619` n `18`; unknown avg `0.1184` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal

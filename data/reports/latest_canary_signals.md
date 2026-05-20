# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T08:22:20.754337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.13` n `12`; crypto_alt avg `-0.1313` n `228`; crypto_major avg `-0.0686` n `8`; equity avg `-0.0635` n `66`; fx avg `-0.0063` n `6`; index avg `0.078` n `23`; metal avg `0.0293` n `18`; unknown avg `0.043` n `384`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.1847` n `228`; crypto_major avg `-0.101` n `8`; equity avg `-0.0206` n `66`; fx avg `0.0001` n `6`; index avg `0.1107` n `23`; metal avg `0.0343` n `18`; unknown avg `-0.0703` n `384`
- 4h: commodity avg `-0.1645` n `12`; crypto_alt avg `0.9702` n `228`; crypto_major avg `0.7601` n `8`; equity avg `0.6077` n `66`; fx avg `-0.0545` n `6`; index avg `0.3341` n `23`; metal avg `0.9155` n `18`; unknown avg `0.3147` n `374`
- 24h: commodity avg `0.1265` n `12`; crypto_alt avg `-0.0112` n `228`; crypto_major avg `-0.1805` n `8`; equity avg `0.5331` n `66`; fx avg `-0.1753` n `6`; index avg `-0.2733` n `23`; metal avg `-1.0757` n `18`; unknown avg `0.2065` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0466`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T01:07:32.720299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `13`; crypto_alt avg `0.0734` n `235`; crypto_major avg `0.1285` n `8`; equity avg `0.0595` n `144`; fx avg `-0.0016` n `6`; index avg `0.0181` n `26`; metal avg `0.0287` n `20`; unknown avg `-0.0402` n `1077`
- 1h: commodity avg `0.021` n `13`; crypto_alt avg `-0.3664` n `235`; crypto_major avg `0.2122` n `8`; equity avg `0.1257` n `144`; fx avg `-0.0207` n `6`; index avg `0.0324` n `26`; metal avg `0.1311` n `20`; unknown avg `-0.02` n `1077`
- 4h: commodity avg `0.0199` n `13`; crypto_alt avg `-0.0677` n `235`; crypto_major avg `0.3179` n `8`; equity avg `0.1687` n `144`; fx avg `0.0158` n `6`; index avg `0.0127` n `26`; metal avg `0.1007` n `20`; unknown avg `-0.0872` n `1019`
- 24h: commodity avg `-0.1453` n `13`; crypto_alt avg `-0.3147` n `235`; crypto_major avg `0.0999` n `8`; equity avg `0.0593` n `144`; fx avg `0.0163` n `6`; index avg `0.095` n `26`; metal avg `0.0465` n `20`; unknown avg `625.3863` n `800`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal

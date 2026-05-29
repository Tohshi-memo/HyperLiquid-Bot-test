# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T19:52:18.516913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0756` n `12`; crypto_alt avg `-0.0109` n `228`; crypto_major avg `-0.0587` n `8`; equity avg `0.1414` n `69`; fx avg `-0.0017` n `6`; index avg `-0.0252` n `23`; metal avg `-0.1042` n `18`; unknown avg `-0.0239` n `419`
- 1h: commodity avg `0.034` n `12`; crypto_alt avg `0.1796` n `228`; crypto_major avg `0.4356` n `8`; equity avg `0.355` n `69`; fx avg `0.0132` n `6`; index avg `0.0981` n `23`; metal avg `-0.0155` n `18`; unknown avg `0.0435` n `419`
- 4h: commodity avg `-0.1156` n `12`; crypto_alt avg `-0.4772` n `228`; crypto_major avg `-0.0196` n `8`; equity avg `0.139` n `69`; fx avg `-0.0089` n `6`; index avg `0.0908` n `23`; metal avg `-0.1808` n `18`; unknown avg `0.8802` n `418`
- 24h: commodity avg `-0.5141` n `12`; crypto_alt avg `0.5799` n `228`; crypto_major avg `1.0071` n `8`; equity avg `1.2509` n `69`; fx avg `0.2162` n `6`; index avg `-0.0293` n `23`; metal avg `0.1843` n `18`; unknown avg `1.616` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T03:22:16.727084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0535` n `12`; crypto_alt avg `-0.0554` n `228`; crypto_major avg `-0.1646` n `8`; equity avg `-0.0675` n `67`; fx avg `0.0084` n `6`; index avg `-0.0178` n `23`; metal avg `-0.046` n `18`; unknown avg `-0.1896` n `418`
- 1h: commodity avg `-0.1546` n `12`; crypto_alt avg `0.254` n `228`; crypto_major avg `0.3627` n `8`; equity avg `-0.0249` n `67`; fx avg `-0.0222` n `6`; index avg `-0.0066` n `23`; metal avg `0.1536` n `18`; unknown avg `-0.405` n `418`
- 4h: commodity avg `-0.4551` n `12`; crypto_alt avg `-0.3696` n `228`; crypto_major avg `0.3102` n `8`; equity avg `0.1678` n `67`; fx avg `-0.0525` n `6`; index avg `0.138` n `23`; metal avg `-0.111` n `18`; unknown avg `-0.1806` n `418`
- 24h: commodity avg `-0.1061` n `12`; crypto_alt avg `-0.125` n `228`; crypto_major avg `0.1323` n `8`; equity avg `0.7501` n `67`; fx avg `-0.0561` n `6`; index avg `1.022` n `23`; metal avg `-0.1815` n `18`; unknown avg `0.8012` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1851`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal

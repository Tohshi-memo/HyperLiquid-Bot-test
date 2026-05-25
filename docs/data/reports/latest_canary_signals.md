# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T15:22:16.981325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3918` n `12`; crypto_alt avg `-0.2813` n `228`; crypto_major avg `-0.2503` n `8`; equity avg `-0.0056` n `67`; fx avg `0.0065` n `6`; index avg `0.0613` n `23`; metal avg `0.1081` n `18`; unknown avg `-0.0808` n `405`
- 1h: commodity avg `-0.252` n `12`; crypto_alt avg `-0.0311` n `228`; crypto_major avg `-0.1611` n `8`; equity avg `0.0779` n `67`; fx avg `-0.0027` n `6`; index avg `0.0291` n `23`; metal avg `0.3495` n `18`; unknown avg `0.0082` n `405`
- 4h: commodity avg `0.0696` n `12`; crypto_alt avg `0.4559` n `228`; crypto_major avg `0.2642` n `8`; equity avg `0.0842` n `67`; fx avg `-0.0084` n `6`; index avg `0.0924` n `23`; metal avg `0.2696` n `18`; unknown avg `-0.2354` n `397`
- 24h: commodity avg `-0.7126` n `12`; crypto_alt avg `2.1765` n `228`; crypto_major avg `0.8677` n `8`; equity avg `0.9136` n `67`; fx avg `-0.0026` n `6`; index avg `0.508` n `23`; metal avg `1.5759` n `18`; unknown avg `0.898` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal

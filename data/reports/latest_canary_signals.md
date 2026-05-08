# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T09:07:19.502592+00:00`
- Correlation status: `ready`
- Asset price records: `632`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0887` n `12`; crypto_alt avg `-0.0639` n `228`; crypto_major avg `-0.0179` n `8`; equity avg `0.1412` n `65`; fx avg `0.0014` n `5`; index avg `0.0651` n `23`; metal avg `0.054` n `18`; unknown avg `0.0186` n `375`
- 1h: commodity avg `-0.2253` n `12`; crypto_alt avg `0.0986` n `228`; crypto_major avg `0.0944` n `8`; equity avg `0.2772` n `65`; fx avg `0.0131` n `5`; index avg `0.1107` n `23`; metal avg `0.2391` n `18`; unknown avg `0.2284` n `375`
- 4h: commodity avg `-0.2311` n `12`; crypto_alt avg `0.1874` n `228`; crypto_major avg `0.3355` n `8`; equity avg `1.005` n `65`; fx avg `0.0794` n `5`; index avg `0.2953` n `23`; metal avg `0.3733` n `18`; unknown avg `0.5931` n `355`
- 24h: commodity avg `1.0081` n `12`; crypto_alt avg `0.8647` n `228`; crypto_major avg `-1.5939` n `8`; equity avg `-0.1862` n `65`; fx avg `0.2351` n `5`; index avg `-0.4234` n `23`; metal avg `-0.2739` n `18`; unknown avg `-0.0676` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1344`, n `624`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1338`, n `624`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `628`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `628`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `628`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `628`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.086`, n `624`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0845`, n `624`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `624`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0731`, n `628`, weak_sample_signal

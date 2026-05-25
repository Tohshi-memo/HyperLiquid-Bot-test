# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T03:07:17.178825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1763` n `12`; crypto_alt avg `-0.0429` n `228`; crypto_major avg `-0.0814` n `8`; equity avg `0.0385` n `67`; fx avg `-0.0062` n `6`; index avg `0.0502` n `23`; metal avg `-0.1616` n `18`; unknown avg `0.0808` n `396`
- 1h: commodity avg `-0.251` n `12`; crypto_alt avg `-0.3227` n `228`; crypto_major avg `-0.4433` n `8`; equity avg `-0.0226` n `67`; fx avg `-0.0427` n `6`; index avg `0.0578` n `23`; metal avg `-0.2647` n `18`; unknown avg `0.047` n `396`
- 4h: commodity avg `-0.0826` n `12`; crypto_alt avg `0.4134` n `228`; crypto_major avg `-0.1629` n `8`; equity avg `0.3973` n `67`; fx avg `-0.1813` n `6`; index avg `0.2526` n `23`; metal avg `-0.3802` n `18`; unknown avg `0.2916` n `396`
- 24h: commodity avg `-0.0458` n `12`; crypto_alt avg `-1.4197` n `228`; crypto_major avg `-0.3302` n `8`; equity avg `0.2892` n `67`; fx avg `-0.0612` n `6`; index avg `-0.1973` n `23`; metal avg `0.386` n `18`; unknown avg `-0.4148` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal

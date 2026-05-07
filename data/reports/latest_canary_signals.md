# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T18:22:24.608858+00:00`
- Correlation status: `ready`
- Asset price records: `573`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2231` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1199` n `12`; crypto_alt avg `0.0183` n `228`; crypto_major avg `-0.033` n `8`; equity avg `-0.1903` n `65`; fx avg `-0.0071` n `5`; index avg `-0.0963` n `23`; metal avg `-0.1288` n `18`; unknown avg `0.0056` n `365`
- 1h: commodity avg `-0.1949` n `12`; crypto_alt avg `0.749` n `228`; crypto_major avg `0.4307` n `8`; equity avg `0.0628` n `65`; fx avg `-0.0431` n `5`; index avg `0.0813` n `23`; metal avg `0.0085` n `18`; unknown avg `0.3742` n `365`
- 4h: commodity avg `1.974` n `12`; crypto_alt avg `0.5328` n `228`; crypto_major avg `-0.2491` n `8`; equity avg `-1.6862` n `65`; fx avg `0.0293` n `5`; index avg `-0.6132` n `23`; metal avg `-1.2838` n `18`; unknown avg `-0.2324` n `365`
- 24h: commodity avg `0.4004` n `12`; crypto_alt avg `1.4362` n `228`; crypto_major avg `-1.5052` n `8`; equity avg `-0.8911` n `65`; fx avg `0.1637` n `5`; index avg `-0.5754` n `23`; metal avg `0.5138` n `18`; unknown avg `0.0611` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `569`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `569`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `569`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `569`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0929`, n `565`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `565`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `565`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0882`, n `565`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0882`, n `565`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.073`, n `565`, weak_sample_signal

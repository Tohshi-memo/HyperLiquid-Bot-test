# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T18:07:36.589251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.864` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.8399` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0169` n `13`; crypto_alt avg `0.1839` n `239`; crypto_major avg `0.4309` n `8`; equity avg `0.2701` n `168`; fx avg `0.0016` n `6`; index avg `0.0181` n `27`; metal avg `0.1874` n `20`; unknown avg `1.0335` n `1257`
- 1h: commodity avg `0.1016` n `13`; crypto_alt avg `1.2969` n `239`; crypto_major avg `1.3045` n `8`; equity avg `1.71` n `168`; fx avg `0.0109` n `6`; index avg `0.19` n `27`; metal avg `0.3831` n `20`; unknown avg `237.4749` n `1262`
- 4h: commodity avg `0.4258` n `13`; crypto_alt avg `2.9693` n `239`; crypto_major avg `3.2657` n `8`; equity avg `1.9792` n `168`; fx avg `0.0572` n `6`; index avg `0.2184` n `27`; metal avg `0.4017` n `20`; unknown avg `44.231` n `1237`
- 24h: commodity avg `0.4586` n `13`; crypto_alt avg `0.4176` n `239`; crypto_major avg `-0.3063` n `8`; equity avg `-2.4983` n `168`; fx avg `-0.0074` n `6`; index avg `-0.2607` n `27`; metal avg `-0.3367` n `20`; unknown avg `445.7847` n `1071`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal

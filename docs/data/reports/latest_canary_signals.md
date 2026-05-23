# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T20:37:12.642255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1801` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.3213` n `12`; crypto_alt avg `0.3932` n `228`; crypto_major avg `0.4653` n `8`; equity avg `0.1666` n `67`; fx avg `0.0187` n `6`; index avg `0.1553` n `23`; metal avg `0.2376` n `18`; unknown avg `0.9359` n `396`
- 1h: commodity avg `-0.8648` n `12`; crypto_alt avg `0.3655` n `228`; crypto_major avg `0.6717` n `8`; equity avg `0.2469` n `67`; fx avg `0.014` n `6`; index avg `0.275` n `23`; metal avg `0.2796` n `18`; unknown avg `1.1773` n `396`
- 4h: commodity avg `-1.6532` n `12`; crypto_alt avg `1.596` n `228`; crypto_major avg `1.5269` n `8`; equity avg `0.7848` n `67`; fx avg `0.0056` n `6`; index avg `0.5979` n `23`; metal avg `0.4288` n `18`; unknown avg `2.9802` n `396`
- 24h: commodity avg `-1.5701` n `12`; crypto_alt avg `1.4638` n `228`; crypto_major avg `1.387` n `8`; equity avg `0.7846` n `67`; fx avg `-0.01` n `6`; index avg `0.5886` n `23`; metal avg `0.4714` n `18`; unknown avg `0.7313` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal

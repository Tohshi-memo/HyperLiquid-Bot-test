# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T14:18:13.995282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.52` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.1554` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0756` n `12`; crypto_alt avg `-0.3812` n `228`; crypto_major avg `-0.4321` n `8`; equity avg `-0.543` n `88`; fx avg `-0.0067` n `6`; index avg `-0.0958` n `23`; metal avg `-0.0128` n `20`; unknown avg `-0.0386` n `764`
- 1h: commodity avg `0.0808` n `12`; crypto_alt avg `-1.1939` n `228`; crypto_major avg `-1.4442` n `8`; equity avg `-1.9916` n `88`; fx avg `0.0253` n `6`; index avg `-0.2888` n `23`; metal avg `-0.3019` n `20`; unknown avg `-0.1465` n `764`
- 4h: commodity avg `-0.0165` n `12`; crypto_alt avg `-1.09` n `228`; crypto_major avg `-1.1217` n `8`; equity avg `-1.9097` n `88`; fx avg `0.0547` n `6`; index avg `-0.3078` n `23`; metal avg `-0.1713` n `20`; unknown avg `0.0433` n `764`
- 24h: commodity avg `-0.5584` n `12`; crypto_alt avg `-1.0323` n `228`; crypto_major avg `-0.99` n `8`; equity avg `-1.4842` n `88`; fx avg `0.1242` n `6`; index avg `-0.2385` n `23`; metal avg `-0.6587` n `20`; unknown avg `0.6686` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal

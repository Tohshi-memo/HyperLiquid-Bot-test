# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T04:52:23.082480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.7824` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.7241` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.66` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.4931` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0163` n `13`; crypto_alt avg `0.7039` n `239`; crypto_major avg `0.8462` n `8`; equity avg `0.2994` n `166`; fx avg `-0.0047` n `6`; index avg `0.0234` n `27`; metal avg `0.0646` n `20`; unknown avg `97.5595` n `1262`
- 1h: commodity avg `0.0063` n `13`; crypto_alt avg `0.412` n `239`; crypto_major avg `0.1557` n `8`; equity avg `-0.0258` n `166`; fx avg `-0.0038` n `6`; index avg `0.0263` n `27`; metal avg `0.0442` n `20`; unknown avg `33.0212` n `1242`
- 4h: commodity avg `-0.0251` n `13`; crypto_alt avg `-2.9977` n `239`; crypto_major avg `-3.8075` n `8`; equity avg `-1.3144` n `166`; fx avg `-0.0255` n `6`; index avg `-0.0834` n `27`; metal avg `-0.1475` n `20`; unknown avg `2.2117` n `1242`
- 24h: commodity avg `0.2469` n `13`; crypto_alt avg `-5.9462` n `239`; crypto_major avg `-7.8289` n `8`; equity avg `-5.7458` n `166`; fx avg `-0.0628` n `6`; index avg `-0.5969` n `27`; metal avg `-0.0651` n `20`; unknown avg `74.5902` n `1109`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal

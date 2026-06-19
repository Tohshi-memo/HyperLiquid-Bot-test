# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T18:22:31.344312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.1433` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.6805` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.6544` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.0522` n `228`; crypto_major avg `0.0744` n `8`; equity avg `-0.0` n `78`; fx avg `0.0141` n `6`; index avg `0.0015` n `23`; metal avg `-0.0218` n `18`; unknown avg `0.0026` n `687`
- 1h: commodity avg `-0.0066` n `12`; crypto_alt avg `0.2653` n `228`; crypto_major avg `0.4548` n `8`; equity avg `0.0275` n `78`; fx avg `0.0031` n `6`; index avg `0.0005` n `23`; metal avg `-0.0148` n `18`; unknown avg `0.0592` n `687`
- 4h: commodity avg `0.255` n `12`; crypto_alt avg `-3.3558` n `228`; crypto_major avg `-4.4255` n `8`; equity avg `0.7178` n `78`; fx avg `-0.0905` n `6`; index avg `0.2289` n `23`; metal avg `-4.2702` n `18`; unknown avg `-0.3401` n `572`
- 24h: commodity avg `0.255` n `12`; crypto_alt avg `-3.3558` n `228`; crypto_major avg `-4.4255` n `8`; equity avg `0.7178` n `78`; fx avg `-0.0905` n `6`; index avg `0.2289` n `23`; metal avg `-4.2702` n `18`; unknown avg `-0.3401` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal

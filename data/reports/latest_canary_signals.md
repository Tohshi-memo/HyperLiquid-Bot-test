# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T21:22:23.093764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.1384` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.73` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.5265` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4376` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `2.0738` n `12`; crypto_alt avg `0.1034` n `228`; crypto_major avg `-0.0691` n `8`; equity avg `0.0223` n `69`; fx avg `-0.0005` n `6`; index avg `0.0269` n `23`; metal avg `0.0009` n `18`; unknown avg `0.0565` n `422`
- 1h: commodity avg `1.9709` n `12`; crypto_alt avg `1.1894` n `228`; crypto_major avg `0.4223` n `8`; equity avg `0.2341` n `69`; fx avg `-0.0282` n `6`; index avg `0.0664` n `23`; metal avg `-0.0021` n `18`; unknown avg `1.1272` n `422`
- 4h: commodity avg `1.9332` n `12`; crypto_alt avg `-0.6083` n `228`; crypto_major avg `-1.2052` n `8`; equity avg `0.3213` n `69`; fx avg `-0.0181` n `6`; index avg `0.2324` n `23`; metal avg `-0.0041` n `18`; unknown avg `-0.2095` n `422`
- 24h: commodity avg `2.01` n `12`; crypto_alt avg `-2.8559` n `228`; crypto_major avg `-4.3745` n `8`; equity avg `1.2114` n `69`; fx avg `0.0593` n `6`; index avg `0.6987` n `23`; metal avg `0.4615` n `18`; unknown avg `0.0405` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal

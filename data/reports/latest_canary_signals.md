# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T23:22:20.919709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.2996` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.6197` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5558` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2636` n `12`; crypto_alt avg `-0.2082` n `228`; crypto_major avg `-0.1491` n `8`; equity avg `-0.3621` n `69`; fx avg `-0.0162` n `6`; index avg `-0.1481` n `23`; metal avg `-0.2859` n `18`; unknown avg `0.8981` n `422`
- 1h: commodity avg `0.4866` n `12`; crypto_alt avg `-1.2977` n `228`; crypto_major avg `-1.0114` n `8`; equity avg `-0.6425` n `69`; fx avg `-0.0216` n `6`; index avg `-0.1876` n `23`; metal avg `-0.5432` n `18`; unknown avg `-0.3051` n `422`
- 4h: commodity avg `0.6386` n `12`; crypto_alt avg `-1.2731` n `228`; crypto_major avg `-1.661` n `8`; equity avg `-0.1052` n `69`; fx avg `-0.0505` n `6`; index avg `-0.0413` n `23`; metal avg `-0.4316` n `18`; unknown avg `0.5933` n `422`
- 24h: commodity avg `0.6485` n `12`; crypto_alt avg `-5.3715` n `228`; crypto_major avg `-6.6804` n `8`; equity avg `0.6297` n `69`; fx avg `0.0546` n `6`; index avg `0.5451` n `23`; metal avg `-0.1875` n `18`; unknown avg `-0.6733` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal

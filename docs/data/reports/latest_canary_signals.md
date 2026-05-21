# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T18:22:16.143530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.4` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.6051` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0262` n `12`; crypto_alt avg `0.2425` n `228`; crypto_major avg `0.1473` n `8`; equity avg `-0.0564` n `67`; fx avg `0.0217` n `6`; index avg `-0.0541` n `23`; metal avg `0.1371` n `18`; unknown avg `0.2572` n `386`
- 1h: commodity avg `-0.3603` n `12`; crypto_alt avg `0.5796` n `228`; crypto_major avg `-0.0387` n `8`; equity avg `0.1075` n `67`; fx avg `0.031` n `6`; index avg `0.161` n `23`; metal avg `0.1298` n `18`; unknown avg `0.0244` n `386`
- 4h: commodity avg `-1.4185` n `12`; crypto_alt avg `2.1536` n `228`; crypto_major avg `1.1866` n `8`; equity avg `1.6378` n `67`; fx avg `0.0238` n `6`; index avg `0.6711` n `23`; metal avg `1.4946` n `18`; unknown avg `1.1786` n `385`
- 24h: commodity avg `-0.7179` n `12`; crypto_alt avg `2.3949` n `228`; crypto_major avg `2.3987` n `8`; equity avg `1.7179` n `66`; fx avg `0.025` n `6`; index avg `0.7158` n `23`; metal avg `0.5758` n `18`; unknown avg `5.6027` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal

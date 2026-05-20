# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T15:22:18.496234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7858` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.5817` n `12`; crypto_alt avg `0.5688` n `228`; crypto_major avg `0.4423` n `8`; equity avg `0.3837` n `66`; fx avg `0.0013` n `6`; index avg `0.1102` n `23`; metal avg `0.3905` n `18`; unknown avg `0.0896` n `384`
- 1h: commodity avg `-0.5858` n `12`; crypto_alt avg `0.6883` n `228`; crypto_major avg `0.5539` n `8`; equity avg `0.5231` n `66`; fx avg `-0.0257` n `6`; index avg `0.1786` n `23`; metal avg `0.5598` n `18`; unknown avg `-0.199` n `384`
- 4h: commodity avg `-1.7136` n `12`; crypto_alt avg `1.3932` n `228`; crypto_major avg `1.0722` n `8`; equity avg `0.7455` n `66`; fx avg `-0.0024` n `6`; index avg `0.7735` n `23`; metal avg `0.7798` n `18`; unknown avg `1.1752` n `384`
- 24h: commodity avg `-1.9532` n `12`; crypto_alt avg `3.0196` n `228`; crypto_major avg `2.1487` n `8`; equity avg `2.6218` n `66`; fx avg `-0.0761` n `6`; index avg `1.5322` n `23`; metal avg `1.4632` n `18`; unknown avg `0.9705` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal

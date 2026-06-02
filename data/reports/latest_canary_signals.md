# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T18:52:30.893082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.37` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.2995` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.772` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6805` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0407` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.3447` n `228`; crypto_major avg `-0.3025` n `8`; equity avg `0.0548` n `69`; fx avg `0.0115` n `6`; index avg `0.0154` n `23`; metal avg `0.0119` n `18`; unknown avg `-0.4133` n `422`
- 1h: commodity avg `0.0312` n `12`; crypto_alt avg `-1.1121` n `228`; crypto_major avg `-0.9636` n `8`; equity avg `-0.0877` n `69`; fx avg `-0.0027` n `6`; index avg `0.0771` n `23`; metal avg `0.0631` n `18`; unknown avg `-0.2427` n `422`
- 4h: commodity avg `0.6175` n `12`; crypto_alt avg `-1.2658` n `228`; crypto_major avg `-1.682` n `8`; equity avg `-0.0015` n `69`; fx avg `-0.0427` n `6`; index avg `0.09` n `23`; metal avg `-0.339` n `18`; unknown avg `0.6957` n `422`
- 24h: commodity avg `-0.1837` n `12`; crypto_alt avg `-3.8369` n `228`; crypto_major avg `-4.4509` n `8`; equity avg `0.0087` n `69`; fx avg `0.0557` n `6`; index avg `0.1639` n `23`; metal avg `0.1192` n `18`; unknown avg `-0.3469` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T14:52:29.159986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0166` n `12`; crypto_alt avg `-0.0027` n `230`; crypto_major avg `-0.0385` n `8`; equity avg `-0.021` n `108`; fx avg `0.0057` n `6`; index avg `-0.0146` n `25`; metal avg `-0.0425` n `20`; unknown avg `-0.0647` n `782`
- 1h: commodity avg `-0.1574` n `12`; crypto_alt avg `0.0681` n `230`; crypto_major avg `0.1827` n `8`; equity avg `-0.8774` n `108`; fx avg `0.0101` n `6`; index avg `-0.1403` n `25`; metal avg `0.1057` n `20`; unknown avg `-0.0082` n `782`
- 4h: commodity avg `-0.3962` n `12`; crypto_alt avg `0.039` n `230`; crypto_major avg `0.2907` n `8`; equity avg `-0.1521` n `108`; fx avg `-0.007` n `6`; index avg `0.0306` n `25`; metal avg `0.278` n `20`; unknown avg `-0.0462` n `782`
- 24h: commodity avg `-0.3179` n `12`; crypto_alt avg `0.772` n `230`; crypto_major avg `0.4556` n `8`; equity avg `0.664` n `108`; fx avg `0.0358` n `6`; index avg `0.2709` n `25`; metal avg `0.7158` n `20`; unknown avg `0.6788` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal

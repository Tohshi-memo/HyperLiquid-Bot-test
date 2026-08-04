# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T08:52:35.459515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1029` n `12`; crypto_alt avg `0.0231` n `230`; crypto_major avg `0.0601` n `8`; equity avg `-0.0804` n `107`; fx avg `0.0132` n `6`; index avg `-0.009` n `25`; metal avg `-0.0603` n `20`; unknown avg `0.0014` n `781`
- 1h: commodity avg `0.2445` n `12`; crypto_alt avg `-0.0561` n `230`; crypto_major avg `-0.1854` n `8`; equity avg `0.0199` n `107`; fx avg `0.009` n `6`; index avg `-0.0295` n `25`; metal avg `-0.0678` n `20`; unknown avg `0.04` n `781`
- 4h: commodity avg `0.1547` n `12`; crypto_alt avg `-0.316` n `230`; crypto_major avg `-0.3815` n `8`; equity avg `0.7749` n `107`; fx avg `0.0755` n `6`; index avg `0.1155` n `25`; metal avg `0.0168` n `20`; unknown avg `0.8259` n `765`
- 24h: commodity avg `0.2638` n `12`; crypto_alt avg `1.2597` n `230`; crypto_major avg `1.5227` n `8`; equity avg `3.1979` n `107`; fx avg `0.087` n `6`; index avg `0.3046` n `25`; metal avg `0.0952` n `20`; unknown avg `1.1103` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal

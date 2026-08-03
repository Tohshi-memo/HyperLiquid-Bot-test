# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T18:37:28.009369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0804` n `12`; crypto_alt avg `-0.0358` n `230`; crypto_major avg `-0.1211` n `8`; equity avg `-0.195` n `103`; fx avg `0.0022` n `6`; index avg `-0.031` n `25`; metal avg `-0.009` n `20`; unknown avg `0.4866` n `784`
- 1h: commodity avg `0.0835` n `12`; crypto_alt avg `0.1831` n `230`; crypto_major avg `-0.0458` n `8`; equity avg `0.0808` n `103`; fx avg `-0.0235` n `6`; index avg `-0.0018` n `25`; metal avg `0.0228` n `20`; unknown avg `0.545` n `784`
- 4h: commodity avg `0.1694` n `12`; crypto_alt avg `0.4172` n `230`; crypto_major avg `0.2657` n `8`; equity avg `1.0382` n `103`; fx avg `0.0139` n `6`; index avg `0.1529` n `25`; metal avg `0.0921` n `20`; unknown avg `-0.0448` n `784`
- 24h: commodity avg `-0.0382` n `12`; crypto_alt avg `0.3983` n `230`; crypto_major avg `0.459` n `8`; equity avg `1.8048` n `102`; fx avg `-0.2147` n `6`; index avg `0.0513` n `25`; metal avg `-0.4741` n `20`; unknown avg `0.0453` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T19:02:20.218735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.2456` n `228`; crypto_major avg `0.0482` n `8`; equity avg `-0.1178` n `73`; fx avg `0.027` n `6`; index avg `-0.0198` n `23`; metal avg `-0.0063` n `18`; unknown avg `-0.1024` n `419`
- 1h: commodity avg `0.138` n `12`; crypto_alt avg `0.1404` n `228`; crypto_major avg `0.0382` n `8`; equity avg `-0.1316` n `73`; fx avg `-0.0218` n `6`; index avg `-0.0356` n `23`; metal avg `-0.0468` n `18`; unknown avg `-0.1367` n `419`
- 4h: commodity avg `0.2572` n `12`; crypto_alt avg `-0.574` n `228`; crypto_major avg `-0.3356` n `8`; equity avg `-0.6068` n `73`; fx avg `-0.0224` n `6`; index avg `-0.2552` n `23`; metal avg `-0.5876` n `18`; unknown avg `-0.544` n `419`
- 24h: commodity avg `0.8571` n `12`; crypto_alt avg `1.7615` n `228`; crypto_major avg `-1.487` n `8`; equity avg `-1.7801` n `72`; fx avg `0.0209` n `6`; index avg `-0.2704` n `23`; metal avg `-2.034` n `18`; unknown avg `0.0189` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal

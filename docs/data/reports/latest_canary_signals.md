# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T13:22:56.947658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1421` n `12`; crypto_alt avg `-0.0429` n `230`; crypto_major avg `-0.0148` n `8`; equity avg `-0.101` n `112`; fx avg `-0.0018` n `6`; index avg `-0.0288` n `25`; metal avg `-0.0302` n `20`; unknown avg `-0.0162` n `782`
- 1h: commodity avg `0.1112` n `12`; crypto_alt avg `-0.037` n `230`; crypto_major avg `0.0802` n `8`; equity avg `0.758` n `112`; fx avg `-0.0619` n `6`; index avg `0.0933` n `25`; metal avg `0.1412` n `20`; unknown avg `-0.0928` n `782`
- 4h: commodity avg `0.002` n `12`; crypto_alt avg `0.1032` n `230`; crypto_major avg `0.5978` n `8`; equity avg `0.8343` n `112`; fx avg `-0.0671` n `6`; index avg `0.1215` n `25`; metal avg `-0.1221` n `20`; unknown avg `0.0042` n `782`
- 24h: commodity avg `0.2339` n `12`; crypto_alt avg `0.6915` n `230`; crypto_major avg `1.1971` n `8`; equity avg `3.7063` n `109`; fx avg `-0.1432` n `6`; index avg `0.2774` n `25`; metal avg `0.4507` n `20`; unknown avg `0.3334` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal

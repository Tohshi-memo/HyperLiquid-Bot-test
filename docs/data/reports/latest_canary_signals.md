# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T23:16:40.912172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0476` n `12`; crypto_alt avg `0.0094` n `230`; crypto_major avg `0.0507` n `8`; equity avg `0.053` n `104`; fx avg `-0.0002` n `6`; index avg `0.0231` n `25`; metal avg `-0.0124` n `20`; unknown avg `0.0011` n `783`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `-0.0548` n `230`; crypto_major avg `-0.0057` n `8`; equity avg `0.0938` n `104`; fx avg `-0.0087` n `6`; index avg `0.0182` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.0691` n `783`
- 4h: commodity avg `-0.0776` n `12`; crypto_alt avg `-0.3048` n `230`; crypto_major avg `-0.4707` n `8`; equity avg `0.4471` n `104`; fx avg `0.0466` n `6`; index avg `0.0974` n `25`; metal avg `0.0205` n `20`; unknown avg `0.0721` n `783`
- 24h: commodity avg `-0.0544` n `12`; crypto_alt avg `0.2357` n `230`; crypto_major avg `0.0017` n `8`; equity avg `2.1222` n `104`; fx avg `-0.3187` n `6`; index avg `0.1118` n `25`; metal avg `-0.2862` n `20`; unknown avg `0.0832` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal

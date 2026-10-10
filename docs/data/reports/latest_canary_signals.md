# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T15:18:36.330590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `13`; crypto_alt avg `-0.0993` n `235`; crypto_major avg `-0.1018` n `8`; equity avg `-0.0097` n `150`; fx avg `0.0` n `6`; index avg `0.0015` n `26`; metal avg `0.0009` n `20`; unknown avg `1.0989` n `1109`
- 1h: commodity avg `0.0031` n `13`; crypto_alt avg `0.3589` n `235`; crypto_major avg `0.2795` n `8`; equity avg `0.0894` n `150`; fx avg `0.003` n `6`; index avg `0.0169` n `26`; metal avg `0.0004` n `20`; unknown avg `0.1051` n `1107`
- 4h: commodity avg `0.0868` n `13`; crypto_alt avg `0.8059` n `235`; crypto_major avg `0.6785` n `8`; equity avg `0.1274` n `150`; fx avg `-0.0038` n `6`; index avg `0.0149` n `26`; metal avg `0.003` n `20`; unknown avg `1.0142` n `1101`
- 24h: commodity avg `-0.5549` n `13`; crypto_alt avg `2.9712` n `235`; crypto_major avg `1.0802` n `8`; equity avg `0.3734` n `150`; fx avg `0.0043` n `6`; index avg `0.0596` n `26`; metal avg `0.0057` n `20`; unknown avg `1.2767` n `928`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T13:38:05.340393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0717` n `12`; crypto_alt avg `-0.1298` n `234`; crypto_major avg `-0.104` n `8`; equity avg `-0.3139` n `141`; fx avg `0.0059` n `6`; index avg `0.0007` n `26`; metal avg `-0.0167` n `20`; unknown avg `93.6842` n `944`
- 1h: commodity avg `-0.0875` n `12`; crypto_alt avg `-0.2706` n `234`; crypto_major avg `-0.5821` n `8`; equity avg `-0.3497` n `141`; fx avg `-0.0704` n `6`; index avg `-0.0189` n `26`; metal avg `-0.1551` n `20`; unknown avg `434.7206` n `942`
- 4h: commodity avg `-0.032` n `12`; crypto_alt avg `0.5067` n `234`; crypto_major avg `0.2949` n `8`; equity avg `-0.5076` n `141`; fx avg `-0.0383` n `6`; index avg `-0.037` n `26`; metal avg `-0.0612` n `20`; unknown avg `9.0958` n `936`
- 24h: commodity avg `-0.012` n `12`; crypto_alt avg `3.6845` n `234`; crypto_major avg `1.9913` n `8`; equity avg `1.0097` n `141`; fx avg `-0.2288` n `6`; index avg `0.2039` n `26`; metal avg `0.1164` n `20`; unknown avg `12.8473` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal

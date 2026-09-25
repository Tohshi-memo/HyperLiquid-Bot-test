# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T05:52:30.589768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `0.1792` n `234`; crypto_major avg `0.0222` n `8`; equity avg `0.0443` n `141`; fx avg `0.012` n `6`; index avg `0.0063` n `26`; metal avg `-0.0065` n `20`; unknown avg `3.1725` n `946`
- 1h: commodity avg `-0.0486` n `12`; crypto_alt avg `0.0325` n `234`; crypto_major avg `-0.0443` n `8`; equity avg `0.199` n `141`; fx avg `-0.0173` n `6`; index avg `0.0515` n `26`; metal avg `0.0246` n `20`; unknown avg `0.0872` n `942`
- 4h: commodity avg `-0.0441` n `12`; crypto_alt avg `-0.3159` n `234`; crypto_major avg `-0.4945` n `8`; equity avg `0.2551` n `141`; fx avg `-0.0868` n `6`; index avg `0.0613` n `26`; metal avg `-0.0812` n `20`; unknown avg `6.4741` n `936`
- 24h: commodity avg `0.3098` n `12`; crypto_alt avg `1.816` n `234`; crypto_major avg `0.3613` n `8`; equity avg `0.6741` n `141`; fx avg `-0.1444` n `6`; index avg `0.109` n `26`; metal avg `-0.1607` n `20`; unknown avg `17.0526` n `813`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal

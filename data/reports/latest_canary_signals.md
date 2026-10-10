# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T01:52:29.620356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `0.2827` n `235`; crypto_major avg `0.2352` n `8`; equity avg `0.0121` n `150`; fx avg `-0.0001` n `6`; index avg `0.0014` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.3834` n `1116`
- 1h: commodity avg `0.0084` n `13`; crypto_alt avg `0.1769` n `235`; crypto_major avg `0.2663` n `8`; equity avg `0.0121` n `150`; fx avg `-0.0031` n `6`; index avg `0.0059` n `26`; metal avg `-0.0155` n `20`; unknown avg `0.3575` n `1114`
- 4h: commodity avg `0.0109` n `13`; crypto_alt avg `1.2405` n `235`; crypto_major avg `0.6008` n `8`; equity avg `0.0954` n `150`; fx avg `0.0021` n `6`; index avg `0.0232` n `26`; metal avg `0.0063` n `20`; unknown avg `0.27` n `1108`
- 24h: commodity avg `-0.0254` n `13`; crypto_alt avg `2.3861` n `235`; crypto_major avg `0.6902` n `8`; equity avg `0.422` n `150`; fx avg `-0.0063` n `6`; index avg `0.0909` n `26`; metal avg `0.1922` n `20`; unknown avg `13.0305` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal

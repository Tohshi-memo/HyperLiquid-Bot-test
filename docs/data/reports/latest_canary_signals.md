# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T03:07:31.771067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0537` n `12`; crypto_alt avg `0.1771` n `234`; crypto_major avg `0.116` n `8`; equity avg `0.1697` n `141`; fx avg `-0.0164` n `6`; index avg `0.0192` n `26`; metal avg `0.057` n `20`; unknown avg `1.3991` n `944`
- 1h: commodity avg `-0.0668` n `12`; crypto_alt avg `-0.9716` n `234`; crypto_major avg `-0.7237` n `8`; equity avg `0.0058` n `141`; fx avg `-0.0415` n `6`; index avg `0.0089` n `26`; metal avg `-0.0423` n `20`; unknown avg `4.5718` n `944`
- 4h: commodity avg `-0.2807` n `12`; crypto_alt avg `-0.7893` n `234`; crypto_major avg `-0.2808` n `8`; equity avg `0.3381` n `141`; fx avg `-0.1392` n `6`; index avg `0.0988` n `26`; metal avg `-0.0084` n `20`; unknown avg `2.1419` n `938`
- 24h: commodity avg `0.4489` n `12`; crypto_alt avg `1.867` n `234`; crypto_major avg `0.5017` n `8`; equity avg `0.2817` n `141`; fx avg `-0.1331` n `6`; index avg `0.0212` n `26`; metal avg `-0.0577` n `20`; unknown avg `20.9625` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal

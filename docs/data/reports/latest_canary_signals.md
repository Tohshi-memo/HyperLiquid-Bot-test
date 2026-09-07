# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T12:52:28.643802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0408` n `12`; crypto_alt avg `0.3979` n `232`; crypto_major avg `0.1963` n `8`; equity avg `0.0142` n `134`; fx avg `0.0093` n `6`; index avg `0.0086` n `26`; metal avg `0.0017` n `20`; unknown avg `0.0718` n `796`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `0.9134` n `232`; crypto_major avg `0.602` n `8`; equity avg `-0.0144` n `134`; fx avg `-0.0121` n `6`; index avg `0.0002` n `26`; metal avg `0.0208` n `20`; unknown avg `6684.733` n `748`
- 4h: commodity avg `0.2441` n `12`; crypto_alt avg `1.2374` n `232`; crypto_major avg `0.6728` n `8`; equity avg `-0.0954` n `134`; fx avg `0.052` n `6`; index avg `-0.0506` n `26`; metal avg `-0.0909` n `20`; unknown avg `6720.9801` n `744`
- 24h: commodity avg `0.1613` n `12`; crypto_alt avg `0.918` n `232`; crypto_major avg `-0.4553` n `8`; equity avg `0.1234` n `134`; fx avg `-0.0891` n `6`; index avg `-0.0058` n `26`; metal avg `-0.146` n `20`; unknown avg `2.0144` n `616`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal

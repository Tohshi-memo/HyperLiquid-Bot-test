# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T07:22:25.716648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `0.0531` n `230`; crypto_major avg `0.1175` n `8`; equity avg `0.0475` n `108`; fx avg `0.0144` n `6`; index avg `0.0083` n `25`; metal avg `0.0311` n `20`; unknown avg `0.0234` n `782`
- 1h: commodity avg `-0.0341` n `12`; crypto_alt avg `0.2028` n `230`; crypto_major avg `0.0686` n `8`; equity avg `0.1367` n `108`; fx avg `0.0331` n `6`; index avg `0.023` n `25`; metal avg `0.0283` n `20`; unknown avg `0.0734` n `782`
- 4h: commodity avg `-0.0209` n `12`; crypto_alt avg `0.5015` n `230`; crypto_major avg `0.3948` n `8`; equity avg `-0.0219` n `108`; fx avg `0.0762` n `6`; index avg `-0.0163` n `25`; metal avg `-0.0178` n `20`; unknown avg `0.103` n `750`
- 24h: commodity avg `-0.1608` n `12`; crypto_alt avg `0.3886` n `230`; crypto_major avg `0.229` n `8`; equity avg `-1.902` n `108`; fx avg `0.0356` n `6`; index avg `-0.3576` n `25`; metal avg `0.1765` n `20`; unknown avg `0.9156` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1953`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T05:22:29.540408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `12`; crypto_alt avg `-0.0314` n `230`; crypto_major avg `0.0139` n `8`; equity avg `-0.1738` n `102`; fx avg `-0.0083` n `6`; index avg `-0.0393` n `25`; metal avg `-0.016` n `20`; unknown avg `-0.2051` n `774`
- 1h: commodity avg `-0.0579` n `12`; crypto_alt avg `0.1119` n `230`; crypto_major avg `0.1262` n `8`; equity avg `-0.1459` n `102`; fx avg `-0.0233` n `6`; index avg `-0.0249` n `25`; metal avg `-0.0649` n `20`; unknown avg `1.8707` n `774`
- 4h: commodity avg `-0.0806` n `12`; crypto_alt avg `0.6228` n `230`; crypto_major avg `0.4286` n `8`; equity avg `-0.5938` n `102`; fx avg `-0.0852` n `6`; index avg `-0.1187` n `25`; metal avg `-0.0488` n `20`; unknown avg `-0.3285` n `773`
- 24h: commodity avg `-0.7709` n `12`; crypto_alt avg `-3.8194` n `230`; crypto_major avg `-3.4202` n `8`; equity avg `-3.7488` n `102`; fx avg `-0.1522` n `6`; index avg `-0.8357` n `25`; metal avg `-0.3511` n `20`; unknown avg `1161.8241` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T17:22:25.942093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.167` n `12`; crypto_alt avg `-0.1446` n `228`; crypto_major avg `-0.2336` n `8`; equity avg `-0.0213` n `67`; fx avg `-0.0068` n `6`; index avg `0.0904` n `23`; metal avg `0.0157` n `18`; unknown avg `0.0753` n `418`
- 1h: commodity avg `-0.1874` n `12`; crypto_alt avg `-0.5743` n `228`; crypto_major avg `-0.3676` n `8`; equity avg `-0.087` n `67`; fx avg `0.0176` n `6`; index avg `-0.0367` n `23`; metal avg `-0.0267` n `18`; unknown avg `-0.0298` n `418`
- 4h: commodity avg `0.3719` n `12`; crypto_alt avg `-0.1019` n `228`; crypto_major avg `-0.654` n `8`; equity avg `-0.7499` n `67`; fx avg `-0.0153` n `6`; index avg `-0.6527` n `23`; metal avg `0.2737` n `18`; unknown avg `-0.6114` n `418`
- 24h: commodity avg `-1.1919` n `12`; crypto_alt avg `-0.9518` n `228`; crypto_major avg `-0.9117` n `8`; equity avg `-0.5543` n `67`; fx avg `-0.0638` n `6`; index avg `-0.5147` n `23`; metal avg `-1.0286` n `18`; unknown avg `-0.7636` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T05:22:34.054619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0312` n `12`; crypto_alt avg `0.0569` n `230`; crypto_major avg `0.0816` n `8`; equity avg `0.0211` n `92`; fx avg `0.0103` n `6`; index avg `0.0055` n `25`; metal avg `-0.0036` n `20`; unknown avg `0.0636` n `765`
- 1h: commodity avg `-0.0685` n `12`; crypto_alt avg `-0.1783` n `229`; crypto_major avg `-0.0553` n `8`; equity avg `-0.0218` n `92`; fx avg `0.0182` n `6`; index avg `0.0057` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.0964` n `765`
- 4h: commodity avg `-0.1145` n `12`; crypto_alt avg `-0.154` n `229`; crypto_major avg `-0.2376` n `8`; equity avg `-0.0197` n `92`; fx avg `0.0172` n `6`; index avg `0.0143` n `25`; metal avg `0.0156` n `20`; unknown avg `-0.3469` n `763`
- 24h: commodity avg `-0.4231` n `12`; crypto_alt avg `0.2802` n `229`; crypto_major avg `-0.2378` n `8`; equity avg `-0.6191` n `92`; fx avg `-0.1664` n `6`; index avg `0.0786` n `25`; metal avg `0.0009` n `20`; unknown avg `4.1844` n `730`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal

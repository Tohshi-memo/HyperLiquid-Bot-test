# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T11:52:29.932037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0504` n `12`; crypto_alt avg `0.0518` n `229`; crypto_major avg `0.1638` n `8`; equity avg `-0.0048` n `91`; fx avg `0.0039` n `6`; index avg `-0.0117` n `25`; metal avg `0.095` n `20`; unknown avg `-0.0301` n `766`
- 1h: commodity avg `0.0997` n `12`; crypto_alt avg `-0.1392` n `229`; crypto_major avg `-0.0444` n `8`; equity avg `0.1188` n `91`; fx avg `0.0194` n `6`; index avg `-0.0203` n `25`; metal avg `0.0367` n `20`; unknown avg `-0.0596` n `766`
- 4h: commodity avg `0.3068` n `12`; crypto_alt avg `0.5014` n `229`; crypto_major avg `0.7333` n `8`; equity avg `0.563` n `91`; fx avg `0.0233` n `6`; index avg `0.0742` n `25`; metal avg `-0.0148` n `20`; unknown avg `0.0825` n `765`
- 24h: commodity avg `-0.8587` n `12`; crypto_alt avg `1.2572` n `229`; crypto_major avg `2.0247` n `8`; equity avg `0.5322` n `91`; fx avg `-0.09` n `6`; index avg `0.1506` n `25`; metal avg `0.1571` n `20`; unknown avg `0.0016` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal

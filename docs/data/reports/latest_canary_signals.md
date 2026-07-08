# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T01:22:46.372118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0634` n `12`; crypto_alt avg `0.0024` n `229`; crypto_major avg `0.0632` n `8`; equity avg `0.1669` n `91`; fx avg `-0.0144` n `6`; index avg `-0.0144` n `25`; metal avg `0.1097` n `20`; unknown avg `-0.0816` n `763`
- 1h: commodity avg `-0.2053` n `12`; crypto_alt avg `0.171` n `229`; crypto_major avg `-0.075` n `8`; equity avg `0.6188` n `91`; fx avg `-0.0234` n `6`; index avg `0.1266` n `25`; metal avg `0.0781` n `20`; unknown avg `-0.1673` n `763`
- 4h: commodity avg `-0.1898` n `12`; crypto_alt avg `-0.0756` n `229`; crypto_major avg `-0.1445` n `8`; equity avg `0.7951` n `91`; fx avg `0.0331` n `6`; index avg `0.1447` n `25`; metal avg `-0.0336` n `20`; unknown avg `-0.1674` n `763`
- 24h: commodity avg `0.8179` n `12`; crypto_alt avg `-2.1158` n `229`; crypto_major avg `-1.6716` n `8`; equity avg `-1.4525` n `91`; fx avg `-0.2202` n `6`; index avg `-0.1849` n `25`; metal avg `-0.2574` n `20`; unknown avg `-0.1761` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal

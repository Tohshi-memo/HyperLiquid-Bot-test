# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T05:52:25.849750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.059` n `12`; crypto_alt avg `0.1726` n `230`; crypto_major avg `0.1364` n `8`; equity avg `0.0093` n `102`; fx avg `-0.0036` n `6`; index avg `-0.019` n `25`; metal avg `0.0285` n `20`; unknown avg `3.8063` n `784`
- 1h: commodity avg `0.0397` n `12`; crypto_alt avg `0.1866` n `230`; crypto_major avg `0.041` n `8`; equity avg `-0.0356` n `102`; fx avg `-0.0178` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0775` n `20`; unknown avg `2.9196` n `784`
- 4h: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.076` n `230`; crypto_major avg `-0.2336` n `8`; equity avg `0.0391` n `102`; fx avg `-0.0178` n `6`; index avg `0.0029` n `25`; metal avg `-0.0129` n `20`; unknown avg `1.5072` n `784`
- 24h: commodity avg `-0.2451` n `12`; crypto_alt avg `-0.8185` n `230`; crypto_major avg `-0.6085` n `8`; equity avg `0.8592` n `102`; fx avg `-0.2331` n `6`; index avg `0.0095` n `25`; metal avg `-0.0783` n `20`; unknown avg `0.991` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal

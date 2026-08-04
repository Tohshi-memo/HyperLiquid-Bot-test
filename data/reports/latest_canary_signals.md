# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T01:07:33.609516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0583` n `12`; crypto_alt avg `0.0964` n `230`; crypto_major avg `0.0963` n `8`; equity avg `-0.1098` n `107`; fx avg `-0.0088` n `6`; index avg `-0.0441` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.0979` n `780`
- 1h: commodity avg `0.0421` n `12`; crypto_alt avg `-0.3721` n `230`; crypto_major avg `-0.3025` n `8`; equity avg `-1.0156` n `107`; fx avg `-0.1027` n `6`; index avg `-0.2349` n `25`; metal avg `-0.1167` n `20`; unknown avg `0.1175` n `780`
- 4h: commodity avg `0.1459` n `12`; crypto_alt avg `-0.5315` n `230`; crypto_major avg `-0.6429` n `8`; equity avg `-0.6367` n `107`; fx avg `-0.0455` n `6`; index avg `-0.1368` n `25`; metal avg `-0.0733` n `20`; unknown avg `0.1728` n `780`
- 24h: commodity avg `0.089` n `12`; crypto_alt avg `0.3174` n `230`; crypto_major avg `0.1323` n `8`; equity avg `0.8873` n `107`; fx avg `-0.0311` n `6`; index avg `0.0239` n `25`; metal avg `-0.2084` n `20`; unknown avg `0.095` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
